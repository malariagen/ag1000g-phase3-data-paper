---
author-meta:
- The Anopheles gambiae 1000 Genomes Consortium
bibliography:
- content/manual-references.json
date-meta: '2021-01-25'
header-includes: '<!--

  Manubot generated metadata rendered from header-includes-template.html.

  Suggest improvements at https://github.com/manubot/manubot/blob/master/manubot/process/header-includes-template.html

  -->

  <meta name="dc.format" content="text/html" />

  <meta name="dc.title" content="Genome variation and population structure in three African malaria vector species within the *Anopheles gambiae* complex" />

  <meta name="citation_title" content="Genome variation and population structure in three African malaria vector species within the *Anopheles gambiae* complex" />

  <meta property="og:title" content="Genome variation and population structure in three African malaria vector species within the *Anopheles gambiae* complex" />

  <meta property="twitter:title" content="Genome variation and population structure in three African malaria vector species within the *Anopheles gambiae* complex" />

  <meta name="dc.date" content="2021-01-25" />

  <meta name="citation_publication_date" content="2021-01-25" />

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

  <link rel="alternate" type="text/html" href="https://malariagen.github.io/ag1000g-phase3-data-paper/v/4b1fdeee62538db3fcb990f9e230bb26c7d12884/" />

  <meta name="manubot_html_url_versioned" content="https://malariagen.github.io/ag1000g-phase3-data-paper/v/4b1fdeee62538db3fcb990f9e230bb26c7d12884/" />

  <meta name="manubot_pdf_url_versioned" content="https://malariagen.github.io/ag1000g-phase3-data-paper/v/4b1fdeee62538db3fcb990f9e230bb26c7d12884/manuscript.pdf" />

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
([permalink](https://malariagen.github.io/ag1000g-phase3-data-paper/v/4b1fdeee62538db3fcb990f9e230bb26c7d12884/))
was automatically generated
from [malariagen/ag1000g-phase3-data-paper@4b1fdee](https://github.com/malariagen/ag1000g-phase3-data-paper/tree/4b1fdeee62538db3fcb990f9e230bb26c7d12884)
on January 25, 2021.
</em></small>

## Authors



+ **The Anopheles gambiae 1000 Genomes Consortium**<br><br>
  <small>
  </small>



## Abstract {.page_break_before}




## Population Sampling

The third and final phase of the Ag1000g project data resource contains wild-caught _Anopheles_ mosquito genomes from Sub-Saharan Africa, collected from a total of 124 sites across 19 countries, 6 of which are novel.

Collections from Mali increase the density of coverage in West Africa, Central African Republic and Democratic Republic of Congo begin to fill the gap previously present in Central Africa while Malawi, Mozambique and Tanzania provide much more power to analyse East African malaria vectors, including _A. arabiensis_ an important vector species not previously sequenced in the project.

Alongside sampling from natural populations, we include colony individuals from a number of laboratory crosses, comprising 11 crosses that were released as part of phase 2, and 4 additional pedigrees.

![Sample Collection Map](images/sample_collection_map.svg){#fig:sample_collection_map width="100%"}

## Whole Genome Sequencing and Alignment {.page_break_before}

4,693 individual mosquito genomes were sequenced on either Illumina HiSeq2000 (n=3,130) or Illumina HiSeqX (n=1,563) to a target coverage of 30X.

Between machine types the median number of bases sequenced per sample was 9.76Gb and 10.33Gb respectively, representing a difference in yield (two-tailed mann-whitney U p < 0.0001).

These values correspond to a yield per reference base (vs AgamP4) of 35.76X and 37.82X. 

91.9% of HiSeqX runs and 80.5% of HiSeq2000 runs met the target yield of 30X.

Reads were aligned to the AgamP4 reference and Single Nucleotide Polymophisms (SNPs) called using GATK UnifiedGenotyper.

All samples successfully completed the pipeline and entered the sample quality control (QC) process.

### Sample QC

For wild-caught samples (n=XXXX), the QC process was composed of three stages, sequence quality assurance, replicate handling, and anomaly detection.

A total of 668 samples were removed where sequencing was of insufficient quality to accurately call genotypes across the whole genome.

Exclusions were due to poor coverage (n=410), potential contamination (n=229), and an ambiguous sex call (n=29).

Where technical replicates were available, we excluded 4 pairs (8 samples) with low genotype concordance. 

Where pairs met the concordance threshold we excluded the lower quality sample (n=407).

Samples were also screened pairwise within submission sets for unexpected pairs, though none were detected.

The third stage used principal component analysis (PCA) to identify and exclude individual samples that were outliers based on available metadata.

A review process identified samples that could not be explained parsimoniously, and were therefore likely to be sample mix ups or instances of mislabelling.

28 samples were excluded as they respectively dominated the first principal components, indicating high divergence from all other samples and therefore likely members of other Anopheline species.

A further 82 samples were excluded as potential sample mix ups.

Following all sample QC steps, 3,483 wild-caught samples (74.2%) were retained from the original cohort for analysis.

This represents an additional 1,823 mosquitoes relative to the phase 2 release.

Due to a change in assessment of sample quality where technical replicates are available, the preferred replicate was changed for 172 mosquitoes between phase 2 and phase 3.

9 samples included in phase 2 are not present in this release (sup XXX).

The AG1000G-X submission set, made up of laboratory experimental crosses, was subject to a slightly different QC process.

Firstly an analysis based on rates of Mendelian error identified true fathers of crosses (where multiple males were introduced to cages), and validated provided pedigrees.

Of the 7XX samples provided we were able to validate 15 crosses to a high level of confidence, comprising 299 samples.

4 of these crosses are novel relative to phase 2.

These samples went through a modified sequence quality assurance process, where 1 sample was removed for insufficient coverage (methods).

The final data release therefore comprises 3,XXX samples, XXX from laboratory crosses, and YYY wild collected samples.

### Coverage

%% TO DO
%% (PLOTS DONE, but numbers needed).

Summary of site coverage post QC exclusions.

- ie what frac of the genome is at 1X median
- what frac at 10X. 
- What frac of exome
- what frac of X

At this point we do not mention arabiensis.

### Species assignment and sex calling

The Anopheles gambiae complex is a crypic group of sibling species, with no single locus offering unambiguous resolution of species.

To identify species we looked beyond the conventional set of PCR based markers and applied a wider set of ancestry informative markers (AIMs).

Species were not assigned to samples from laboratory colony crosses due to inbreeding and high levels of genetic drift.

To distinguish _A. arabiensis_ from _A. gambiae s.l_ a set of novel markers was derived from data from the 16 genomes project (ref).

Using cut offs based on agreement with the established PCR marker, 368 individuals were classed as _A. arabiensis_ and 2415 as _A. gambiae s.l_. 

A single individual collected in Tororo, Uganda is classed as intermediate- given the majority (XX%) of AIM SNPs in the genome are heterozygous between the gambiae-like and arabiensis-like alleles, this individual is likely to be an F1 hybrid.

To resolve the _A. gambiae s.l_ individuals as _A. gambiae_ and _A. coluzzii_ we applied 729 AIMs previously identified by Neafsey et al (ref), and used in previous analyses of Ag1000G data. (ref paper2, paper1).

Of the 2415  _A. gambiae s.l_ individuals, 1571 were called as _A. gambiae s.s_, 675 as _A. coluzzii_ and 169 as intermediate (ref collection map). 

Many intermediate samples were sampled from the Western coast of West Africa (particularly The Gambia and Guinea Bissau), and given distinct populations of _A. gambiae s.l._ and _A. coluzzii_ are also found in this region, this result highlights the complexity of species relationships here.

Additionally a number of intermediate samples were identified in coastal populations of East Africa, in Kilifi Kenya, and Muleba Tanzania.

%% TODO This analysis
It is established that species barriers between members of the gambiae complex are porous, and numerous instances of introgression associated with selection have been observed in West Africa. (ref clarkson + li, others?).  

We observe known introgression from gambiae to coluzzii of the kdr allele in West Africa.

In West African coluzzii populations, presence of gambiae-like alleles at this locus reach 95%.

However no introgression is obseved in Angola, or CAR.

%% TODO
What about other loci

%% TODO Method to id these regions. Simply just plot frequency of gambiae allele in coluzzii samples?
No clear introgression is observed between gambiae and arabiensis. 

%% TODO ADD AIM FIGURES

### SNP filtering and quality

Site filtering is necessary to ensure that reported variation is of high quality.

Features of specific regions of the Anopheles genome contribute to calling errors in short-read technologies; such features include regions of high divergence from the reference, high homology between regions, copy number variation, or the presence of transposable elements.

Where previously we have used manually curated cutoffs based on observed mendelian error rates to filter sites (ref phase1, phase2), here we built a statistical model where cohort level summary statistics were used to identify sites likely to contain genotyping errors.

Using the 15 available Anopheles pedigrees previously described, we used the presence of mendelian error at sites as a proxy for genotype discordance.

10 of the 15 crosses were used to train the model while 5 were held out for validation.

Each of the 5 pedigrees represent independent evaluation sets.

Before applying the site filters, the false discovery rate (FDR) of the 5 crosses over all autosomal sites ranged between 0.74% and 1.10% (table XXX).

The application of the site filters defines the accessible fraction of the autosomes at 72.58%, and the range of false discovery rates is 0.04% to 0.10%.

The median fold change of FDR was -3.71.


On the hemizygous X chromosome we used the more direct measure of heterozygote calls in males to ascertain mendelian error.

In the dataset are 220 _A. gambiae s.l_ male samples, each of which represent an independent proxy for genotype discordance.

Pre-application of the site filters, subject to a Genotype Quality (GQ) threshold of 30, the median heterozygosity rate was 0.244%, and post filtering this drops to 0.023% (table XX).

The median fold change in error rate was -3.33, with 69.97% of the X chromosome passing site filters.

The new model based method represents a marked improvement over the site filters generated as part of phase 2; all 5 evaluation pedigrees showed a modest reduction in FDR, but the higher rate of accessibility in this release (72.58% vs 62.05%) resulted in an significant improvement in Youden score (Table XXX) across autosomes.

The X chromosome showed a similar pattern, the median heterozygosity rate in phase 2 is similar to the new site filters (0.028%), but the higher accessibility in the updated filter set (69.97%  vs 62.46%) yields improved sensitivity.

As genomic features vary between species, different sets of site filters were generated to allow high quality analyses both within and between species. 

The `gamb_colu` site filters were generated as above, and are appropriate for analyses that include _gambiae_ and _coluzzii_ samples only.

%% TODO Add accessibility of other site filters.
The `arab` site filters were generated following application of the model to the summary statistics from arabiensis samples in the cohort (n=XXX), this set of site filters are appropriate when working with _A. arabiensis_ samples only.

Finally, the `gamb_colu_arab` site filters allow analyses across all three species and are the intersection of the `gamb_colu` and the `arab` site filters.

Place holders for tables.

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

Accessibility of the `arab` site filters closely follows that of `gamb_colu`, with the exception of the X chromosome where we see substantially lower values.

This appears to be driven by high divergence between AgamP4 and our _A. arabiensis_ samples, particularly around the Xag inversion at Q-Q Mbp, ref figure.

On the autosomes the divergence from the reference is comparable between _A.arabiensis_ and _A. gambiae_/ _A. coluzzii_ samples, suggesting a strong basis for comparison accross species.

The median divergence (Dxy) of 100kbp windows is XXX (5%/95% TTT/SSS) for gambiae/coluzzii and YYY (TTT/YYY) for arabiensis.  

On the X chromosome these values are XXX ( / ) for gambiae/coluzzii and YYY (  / ) for arabiensis.
 
### SNP discovery

Overall, we report XX,XXX,SSS single nucleotide polymophisms (SNPs) segregating in this cohort that pass filters, of which XX,XXX (%) are multiallelic.

12,223 SNPs are segregating in both species groups, while XXX are private to gambiae_/coluzzii_ and YYY to arabiensis [fig ref].

This phase of the study reports an additional XXX SNPs from phase 2.

In XXX gambiae and coluzzii individuals we report 12,222,222 SNPs (Q% multiallelic), corresponding to a SNP every 1.6 accessible bases.

In XXX arabiensis individuals we identify 10,000,000 SNPs (Q% multiallelic), a SNP every 2.5 accessible bases.

## Population Structure

### Genome wide patterns

%% TODO NOtes currently.

Re-introduce key idea of structure being different across the genome. 

How does arabiensis fit into this? Are there regions of the genome where arabiensis ancestry is secondary?


### PCA / UMAP

To highlight population structure we performed principal component analysis across all wild-caught samples in the dataset.

To avoid confounding of structure in genomic regions including paracentric inversions, extremely low diversity and regions under strong selection, we limited our analysis to euchromatic regions of chromosome 3L. 

The most apparent signal in the dataset is PC1 clearly being driven by Arabiensis, with clear separation of arabiensis samples from gambiae/coluzzii. 

The apparent hybrid sits between gambiae and arabiensis samples.

To view population structure within gambiae/coluzzii and arabiensis more independently, we performed subsequent PCA analysis Arabiensis and gambiae/coluzzii individuals separately. 

Population structure between gambiae and coluzzii is significantly more complex. 



Separately between species. What are the major findings?

- Arabiensis drives PC1. 

- East Africa: Seems to be clear population structure between _gambiae_ in KE and TZ.

- According to AIM analysis, a significant proportion of samples in these groups are classed as IM between gambiae. Certainly not coluzzii, but some kind of complex ancestry. 

- Relevance to TENEGLRA

- West Africa- in far west Africa we see intermediate population. Not gambiae coluzzii, unlikely to be hybrids, but a related subspecies. 

Interestingly seems to be stable in the presence of both gamb and colu. Although they sit close to col in the PCA they are distinct from coluzzii, given they are founf at the same site.

### Genetic Diversity within sampling sites

Better to avoid use of population.

Using species groupings above, i.e. PCA clusters of samples not clearly gambcolu, but sympatric with them are classed as intermediate. 

First look at diversity at a regional level within species. ie gambiae is more diverse in west than east africa. Central?

Coluzzii is similar within its range. 

Arabiensis only found in EA, but do we see differences in diversity?

Justification of using wattersons theta.

THEN, we can start to speak about differences between species, within regions. 

West African gambiae have higher diversity than coluzzii. 

Then how do west african intermediate compare to these?

In east africa, we compare gambiae to arabiensis. 


## Insecticide Resistance

- kdr frequencies in different sampling groups
- we don't have CNVs... so? We can use markers?

## Gene Drive

- repeat of phase 2 analysis.






# Methods  {.page_break_before}

## Population Sampling

Mosquitoes, from natural populations, were collected at 124 sites (unique latitude/longitudes) in 19 sub-Saharan African countries (Figure 1; Supplemental Table @@??). 

95 of these sites are novel to Ag1000G phase 3, including 19 sites in six newly sampled countries, the remainder were previously sampled in phases 1 and 2 of the project (@doi.org/10.1038/nature24995; @@phase 2 doi when published).

New samples present in phase 3 comprised the following:

**Burkina Faso**

Two new submissions of collections from Burkina Faso are included here. The first added collections made in three villages separated by at most 30km: Bana (11.233, -4.472), Souroukoudinga (11.235, -4.535) and Pala (11.150, -4.235).

These collections were made in July and October 2014, and January, February and April 2015. The area is agricultural, with rice-growing areas near Bana and Souroukoudinga, and a large mango grove near Pala.

Female mosquitoes were collected by human landing catch, pyrethrum spray collection or aspiration; males were collected by swarm netting. Both _An. gambiae_ and _An. coluzzii_ (@doi:10.1186/1475-2875-5-125) were collected. 

Specimens were stored in 80% ethanol and DNA was extracted using the DNeasy Tissue Kit (Qiagen).

The second new submission from Burkina Faso added collections of indoor resting adults made by spray catch from Monomtenga in central Burkina Faso (12.06, -1.17). 

These specimens were sorted morphologically to _An. gambiae_ s.l.

Ovaries of half-gravid females were dissected and placed in numbered individual micro-tubes containing modified Carnoy's solution (1:3 glacial acetic acid: 100% ethanol).

Carcasses were placed in correspondingly numbered micro-tubes over desiccant. Genomic DNA was isolated from individual mosquitoes using one of the following: DNeasy Extraction Kit (Qiagen, Valencia, CA), Puregene kit (Gentra Systems, Inc., Minneapolis, MN), DNAzol kit (Molecular Research Center, Inc., Cincinnati, OH.) or Easy-DNA kit (Invitrogen, Carlsbad, CA).

_An. gambiae_ s.s. and its molecular forms were identified using one of two rDNA-based PCR/RFLP assays (@doi:10.1046/j.1365-2915.2002.00393.x;  @doi:10.4269/ajtmh.2004.70.604).

Ovaries from specimens of the desired species were subject to polytene chromosome analysis.

**Democratic Rebublic of the Congo**

Samples were collected from Gbadolite (4.283, 21.017), a town located in the far north of the Democratic Republic of Congo (DRC) near the border with the Central African Republic, surrounded by forest.

In common with much of DRC, malaria transmission rates are high, and the samples are _An. gambiae_ s.s., which is the dominant vector.

Samples were collected as larvae from temporary pools within and around the town by dipping in early August 2015. All larvae were reared to adults and females preserved over silica for DNA extraction using Qiagen DNAEasy kits.

**Central African Republic**

Collections were carried out in Bangui (4.367, 18.583), during December 1993, by indoor resting aspiration or pyrethrum spray catch.

**Cameroon**

Two new submissions of samples from Cameroon are included in this phase. 

In the first submission anopheline mosquitoes were taken from 64 locations covering a 1,500 km north-to-south transect that crossed all eco-geographical areas of Cameroon (@doi:10.1186/1472-6785-9-17). 

Mosquito collection involved spraying aerosols of pyrethroid insecticides inside human dwellings, dead mosquitoes were retrieved from white sheets that  were laid on the floor.

Anopheline mosquitoes were identified using morphological identification keys (>>Gillies and De Meillon 1968<<@@how reference books with no ISBN?; @isbn:0620103213).

Ovaries from half-gravid _An. gambiae_ s.l. females were dissected and stored in Carnoy's fixative solution (absolute ethanol:glacial acetic acid 3:1) for cytogenetic analyses.

Carcasses were stored individually in tubes containing a desiccant and kept at -20°C until they were molecularly processed. All half-gravid specimens collected in each village were identified to species and molecular forms using PCR-RFLP (@doi:10.1046/j.1365-2915.2002.00393.x).

The second Cameroonian submission came from pyrethrum spray collections, larval sampling and human landing catches conducted in twenty locations during October 2013.

These villages are scattered throughout the country and reflect a gradient of human-dominated environments, for example, forest (Manda: 5.726, 10.868 and Campo: 2.367, 9.817); forest/savanna transition (Tibati: 6.469, 12.629); savanna (Lagdo: 9.049, 13.656); suburban area (Nkolondom: 3.972, 11.516) and 
urban areas (Douala: 4.055, 9.721 and Yaoundé: 3.880, 11.506).

Contributed specimens were _An. gambiae_ and _An. coluzzii_ (@doi:10.1046/j.1365-2915.2002.00393.x).

Population genomics studies indicated the presence of relatively differentiated subgroups within both species as well as clusters thriving in polluted breeding sites in large cities (@doi:10.1093/molbev/msx0877).

Specimens were stored on silica gel, and DNA was extracted using a Zymo research kit for adults and a Qiagen kit for larvae.

**Mayotte**

Phase 3 adds collections from three novel sites on the island of Mayotte. 

Samples were collected as larvae during March-April 2011 in temporary pools by dipping in  Tsounzou (-12.797, 45.185), Tsinkoura (-12.936, 45.138) and aerogare (-12.803, 45.283).

Larvae were stored in 80% ethanol prior to DNA extraction.

All specimens contributed were _An. gambiae_ (@doi:10.4269/ajtmh.2004.70.604) with the standard 2L<sup>+a</sup>/2L<sup>+a</sup> or inverted 2L<sup>a</sup>/2L<sup>a</sup> karyotype as determined by the molecular PCR diagnostics (@doi:10.4269/ajtmh.2007.76.334).

The samples were identified as males or females by the sequencing read coverage of the X chromosome using LookSeq (@doi:10.1101/gr.093443.109).

**Gabon** @@was this submission "GA-B" included in the release?? I can't see it in the meta data, delete?

_Anopheles_ sampling was carried out in three new locations in Gabon @@year?.

Adult _An. gambiae_ females were collected in Benguia (-1.633, 13.492) by human landing catches (National Research Ethics Committee of Gabon n°. 0031/2014/SG/CNE) in September 2015.

Benguia is a forest-savanna village with less than 300 inhabitants. Malaria is endemic across the year.

The specimens were stored immediately at -80°C.

_An. coluzzii_ larvae were sampled in Libreville (0.390, 9.454) and Cocobeach (0.992, 9.576) by dipping in natural breeding sites in January 2016.

Libreville is the capital of the country and it is urban and polluted site, Cocobeach is a coastal village north of Libreville.

Across both malaria is endemic across the year.

The specimens were stored in alcohol at -20°C.

Total genomic DNA was extracted for all the mosquitoes using the CTAB protocol (@doi:10.4269/ajtmh.2005.73.1077).

**The Gambia**

Two new submissions of samples from The Gambia are present in phase 3.

The first were collected along the Gambia River from the western coastal region of The Gambia, (Low River Area; Caputo et al. 2008), in August 2006. 

_An. gambiae_ and _An. coluzzii_ specimens were identified to species following the PCR-RFLP protocol (@doi:10.1046/j.1365-2915.2002.00393.x) using DNA extracted from the mosquito leg.

Only _An. coluzzii_ specimens were collected from villages of Tankular (13.417, -16.033) and Kalataba (13.550, -15.617). 

_An. gambiae_ and _An. coluzzii_ specimens were found in sympatry and collected from villages of Yallal Tankonjala (13.550, -15.700), Sare Samba Sowe (13.583, -15.900) and Hamdalai (13.567, -16.0167).

PCR-RFLP protocol also revealed the presence of mosquitoes with hybrid _An. gambiae_/_An. coluzzii_ genotype in Yallal Tankonjala and Sare Samba Sowe.

Collections of indoor daytime-resting half gravid mosquitoes were carried out mainly in human dwellings and, in few cases, in animal shelters.

Collections were carried out by pyrethroid and/or paper-cup mouth aspirators from 12 AM to sunset, and kept in vials with desiccant.

Ovaries were dissected, maintained into Carnoy fixative (three parts pure ethanol:one part glacial acetic acid) and stored at -20<sup>o</sup>C before polytene chromosome preparations (@doi:10.1186/1475-2875-7-182).

Chromosome scoring was carried out under a phase‐contrast optical microscope. 

Paracentric inversion karyotypes were scored according to the nomenclature and conventions of Coluzzi et al. (@doi:10.1016/0035-9203(79)90036-1) and Touré et al. (@pubmed:10645562).

The second new submission consists of adult mosquitoes collected at Wali Kunda in the rural, central river region of The Gambia (13.567, -14.917).

The area is 180 km from the sea, on the south bank of the River Gambia, in flat Sudan savannah with a small fishing village (and a research field station) as well as rice fields and swamplands.

The dominant _Anopheles_ vector species is _An. coluzzii_ (@doi:10.1186/s12936-016-1203-z).

Mosquitoes were captured using human landing collections both inside and outside huts for 19 days in October and November 2012. Mosquitoes were stored in RNAlater or dried over silica gel and stored at -20<sup>o</sup>C.

**Guinea and Mali**

A novel sample submission to phase 3 included collections from both Guinea and Mali.

Mosquitoes were collected from four different study sites at the border with Mali and in Guinea Conakry. Takan (11.47, -8.33) and Toumani Oulena (10.83, -7.81) are both small villages in the Yanfolila district of southern Mali and represent the Sudanian savannah ecological zone.

Takan is arid savannah, while Toumani Oulena is humid savannah.

In Guinea Conakry, we sampled in Koraboh, (9.28, -10.03) a small village in the Kissidougou district in the Faranah region representing a semi-forest site with intermediate ecology, a mix of savannah and forest, and in Koundara, (8.48, -9.53), a small village in the Macenta district in the Nzerekore region representing deep forest ecology. 

All reported collections occurred in October and November in 2012.

At each site, mosquitoes were collected using three different methods: human-landing capture, indoor manual aspirator or pyrethroid spray catch, and larval capture - where the first and second instar larvae were raised to adult in a field insectary under standard insectary conditions prior to DNA isolation from the adults, and the third and fourth instar larvae were preserved directly for DNA isolation, without rearing in the insectary.

The two distinct methods of larval collection were used to control for possible genetic bias inherent in lab rearing of captured larvae.

Across sites, all types of larval sites were sampled, including both temporary and permanent sites.

Human-landing captures were performed both inside dwellings and outside (>10 m from dwelling) at night between 18:00 and 06:30.

The indoor aspirator or spray catches were done in the morning between 06:00 and 12:00.

Adult specimens or third and fourth instar larvae were preserved immediately in 80% ethanol until later DNA extraction.

First and second instar larvae were raised to adults in nearby field insectaries and upon emergence were preserved in 80% ethanol.

DNA was extracted from mosquitoes using DNAzol by the provided protocol (Invitrogen, CA, USA).

Further details on sampling and basic Southern Mali/Guinea vector biology are presented in Coulibaly et al. (doi:10.1186/s12936-016-1242-5).

**Guinea Bissau**

Two new Guinea Bissau collection sites are added here, both performed in October 2010 by indoor CDC light traps.

Samples were also collected from Ga-Mbana (12.052, -14.902) and Leibala (12.272, -14.222).

Ga-Mbana is a rural village located along a main road in central Guinea Bissau, while Leibala is a neighbourhood of the eastern town of Gabu.

The samples of Ga-Mbana comprised _An. coluzzii_ whereas the samples of Leibala comprised _An. gambiae_, all being identified by IGS and SINEX markers as described in Vicente et al. (@doi:10.1038/srep46451).

The _kdr_ pyrethroid target site resistance mutation L1014F occurs at high frequency in Leibala but at very low frequency in Ga-Mbana (@doi:10.1038/srep46451).

Malaria is meso-hyperendemic (@doi:10.4269/ajtmh.2003.68.2.0680161) and sporozoite rates are below 1% in the region.

Specimens were stored on silica gel and DNA extraction was performed by a phenol-chloroform protocol described in Donnelly et al. (@doi:10.1038/sj.hdy.6885930).

**Kenya**

New Kenyan specimens were obtained from villages located in Kilifi County near the Kenyan coast between 2000 and 2014.

All Anopheles mosquito sampling was conducted indoors using CDC light traps.

_An. gambiae_, _An. funestus_, _An. arabiensis_ and _An. merus_ were present at sampling locations (@doi:10.4269/ajtmh.1993.49.520).

Sporozoite rates for the area during previous studies were 1.47% (@doi:10.1038/ncomms1672).

**Mali**

Two further submissions containing collections from 11 sites in Mali are new for phase 3.

In the first, collections were made in four villages in the Koulikoro region; Tieneguebougou (12.810, -8.080) approximately 20 km north of Bamako, 
and Kababougou (12.890, -8.150), Ouassorola (12.900, -8.160), Sogolombougou ( 12.880, -8.140), approximately 30 km north of Bamako.

The collections were made in August 2014 by human landing catch and pyrethrum spray catch.

Both _An. gambiae_ and _An. coluzzii_ (@doi:10.1046/j.1365-2915.2002.00393.x) were collected.

Specimens were stored in 80% ethanol.

In the second submission, collections of indoor resting adults were made by spray catch from seven villages in the southern part of Mali in August-September 2004: Banambani (12.800, -8.050), Bancoumana (12.200, -8.200), Douna (13.210, -5.900), Fanzana (13.200, -6.130), Kela (11.880, -8.450), Moribobougou (12.690, -7.870) and N'Gabakoro (12.680, -7.840).

Specimens were sorted morphologically to _An. gambiae_ s.l. 

Ovaries of half-gravid females were dissected and placed in numbered individual micro-tubes containing modified Carnoy's solution (1:3 glacial acetic acid: 100% ethanol).

Carcasses were placed in correspondingly numbered micro-tubes over desiccant.

Genomic DNA was isolated from individual mosquitoes using one of the following: DNeasy Extraction Kit (Qiagen, Valencia, CA), Puregene kit (Gentra Systems, Inc., Minneapolis, MN), DNAzol kit (Molecular Research Center, Inc., Cincinnati, OH.) or Easy-DNA kit (Invitrogen, Carlsbad, CA).

_An. gambiae_ s.s. and its molecular forms were identified using one of two rDNA-based PCR/RFLP assays (@doi:10.1046/j.1365-2915.2002.00393.x; @doi:10.4269/ajtmh.2004.70.604).

Ovaries from specimens of the desired species were subject to polytene chromosome analysis.

**Malawi**

Specimens were obtained from villages within the catchment of the Majete Malaria Project, Chikhwawa District, Malawi (-15.933, 34.755) (@doi:10.1186/s12879-017-2749-2).

Mosquitoes were collected indoors and outdoors by Suna light trap in May 2015.

Chickhwawa District is an area with perennial and intense malaria transmission (@doi:10.4269/ajtmh.13-0028).

All specimens were _An. arabiensis_ (@doi:10.1046/j.1365-2915.2002.00393.x).

Additional details of vector population bionomics may be found in (@doi:10.1186/s12879-017-2749-2; @doi:10.1186/1475-2875-11-380).

Specimens were stored over silica and DNA was extracted using the Qiagen plate protocol.

**Mozambique**

Mosquito samples were collected in Furvela (-23.716, 35.299), Mozambique, by CDC light traps between December 2003 and April 2004.

Specimens were stored on silica gel and DNA was extracted according to Collins et al. (@doi:10.4269/ajtmh.1987.37.37).

Contributed specimens consisted of _An. gambiae_ individuals identified according to Fanello et al. (@doi:10.1046/j.1365-2915.2002.00393.x).

Furvela is a rural village located in Inhambane Province, where malaria is transmitted mainly by _An. gambiae_ and _An. funestus_ (@doi:10.1111/mve.12084).

_An. arabiensis_ and _An. merus_ are also found at low frequency.

Sporozoite rates around 4% have been reported in *An. gambiae* from Furvela (@doi:10.1111/mve.12084).

**Tanzania**

Tanzanian samples were collected from four distinct locations.

Moshi samples came from lower Mabogini (-3.400, 37.350), rice fields near lower Moshi on the southern slope of Mount Kilimanjaro, a region shown to have increasing resistance to pyrethroids (@doi:10.1186/1756-3305-7-274).

Mosquitoes were collected as larvae, during the rice growing season in August-September 2012, raised to adults and females bioassayed in WHO tubes for one hour with 0.05% lambda cyhalothrin (@isbn:9789241511575).

Alive and dead mosquitoes were preserved over silica.

In Tanzanian samples screened in Kabula et al. (@doi:10.1111/j.1365-3156.2012.02986.x), Moshi was the most pyrethroid resistant population, they were found to be completely DDT susceptible, only in one out of 642 mosquitoes assayed by Matowo et al. (@doi:10.1186/1756-3305-7-274) was found to carry a _kdr_ resistance mutation (Vgsc-995F).

Tarime collections took place in the village of Komaswa (-1.417, 34.183) about 410 km north west of Moshi, during August 2012.

Mosquito larvae were collected, raised to adults and females bioassayed with a range of insecticides in WHO tubes for one hour (@isbn:9789241511575), 
finding almost complete multi-insecticide susceptibility: permethrin (100% mortality), lambda cyhalothrin (97%), fenitrothion (100%), DDT (100%) and bendiocarb (100%) (Nyka, T. unpublished data – Insecticide Resistance Monitoring Report 2012. NIMR Tanzania).

Mulheza samples were collected from Zeneti village (-5.217, 38.650), northeast Tanzania.

Malaria is intense and perennial with transmission peaking after the rainy season in May and June (@doi:10.1111/j.1365-3156.2012.02986.x).
Mosquitoes were sampled between November 2012 and May 2013.

Indoor resting collections were used to obtain live females for deltamethrin susceptibility testing and pyrethrum spray catches were used for mosquitoes that were collected for blood meal analysis.

Collections were conducted between 06:00 and 09:00 from randomly selected houses.

Live mosquitoes collected for susceptibility testing were provided with 10% glucose solution and transported to the field insectary.

Mosquitoes were sorted and morphologically identified to species, carcasses were stored individually over desiccant for laboratory processing.
Muleba (1.750, 31.667), the final collection region, is in the North-western part of Tanzania.

The district is known to be a malaria epidemic prone area with unstable transmission of varying seasonality.

The highest peak of malaria transmission is usually reached between May-July and November-January, which results from proceeding rain seasons.

There have been malaria vector control efforts since 2007 when indoor residual spraying using Lambdacyhalothrin was introduced.

Insecticide resistance in this district is coupled with high frequency of _kdr_ pyrethroid target site mutations in the _An. gambiae_ s.s population (@doi:10.1111/j.1365-3156.2012.02986.x; @doi:10.1186/1475-2875-12-149).

Sampling was conducted over six months, which include both dry and rainy season and covers 6 villages selected to represent all major ecological systems in the district. 

**Uganda**

In Uganda, a single new site is sampled in phase 3.

In Kihihi subcounty, Kanungu District (-0.751, 29.701), resting mosquitoes were collected during October and November 2012.

Kihihi is located in an  upland area with seasonal malaria transmission (@doi:10.1186/1475-2875-13-111).

All specimens were _An. gambiae_ (@doi:10.1046/j.1365-2915.2002.00393.x).

Additional details of vector population bionomics may be found in (@doi:10.1186/1475-2875-13-1114).

Specimens were stored in 80% ethanol and DNA was extracted using the Qiagen plate protocol.

Details of natural population samples previously described in phases 1 and 2 can be found in the Supplementary Information of The Anopheles gambiae 1000 Genomes Consortium (@doi.org/10.1038/nature24995; @@phase 2 doi when published - respectively).

**Colony Crosses**

15 crosses were contributed to Ag1000G phase 3.

The crosses were generated using parents from eight different colonies: G3(MRA-112); Kisumu(MRA-762); Pimperena (canonical representative of _An. gambiae_ species; MRA-861); Ghana (recent colony of _An. coluzzii_ from Okyereko, southern Ghana (@doi:10.1371/journal.pgen.1004236)); Mali-NIH (canonical representative of _An. coluzzii_ species; Niono, MRA-860); (P)Akron (Benin, MRA-913); Nagongera (Tororo, Uganda); and Tiassalé (southern Cote d’Ivoire (@doi:10.1371/journal.pgen.1004236)).

The labels, e.g. “29-2”, are identifiers used for each of the crosses within the project and have no special meaning.

Full full details of cross production, sequencing and quality control is described in the Supplementary Information of The Anopheles gambiae 1000 Genomes Consortium (@doi.org/10.1038/nature24995).

The only difference between the production of the four crosses that are novel to phase 3: B4, K2, K4 and K6, and those from earlier phases of the project, is that multiple males and multiple females were placed together for mating, then all male and all egg laying female mosquitoes were sequenced.

This necessitated matching up potential fathers of crosses with the correct mother and offspring.

For each cross for which the father was in doubt, the list of potential parental pairs was computed. 

For each of these pairs, for each chromosome, the Mendelian error was computed for every sample of the progeny and the median value (along samples) was plotted for every computation. 

If one pair yielded median Mendelian errors significantly lower for every chromosome than any other pair (except X which was consistent no matter the parents), that pair was chosen as the parsimonious parents. 

In four crosses (B4, K2, K4 and K6) parental pairs could be clearly identified and these crosses could, therefore, be included in the phase 3 data release.

Two of the novel crosses, K4 and K6, were found to be fathered by the same male, AC0398.


## Whole Genome Sequencing and Alignment

4,693 individual mosquitoes were sequenced using the Illumina HiSeq2000 (n=3,130) and the Illumina HiSeqX (n=1,563) to a target coverage of 30X.

Reads were aligned to the AgamP4 reference genome using `bwa` version `0.7.15`.

Indel realignment was performed using GATK `v3.7-0` RealignerTargetCreator and IndelRealigner. 

Single nucleotide polymophisms were called against AgamP4 using GATK UnifiedGenotyper `v3.7-0`.

Sample genotypes were called independently, in genotyping mode, given all possible alleles at each site, allowing parallelisation over samples.

Coverage considered at individual sites was capped at 250X by random downsampling.

Full details of pipelines including all parameter settings are available in supplementary information.

Following successfull completion of the pipeline samples entered the sample quality control (QC) process.

# Sample QC

The sample QC process was composed of three distinct stages: sequence quality assurance, replicate handling, and anomaly detection.

To meet the requirements of sequence quality assurance median coverage had to be at least 10X, and minumum 50% of the genome covered by at least 1X.

We also implemented the test for contamination in NGS alignments described in Jun et al (https://doi.org/10.1016/j.ajhg.2012.09.004). 

Briefly the method estimates the likelihood of the observed alternate and reference allele counts under different contamination fractions given population allele frequencies.

Population allele frequencies were estimated from the Ag1000G phase 2 data.

The model computes a maximum likelihood value for a parameter representing percentage contamination (alpha).

Where this parameter was 4.5% or greater the sample was excluded.

We also made sex calls based on the modal coverage ratio X:3R.

3R was selected as representative of autosomal coverage as it is free from inversions and large regions of heterochromatin.

The modal coverage was used owing to concerns around the high skewdness of coverage distributions. 

To mitigate this further, when computing the modal coverage we only considered sites where coverage was at least 2X.

The sample was classed as male where the coverage ratio was between 0.4-0.6, and female between 0.8-1.2.

Where the ratio was outside these limits, the sex call was not made and the sample dropped.

One of the submission sets from The Gambia, was composed entirely of Whole Genome Amplified (WGA) samples. 

These received a sex call where possible but the decision was made not to exclude based on ratio, due to the inherent value of this submission.

The fact this set is entirely WGA was considered throughout the analysis of these samples.

The sample QC process also included assessment of technical replicates.

We computed pairwise genetic distance between all sample pairs within a submission set.

The metric used was Hamming between alleles, so a genotype of 0/1 records a value of 1 against the genotype 1/2, allowing straightforward handling of multiallelic SNPs.

Only sites where both samples had a genotype call were included, mean distance was calculated over a denominator of the number of assessed sites multiplied by 2 for diploidy.

Computations were initially carried out on a downsampled set of 10 x 100,000 contiguous sites genome wide to be computationally feasible.

This use of chunks was convenient to leverage the underlying storage of data in `zarr` format.

Where a pair of samples fell beneath a conservative threshold of 0.012, the true genetic distance (i.e. without downsampling)  was computed across all sites.

For each pair of technical replicates, we excluded both members of the pair where genetic distance was above 0.006.

Where replicate pairs met the concordance threshold we excluded the lower quality sample.

Quality was determined based on the skewdness of mean to median, i.e. $1 - |mean_{cov}/median_{cov}|$. 

The sample with the lower value was preferred as it suggests a more normal coverage distribution.

To identify unknown replicate pairs as a result of sample mix ups or mislabelling, we screened within submission sets for unexpected pairs, using the genetic distance cut off of 0.006 as above.

We did not attempt to identify unknown replicate pairs in the AG1000G-X submission set, made up of laboratory experimental crosses, due to familial similarity and high levels of inbreeding.

The third stage used principal component analysis (PCA) to identify and exclude individual samples that were outliers based on available metadata.

A review process identified samples that could not be explained parsimoniously, and were therefore likely to be sample mix ups or instances of mislabelling.

Using the PCA implementation in `scikit-allel v2.1.0` we downsampled to 100,000 segregating non-singleton sites from chromosomes 3R and 3L, to avoid regions complicated by known introgression loci or paracentric inversions.

Multiallelic sites were included as dummy rows by melting the data structure. 

A careful review process identified: a) samples that dominated single principal components, either individually or in very small numbers. 

This suggests an individual belonging to another Anopheline species, or some inherent problem with the sample.

Or b) samples that clustered with other samples inconsistently with metadata.

This was a subjective assessment, but bore in mind the given collection location, time, and PCR species assignment (where available) of the sample. 

Multiple geographical sites submitted by the same partner were also considered, where sample mix ups formed the most parsimonious explanations of incongruent clustering.

### Species assignment and sex calling

Ancestry informative markers were used to assign species in our cohort.

To derive markers informative between _A. arabiensis_ and _A. gambiae s.l._, we used publicly available data from the 16 genomes project (ref). 

Whole genome SNP calls called against the AgamP3 reference for 12 _A. arabiensis_ and 38 _A. gambiae s.l_ individuals were available.

Alleles were mapped onto the same alternate allele space, the frequencies of which were computed across both groups.

Sites that were multiallelic in either group were excluded, as well as sites where any genotypes were missing. 

565,329 SNPs were identified as potentially informative where no shared alleles were present between groups.

These were spread throughout the genome, but were concentrated on the X chromosome (63.2%), particularly around the Xag inversion.

The full AIM set of positions and alleles are available as part of the phase 3 data release.

Called genotypes for each individual in the dataset were cross referenced against a random subset of 50,000 ancestry informative marker alleles, genotype alleles were accordingly classified as gambiae-like or arabiensis-like.

AIM fractions were cross referenced against PCR results available from a subset of inviduals.

Given the relatively small number of _A. arabiensis_ samples in the 16 genomes project- it was clear that a significant proportion of putative AIMs were not likely to be truly informative.

Therefore, classification requirements are less rigourous than other sets of validated markers; individuals were classed as _A. arabiensis_ where a fraction >0.6 of alleles were arabiensis-like (n=368), and as _A. gambiae s.l_ where this value was < 0.03 (n=2415).

Species were not assigned to samples from the AG1000G-X submission due to inbreeding and high levels of genetic drift.

A single individual collected in Tororo, Uganda is classed as intermediate- given the majority (XX%) of sites in the genome are heterozygous between the gambiae and arabiensis allele, this individual is likely to be an F1 hybrid.

To resove the _A. gambiae s.l_ individuals into _A. gambiae_ and _A. coluzzii_ we applied the 729 AIMs previously identified by Neafsey et al (ref).

?? Need to find code that creates gambiae from neafsey set

Cutoffs were made at <0.12 (gambiae) and >0.9 (coluzzii), with individuals between classed as intermediate. 

Of the 2415  _s.l_ individuals, 1571 were called as gambiae, 675 as coluzzii and 169 as intermediate (ref collection map). 

### SNP filtering and quality

Site filtering ensures that reported variation is of high quality.

As genomic features vary between species, different sets of site filters were generated to allow high quality analyses both within and between species. 

The `gamb_colu` site filters were generated using a decision tree model, and are appropriate for analyses that include _gambiae_ and _coluzzii_ samples only.

Inputs to the decision tree model are summary statistics from the set of SNP calls and genotype alignments.

The `arab` site filters were generated following application of the resulting model to the summary statistics from arabiensis samples in the cohort, this set of site filters are appropriate when working with _A. arabiensis_ samples only.

Finally, the `gamb_colu_arab` site filters allow analyses across all three species and are the intersection of the `gamb_colu` and the `arab` site filters.


Using the 15 available Anopheles pedigrees previously described, we used the presence of mendelian error at sites as a proxy for genotype discordance.

Where previously we have used manually curated cutoffs based on observed mendelian error rates to filter sites (ref phase1, phase2), here we built a statistical model where cohort level summary statistics were used to predict the presence or absence of mendelian error, becoming a binary classification problem.

Summary statistics used as input to the model are presented in table (ref). 

Pedigrees included _A. gambiae_ and _A. coluzzii_ mosquitoes only, and summary statistics to build the initial site filters model came from females of these species (n=2415). 

Males were excluded, so that the model could also be applied without modification to the X chromosome.

5 of the 15 crosses were held out for validation, so performance could be evaluated objectively.

Sites were defined as PASS where all genotypes across all 10 remaining crosses were called, and no mendelian inconsistencies were observed.

Sites were defined as FAIL where a mendelian inconsistency was observed in any pedigree.

All other sites were not considered eligible for inclusion in model training.

A balanced training set was generated from the remaining 10 crosses containing XXX autosomal(?) sites.

We applied a decision tree, as it provides decisions with clear explanations, and is similar in concept to the set of hard thresholds commonly used in SNP calling in non-model organisms.

A set of trees with different parameter settings were learned, exploring the depth of trees and the number of samples allowed at a terminal node.

Parameter settings were evaluated on an unbalanced evaluation set, consisting of XXX sites randomly from sampled from the whole genome.

Leaves of the trained models contain different proportions of PASS sites, by increasing the cutoff for these proportions required to label a leaf as PASS, we were able to compute the area under the receiver operating curve (AUROC) for each parameter set.

The best performing parameter set based on AUROC was selected as the final model, the classification cutoff used was optimised based on the Youden statistic.

The resulting model was a decision tree of depth 8, with a maximum of XX (CHECK NUMBERS) terminal nodes, where leaves were assigned to PASS where > 0.533 of training data in that leaf were PASS.

All sites in the genome were then assigned to PASS or FAIL given the model inputs.


The 5 remaining cross pedigrees were used to perform a final evaluation of the approach.

Above definitions of PASS sites were retained, but independently within pedigrees, providing 5 distinct evaluation sets.

To evaluate performance on the hemizygous X chromosome we use the more direct measure of heterozygote calls in males.

In the dataset are 220 _A. gambiae s.l._ male samples, each of which represent an independent proxy for genotype discordance.

Male error rates were estimated from genotype calls with a minimum Genotype Quality (GQ) value of 30.

A non heterozygote call is labelled PASS, and a heterozygote call FAIL.

Error rates were computed for all crosses, over all chromosomes before and after application of site filters.

We report the false positive rate (FPR), (i.e proportion of the genome considered accessible), and the Youden statistic (ratio of sensitivity to specificity).


## References {.page_break_before}

<!-- Explicitly insert bibliography here -->
<div id="refs"></div>
