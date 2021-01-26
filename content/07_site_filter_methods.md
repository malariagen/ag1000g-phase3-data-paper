## Site filtering}\label{sec:snp-filtering}

We developed filters that identify genomic sites where SNP calling and genotyping is likely to be less reliable in one or more mosquito species.
%
To guide the design and calibration of the site filters, we made use of the 15 colony crosses included in Ag1000G phase 3.
%
Each cross comprises two parents and up to 20 progeny, and thus it is possible to identify sites where genotypes in one or more progeny are not consistent with Mendelian inheritance (Mendelian errors).
%
A small number of Mendelian errors may be due to \textit{de novo} mutation, but the vast majority of Mendelian errors are likely to be due to errors in sequencing, alignment or SNP calling.
%
The general approach we took was to use Mendelian consistency to identify sets of positive and negative training sites, then used these to train a machine learning model that classified all genomic sites as either PASS or FAIL.


### Site filters for use with \agamb and/or \acolu


All the 15 crosses involved \agamb and/or \acolu parents, and none of the crosses involved \aarab, so we used the crosses to first develop site filters suitable for use with \agamb and/or \acolu.
%
Hereafter we refer to these filters as the ``\texttt{gamb\_colu}'' site filters.
%
Five of the 15 crosses were held out for validation, so performance could be evaluated objectively.
%
Sites were assigned to the positive training set where all genotypes across all 10 crosses were called, and no Mendelian errors were observed.
%
Sites were assigned to negative training set where one or more Mendelian errors were observed in any cross.
%
All other sites were not considered eligible for inclusion in model training.
%
A balanced training set was then generated containing 100,000 autosomal sites from each of the positive and negative training sets.


The inputs to the machine learning model were a set of per-site summary statistics computed from the sequence read alignments and SNP genotypes across all wild-caught \agamb and \acolu individuals.
%
These input summary statistics are described further in the appendix.
%
Male individuals were excluded from the summary statistic calculations, so that the model could also be applied without modification to the X chromosome.
%
We used these summary statistics, together with the positive and negative training sites, to train a decision tree model.
%
We initially trained a set of trees with different hyperparameter values, exploring the depth of trees, and the number of samples allowed at a terminal node.
%
Each of these trees was evaluated on an unbalanced set of sites randomly sampled from the whole genome (2\% of all sites, without replacement).
%
Leaves of these trees contained different proportions of positive and negative training sites, and by increasing the cutoff for these proportions required to label a leaf as PASS, we were able to compute the area under the receiver operating curve (AUROC) for each set of hyperparameter values.
%
The best performing hyperparameter set based on AUROC was selected as the final model, and the leaf classification cutoff used was optimised based on the Youden statistic.
%
The resulting model was a decision tree of depth 8, where leaves were assigned to PASS where > 0.533 of training data in that leaf were positive training sites.
%
All sites in the genome were then assigned to PASS or FAIL via this model.


The 5 remaining cross pedigrees were used to perform a final evaluation of the approach.
%
For each of these crosses, we computed the Mendelian error rate (fraction of variants with one or more Mendelian errors among progeny) before and after applying the site filters, to provide five independent evaluation results.
%
We also evaluated performance on the X chromosome using heterozygote calls in males as an error indicator.
%
The fraction of variants with a heterozygous genotype call in or more males was computed before and after applying site filters.
%
Male error rates were estimated from genotype calls with a minimum Genotype Quality (GQ) value of 30.
%
Performance of the decision tree model was better than the hand-crafted site filters created during the previous project phase (Ag1000G phase 2), with lower Mendelian error rates, and a larger number of sites passing the filter.
%
Full performance metrics will be reported in a future publication.


### Site filters for use with \aarab

To generate site filters for use with \aarab, we recomputed site summary statistics using only wild-caught \aarab individuals, then applied the decision tree model described above.
%
These filters, which we refer to as the ``\texttt{arab}'' site filters, are appropriate when working with \aarab samples only.


### Site filters for joint analyses of all three species

We created site filters suitable for joint analysis of individuals from all three species by taking the intersection of the \texttt{gamb\_colu} and the \texttt{arab} site filters.
%
We refer to these filters as the ``\texttt{gamb\_colu\_arab}'' site filters.




