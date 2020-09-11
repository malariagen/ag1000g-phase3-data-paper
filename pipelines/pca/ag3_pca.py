import psutil
from humanize import naturalsize
import numba
import numpy as np
import dask.array as da

__version__ = '0.1.0'

class Util:

  def show_memory(self):
      vm = psutil.virtual_memory()
      print(f"{naturalsize(vm.used)} used, {naturalsize(vm.available)} available, {naturalsize(vm.total)} total")


  # Define a function to return the genotype data for a given chromosome region, for a given sample set.
  # Use the specified intake catalog.
  def load_genotype_calldata(self, cat, sample_set, chrom_arm, region_slice_obj):
      print('- load_genotype_calldata', sample_set, chrom_arm, region_slice_obj)
      zarr_data = cat.ag3.snp_genotypes(sample_set=sample_set).to_zarr()
      return da.from_zarr(zarr_data[chrom_arm]["calldata"]["GT"])[region_slice_obj]


  # Define a function to count the presence of each allele in a given array of genotypes (samples * variants * alleles)
  # and return an array of allele counts with a row for each possible allele (limited by max_allele) for each sample, and column for each variant
  @staticmethod
  @numba.njit(
      numba.int8[:, :](numba.int8[:, :, :], numba.int8), nogil=True)
  def numpy_genotype_tensor_to_allele_counts_melt(gt, max_allele):
      # Create an array of zeros (for defaults) with the same number of colums (variants) as the genotype array but a row for each allele, for each sample
      out = np.zeros((gt.shape[0] * (max_allele + 1), gt.shape[1]), dtype=np.int8)
      # For each row (sample) in the genotype array
      for i in range(gt.shape[0]):
          # For each column (variant) in the genotype array
          for j in range(gt.shape[1]):
              # For each allele in the genotype array 
              for k in range(gt.shape[2]):
                  allele = gt[i, j, k]
                  # If the value in the genotype array at this row and colum and 3rd dimension (i.e. the allele value) is between 0 and max_allele  
                  if 0 <= allele <= max_allele:
                      # Increment the value of the `out` array at the row corresponding to this allele for this sample, at the corresponding variant column
                      out[(i * (max_allele + 1)) + allele, j] += 1
      return out


  # Define a function to apply the above function chunk-wise
  def dask_genotype_tensor_to_allele_counts_melt(self, gt, max_allele):

      # Determine output chunks - change axis 0; preserve axis 1; drop axis 2.
      dim0_chunks = tuple(np.array(gt.chunks[0]) * (max_allele + 1))
      chunks = (dim0_chunks, gt.chunks[1])

      return gt.map_blocks(
          Util.numpy_genotype_tensor_to_allele_counts_melt,
          max_allele=max_allele,
          chunks=chunks,
          dtype="i1",
          drop_axis=2,
      )
