---
author-meta:
- The Anopheles gambiae 1000 Genomes Consortium
bibliography:
- content/manual-references.json
date-meta: '2020-08-18'
header-includes: '<!--

  Manubot generated metadata rendered from header-includes-template.html.

  Suggest improvements at https://github.com/manubot/manubot/blob/master/manubot/process/header-includes-template.html

  -->

  <meta name="dc.format" content="text/html" />

  <meta name="dc.title" content="Genome variation and population structure in three African malaria vector species within the *Anopheles gambiae* complex" />

  <meta name="citation_title" content="Genome variation and population structure in three African malaria vector species within the *Anopheles gambiae* complex" />

  <meta property="og:title" content="Genome variation and population structure in three African malaria vector species within the *Anopheles gambiae* complex" />

  <meta property="twitter:title" content="Genome variation and population structure in three African malaria vector species within the *Anopheles gambiae* complex" />

  <meta name="dc.date" content="2020-08-18" />

  <meta name="citation_publication_date" content="2020-08-18" />

  <meta name="dc.language" content="en-GB" />

  <meta name="citation_language" content="en-GB" />

  <meta name="dc.relation.ispartof" content="Manubot" />

  <meta name="dc.publisher" content="Manubot" />

  <meta name="citation_journal_title" content="Manubot" />

  <meta name="citation_technical_report_institution" content="Manubot" />

  <meta name="citation_author" content="The Anopheles gambiae 1000 Genomes Consortium" />

  <link rel="canonical" href="https://malariagen.github.io/ag1000g-phase3-data-paper/" />

  <meta property="og:url" content="https://malariagen.github.io/ag1000g-phase3-data-paper/" />

  <meta property="twitter:url" content="https://malariagen.github.io/ag1000g-phase3-data-paper/" />

  <meta name="citation_fulltext_html_url" content="https://malariagen.github.io/ag1000g-phase3-data-paper/" />

  <meta name="citation_pdf_url" content="https://malariagen.github.io/ag1000g-phase3-data-paper/manuscript.pdf" />

  <link rel="alternate" type="application/pdf" href="https://malariagen.github.io/ag1000g-phase3-data-paper/manuscript.pdf" />

  <link rel="alternate" type="text/html" href="https://malariagen.github.io/ag1000g-phase3-data-paper/v/48d9a76b45b41aa1711cd5df6d1990d3354d7875/" />

  <meta name="manubot_html_url_versioned" content="https://malariagen.github.io/ag1000g-phase3-data-paper/v/48d9a76b45b41aa1711cd5df6d1990d3354d7875/" />

  <meta name="manubot_pdf_url_versioned" content="https://malariagen.github.io/ag1000g-phase3-data-paper/v/48d9a76b45b41aa1711cd5df6d1990d3354d7875/manuscript.pdf" />

  <meta property="og:type" content="article" />

  <meta property="twitter:card" content="summary_large_image" />

  <link rel="icon" type="image/png" sizes="192x192" href="https://manubot.org/favicon-192x192.png" />

  <link rel="mask-icon" href="https://manubot.org/safari-pinned-tab.svg" color="#ad1457" />

  <meta name="theme-color" content="#ad1457" />

  <!-- end Manubot generated metadata -->'
keywords:
- malaria
- anopheles
- genomics
lang: en-GB
manubot-clear-requests-cache: false
manubot-output-bibliography: output/references.json
manubot-output-citekeys: output/citations.tsv
manubot-requests-cache-path: ci/cache/requests-cache
title: Genome variation and population structure in three African malaria vector species within the *Anopheles gambiae* complex
...






<small><em>
This manuscript
([permalink](https://malariagen.github.io/ag1000g-phase3-data-paper/v/48d9a76b45b41aa1711cd5df6d1990d3354d7875/))
was automatically generated
from [malariagen/ag1000g-phase3-data-paper@48d9a76](https://github.com/malariagen/ag1000g-phase3-data-paper/tree/48d9a76b45b41aa1711cd5df6d1990d3354d7875)
on August 18, 2020.
</em></small>

## Authors



+ **The Anopheles gambiae 1000 Genomes Consortium**<br><br>
  <small>
  </small>



## Abstract {.page_break_before}




## Population Sampling

DNA extracted from wild-caught _Anopheles_ mosquitoes were submitted to the Ag1000G consortium in 23 sets by consortial partners. (chris' line)

![Sample Collection Map](images/sample_collection_map.svg){#fig:sample_collection_map width="100%"}

## Whole Genome Sequencing and Alignment {.page_break_before}

A total of 4,693 individual mosquitoes were sequenced on either Illumina HiSeq2000 (n=3,130) or Illumina HiSeqX (n=1,563) to a target coverage of 30X.

Between machine types the median number of bases sequenced per sample was 9.76Gb and 10.33Gb respectively, representing a difference in yield (two-tailed mann-whitney U p < 0.0001).

These values correspond to a yield per reference base (vs AgamP4) of 35.76X and 37.82X. 

91.9% of HiSeqX runs and 80.5% of HiSeq2000 runs met the target yield of 30X.

Reads were aligned to the AgamP4 reference genome using `bwa` version `0.7.15`.

Indel realignment was performed using GATK `v3.7-0` RealignerTargetCreator and IndelRealigner. 

Single nucleotide polymophisms were called against AgamP4 using GATK UnifiedGenotyper `v3.7-0`.

Sample genotypes were called independently, in genotyping mode, given all possible alleles at each site, allowing parallelisation over samples.

Coverage considered at individual sites was capped at 250.

Full details of pipelines including all parameter settings are provided in supplementary.

All samples successfully completed the pipeline and entered the sample quality control (QC) process.

### Sample QC

The sample QC process was composed of three stages, sequence quality assurance, replicate handling, and anomaly detection.

668 samples were removed where sequencing was of insufficient quality to accurately call genotypes across the whole genome.

Exclusions were due to poor coverage (n=410), potential contamination (n=229), and the autosomal vs X coverage ratio not following the expected bimodal distribution (n=29).

Where technical replicates were available, we excluded 4 pairs (8 samples) with low genotype concordance. 

Where pairs met the concordance threshold we excluded the lower quality sample.

In total 407 samples in were excluded in favour of better quality samples, based on skewedness of the mean vs median.

Samples were also screened pairwise within submission sets for unexpected pairs, though none were detected.

The AG1000G-X submission set, made up of laboratory experimental crosses, was exempted from the requirements of this stage due to familial similarity and high levels of inbreeding.

The third stage used principal component analysis (PCA) to identify and exclude individual samples that were outliers based on available metadata.

A review process identified samples that could not be explained parsimoniously, and were therefore likely to be sample mix ups or instances of mislabelling.

28 samples were excluded as they respectively dominated the first principal components, indicating high divergence from all other samples and therefore likely members of other Anopheline species.

A further 82 samples were excluded as potential sample mix ups.

Following all sample QC steps, 3,483 samples (74.2%) were retained from the original cohort for analysis.

Full details including exclusion thresholds are available in supplementary.

### Coverage

Summary of site coverage post QC exclusions.

### SNP filtering and quality

Site filtering is necessary to ensure that reported variation is of high quality.

Features of specific regions of the Anopheles genome contribute to calling errors in short-read technologies; such features include regions of high divergence from the reference, high homology between regions, copy number variation, or the presence of transposable elements.

Owing to DNA availability, no second technology was available for direct benchmarking.

Using the 15 available Anopheles pedigrees previously described, we used the presence of mendelian error at sites as a proxy for genotype discordance.

Where previously we have used manually curated cutoffs based on observed mendelian error rates to filter sites (ref phase1, phase2), here we built a statistical model where cohort level genome annotations were used to predict the presence of mendelian error, becoming a binary classification problem.

Pedigrees included _A. gambiae_ and _A. coluzzii_ mosquitoes only, and cohort level annotations to build the initial site filters model came from these species (n=XXX). 

5 of the 15 crosses were held out for validation, so performance could be evaluated against the previous site filtering scheme.

Sites were defined as PASS where all genotypes across all 10 remaining crosses were called, and no mendelian inconsistencies were observed.

Sites were defined as FAIL where a mendelian inconsistency was observed in any pedigree.

All other sites were not considered eligible for inclusion in model training.

A balanced training set was generated from the remaining 10 crosses containing XXX autosomal(?) sites.

We applied a decision tree, as it provides clear unambiguous decisions, and is similar in concept to the set of filters commonly used in non-model organism genomics.

A set of trees with different parameter settings were learned, exploring the depth of trees, and the number of samples allowed at a terminal node.

Parameter settings were evaluated on an unbalanced evaluation set, consisting of XXX sites randomly from sampled from the whole genome.

The leaves of the trained models contain different proportions of PASS sites, by increasing the cutoff for these proportions required to label a leaf as PASS, we were able to compute the area under the receiver operating curve (AUROC) for each parameter set.

The best performing parameter set based on AUROC was selected as the final model, the classification cutoff used was optimised based on the Youden statistic.

The resulting model was a decision tree of depth 8, with a maximum of 50 terminal nodes, where leaves were assigned to PASS where > 0.533 of training data in that leaf were PASS.

All sites in the genome were then assigned to PASS or FAIL given the model inputs.

The 5 remaining cross pedigrees were used to perform a final evaluation of the approach.

The above definitions of PASS sites were retained, but independently over pedigrees, providing 5 distinct evaluation sets.

Before applying the site filters, the mendelian error rate of the 5 crosses over all autosomal sites ranged between XXX and XXX (table XXX).

The application of the site filters mask defines the accessible fraction of the genome at 70%, and reduces the mendelian error rate by a median factor of 10x on the autosomes.

In all 5 crosses the Youden score was substantially increased by a median factor of XXX.

Directly comparing the numbers to the phase 2 site filters, we observe similar levels of mendelian error, however the updated site filters have a substantially higher sensitivity, yielding a higher Youden score over all crosses and chromosomes.

- Table A: Mendel errors per cross per chromosome. 
row indices: chromosome and raw/filtered
column indexes: crosses + frac accessible.
ie 10 rows, and 6 columns.

- Table B: comparison of 3 vs 2.
row indices: as above
column indices: MER, frac accessible, Youden, each for 2 and 3.
ie 10 rows, and 6 columns.

Site filters on arab and gamb_colu_arab.

As genomic features vary between species, different sets of site filters were generated to allow high quality analyses both within and between species. 

The `gamb_colu` site filters were generated as above, and are appropriate for analyses that include _gambiae_ and _coluzzii_ samples only.

The `arab` site filters were generated following application of the model to the summary variables from arabiensis samples in the cohort (n=XXX), this set of site filters are appropriate when working with _A. arabiensis_ samples only.

Finally, the `gamb_colu_arab` site filters allow analyses across all three species and are the intersection of the `gamb_colu` and the `arab` site filters.

Rather than mendelian errors, on the hemizygous chromosome we can use the more direct measure of heterozygote calls in males.

In the dataset are 220 male samples identified as gambiae/coluzzii, each of these represent an independent proxy for genotype discordance.

Pre-application of the site filters, the median heterzygosity rate on X was 0.44%, and post filtering this drops to 0.12% (table XX).

The median fold change in error rate was -1.74, with 69.97% of the X chromosome passing site filters.

? (Also some measure of GQ? when applied to the X chromosome).

? Direct comparison to the phase 2 site filters is favourable; we observe similar levels of mendelian error, but with substantially higher sensitivity, yielding a higher Youden score over all crosses and chromosomes.

- Table A: Mendel errors per cross per autosome. 
row indices: chromosome and raw/filtered
column indexes: crosses + frac accessible.
ie 8 rows, and 6 columns.

- Table B: comparison of cross and X
row indices: raw/filtered
column indices: MER, frac accessible, Youden, each for 2 and 3.
column indexes: crosses + frac accessible.
ie 2 rows, and 6 columns.

::: {style="font-size: 8pt"}
```table
---
caption: 'Result of heterozygote calls on male X chromosome'
alignment: LLLLLLLL
include: content/tables/mer_X.csv
csv-kwargs:
  dialect: unix
width: [0.2, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1, 0.1]
---
```
:::

### Genome accessibility

We define accessibility as the fraction of sites in a region passing the appropriate set of site filters.

Overall, 70% of the genome, and ??% of the exome are considered accessible in the `gamb_colu` set.

This is an improvement from phase 2, where XXX of the genome, and YYY of the exome was considered accessible.

As expected, accessiblity was generally lower around the centromeres, and in regions of heterochromatin (table ref).

One notable region of low accessibility spans 40-41Mbp of chromosome 3R, this corresponds to ??.

Accessibility of the `arab` site filters closely follows that of `gamb_colu`, with the exception of the X chromosome where we see a substantially lower rate.

This appears to be driven by high divergence between AgamP4 and our _A. arabiensis_ samples, particularly around the Xag inversion at Q-Q Mbp, ref figure.

On the autosomes the divergence from the reference is comparable between _A.arabiensis_ and _A. gambiae_/ _A. coluzzii_ samples, suggesting there is 

The median divergence (Dxy) of 100kbp windows is XXX (5%/95% TTT/SSS) for gambiae/coluzzii and YYY (TTT/YYY) for arabiensis.  

On the X chromosome these values are XXX ( / ) for gambiae/coluzzii and YYY (  / ) for arabiensis.
 
### SNP discovery

Overall, we report XX,XXX,SSS single nucleotide polymophisms (SNPs) segregating in this cohort that pass filters, of which XX,XXX (%) are multiallelic.

12,223 SNPs are segregating in both species groups, while XXX are private to gambiae_/coluzzii_ and YYY to arabiensis [fig ref].

This phase of the study reports an additional XXX SNPs from phase 2.

In XXX gambiae and coluzzii individuals we report 12,222,222 SNPs (Q% multiallelic), corresponding to a SNP every 1.6 accessible bases.

In XXX arabiensis individuals we identify 10,000,000 SNPs (Q% multiallelic), a SNP every 2.5 accessible bases.

## Species Assignment

## Population Structure

## Genetic Diversity within Populations

## Insecticide Resistance

## Gene Drive


## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>
