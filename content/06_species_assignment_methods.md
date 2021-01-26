## Species assignment

We assigned a species to each individual that passed sample QC using their genomic data, via two independent methods: ancestry-informative markers (AIMs) and principal components analysis (PCA).


### Species calling via ancestry-informative markers

To derive AIMs between _A. arabiensis_ and _A. gambiae_, we used publicly available data from the _Anopheles_ 16 genomes project (@doi:10.1126/science.1258522). 

Whole genome SNP calls for 12 _A. arabiensis_ and 38 _A. gambiae_ individuals were used.

Alleles were mapped onto the same alternate allele space, and allele frequencies were computed for both species.

Sites that were multiallelic in either group were excluded, as well as sites where any genotypes were missing. 

565,329 SNPs were identified as potentially informative, where no shared alleles were present between groups.

These were spread throughout the genome, but were concentrated on the X chromosome (63.2%), particularly around the Xag inversion.

We randomly down-sampled these SNPs to a set of 50,000 AIMs, then computed the fraction of alleles at these SNPs that were arabiensis-like for each individual in the Ag1000G phase 3 cohort.

Given the relatively small number of _A. arabiensis_ samples in the 16 genomes project, it was clear that a significant proportion of putative AIMs were not likely to be truly informative across the broader sampling in Ag1000G.

Individuals in Ag1000G were classed as _A. arabiensis_ where a fraction >0.8 of alleles were arabiensis-like.

To resolve the non-_A. arabiensis_ individuals into _A. gambiae_ and _A. coluzzii_, we applied the AIMs previously used in @doi:10.1101/gr.262790.120.

For each individual, we computed the fraction of coluzzii-like alleles at these AIMs.

Individuals were called as _A. gambiae_ where this fraction was <0.12 and _A. coluzzii_ where this fraction was >0.9, with individuals in between classed as intermediate.


### Species calling via principal components analysis

To provide a complementary view of species assignments, we also used the results of the principal components analysis of Chromosome 3 computed during the outlier analysis described above.

Based on a comparison with the AIM species calls, it was apparent that the first two principal components could be used to assign species.

Individuals where PC1 > 150 were called as _A. arabiensis_.

Individuals where PC1 < 0 and PC2 > -7 were called as _A. gambiae_.

Individuals where PC1 < 0 and PC2 < -24 were called as _A. coluzzii_.

All other individuals were called as intermediate.

The results of the PCA and AIM species calls were highly concordant in most sample sets, except for the Far West (Guinea-Bissau, The Gambiae) and Far East (Kenya, Tanzania).

Further investigation is required to resolve the species status of these individuals.

