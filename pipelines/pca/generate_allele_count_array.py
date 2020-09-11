from dask_kubernetes import KubeCluster
from dask.distributed import Client, progress
import dask.array as da
import numpy as np
import zarr
import allel
import ag3_pca

import sys
sys.path.insert(0, snakemake.params.module_path)
import ag3

dask_genotype_tensor_to_allele_counts_melt = ag3_pca.Util().dask_genotype_tensor_to_allele_counts_melt

try:

    n_workers = snakemake.params.n_workers
    regions = snakemake.params.regions
    query_str = snakemake.params.sample_query
    max_allele = snakemake.params.max_allele
    n_downsample_variants = snakemake.params.n_downsample
    species_group = snakemake.wildcards.species_group
    random_seed = snakemake.params.random_seed
    
    # cluster setup
    cluster = KubeCluster()
    cluster.scale_up(n_workers)
    
    # dask client setup
    client = Client(cluster)
    print(cluster.dashboard_link)

    # grab data from release
    v3 = ag3.release_data()
    
    sample_sets = v3.all_wild_sample_sets

    # load_metadata
    metadata = v3.load_sample_set_metadata(sample_sets)
    
    sample_loc = metadata.eval(query_str).values
    assert sample_loc.sum() > 0, "Must select >0 samples"
    
    genotypes = []
    site_filters = []

    for chrom, start, stop in regions:

        print(chrom, start, stop)
        pos = allel.SortedIndex(
            v3.load_variants(chrom))

        ix = pos.locate_range(start, stop)

        gt = v3.load_sample_set_calldata(chrom, sample_set=sample_sets)[ix]

        mask = v3.load_mask(chrom, species_group)[ix]
        g = da.compress(sample_loc, gt, axis=1)

        genotypes.append(g)
        site_filters.append(mask)
    
    genotype_data = da.concatenate(genotypes, axis=0)
    site_filters_data = da.concatenate(site_filters, axis=0)
    
    melted_allele_counts = dask_genotype_tensor_to_allele_counts_melt(genotype_data, max_allele=max_allele)
    
    # Get the number of genotyped samples
    number_of_samples = genotype_data.shape[1]
    print("Number of samples", number_of_samples)
    
    # Sum the allele counts
    allele_count_sums = da.sum(melted_allele_counts, axis=1, dtype='int16')
    
    # Determine which alleles meet the criteria, and record as a Boolean array.
    loc_midfreq_alleles = (allele_count_sums >= 2) & (allele_count_sums <= ((number_of_samples * 2) - 2))
    
    # Transform the Boolean site_filter index into the same space as the melted allele counts.
    loc_accessible = da.repeat(site_filters_data, max_allele + 1) # 4 alleles
    
    # Check that loc_accessible is the same shape as loc_midfreq_alleles
    assert loc_accessible.shape == loc_midfreq_alleles.shape

    # Determine the corresponding array indices for all of the mid-frequency alleles that are accessible
    # We use the '&' to choose sites that meet the critera AND are accessible.
    midfreq_alleles_as_indices = da.nonzero(loc_midfreq_alleles & loc_accessible)[0]
    
    # Compute (and bring into client memory) the midfreq_alleles_as_indices
    ix_select = midfreq_alleles_as_indices.compute()
    
    # Set/reset the random seed used for random variant selection
    # to ensure that we always select the same set of random variants
    np.random.seed(random_seed)

    # Randomly choose `n_downsample_variants` items from the array of accessible mid-frequency allele indices
    downsampled_site_indices = np.random.choice(
        ix_select, 
        size=n_downsample_variants, 
        replace=False)

    # Sort the indices to allow contiguous parsing
    downsampled_site_indices.sort()

    # From the melted_allele_counts array, take the corresponding indices
    downsampled_allele_counts = da.take(melted_allele_counts, downsampled_site_indices, axis=0)

    computed_downsampled_allele_counts = downsampled_allele_counts.compute()
    
    # finally save to zarr...
    z = zarr.ZipStore(snakemake.output.zipzarr)
    zg = zarr.group(z)
    zg.create_dataset("allele_counts_pca_ready", data=computed_downsampled_allele_counts)
        
finally:
    cluster.close()
