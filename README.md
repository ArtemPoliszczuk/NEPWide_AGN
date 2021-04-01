
![](img_w.jpeg?raw=true "Optional Title")

## Active Galactic Nuclei catalog from the AKARI NEP Wide field
**Supplement for the publication.**

* **Status**: submitted to A&A
* **Astronomy & Astrophysics**: to be announced
* **arXiv.org**: to be announced


### Table of contents
* [Description of the project](#description-of-the-project)
* [AGN catalog](#agn-catalog)
* [Technologies](#technologies)
* [Training samples](#training-samples)
* [Training results](#training-results)
* [SED fitting](#sed-fitting)

### Description of the project
* **Context**. The North Ecliptic Pole (NEP) field provides a unique set of panchromatic data, well suited for active galactic nuclei (AGN) studies. Selection of AGN candidates is often based on mid-infrared (MIR) measurements. Such method, despite its effectiveness, strongly reduces a catalog volume due to the MIR detection condition. Modern machine learning techniques can solve this problem by finding similar selection criteria using only optical and near-infrared (NIR) data.
* **Aims**. Aims of this work were to create a reliable AGN candidates catalog from the NEP field using a combination of optical  SUBARU/HSC and NIR AKARI/IRC data and, consequently, to develop an efficient alternative for the MIR-based AKARI/IRC selection technique.
* **Methods**. A set of supervised machine learning algorithms was tested in order to perform an efficient AGN selection. Best of the models were formed into a majority voting scheme, which used the most popular classification result to produce the final AGN catalog. Additional analysis of catalog properties was performed in form of the spectral energy distribution (SED) fitting via the CIGALE software.
* **Results**. The obtained catalog of 465 AGN candidates (out of 33 119 objects) is characterized by 73% purity and 64% completeness. This new classification shows consistency with the  MIR-based selection. Moreover, 76% of the obtained catalog can be found only with the new method due to the lack of MIR detection for most of the new AGN candidates. Training data, codes and final catalog are available via the github repository. Final AGN candidates catalog is also available via the CDS service.
* **Conclusions**. New selection methods presented in this paper proves to be a better alternative for the MIR color AGN selection. Machine learning techniques not only show similar effectiveness, but also involve less demanding optical and NIR observations, substantially increasing the volume of available data samples.


### AGN catalog
Final catalog of AGN candidates can be found in **agn_candidates_catalog.csv** file.
Catalog description:
* **RA**, **DEC** - Position of the object (J2000).
* **AKR_ID** - ID of the object in the AKARI database.
* **HSC-ID** - ID of the object in the North Ecliptic Pole SUBARU/HSC catalog (Goto et al. 2017, Oi et al. 2020, Kim et al. 2020).
* **G**,  - object brightness measured in G filter of SUBARU/HSC instrument. Value is presented in the AB magnitude system. Reader can also find measurements of **R**, **I**, **Z**, **Y** filters respectively.
* **GCme** - **G** measurement uncertainty. **Rme**, **Ime**, **Zme**, **Yme** uncertainties correspond the remaining SUBARU/HSC filters. These uncertainties are understimated due to the SUBARU/HSC data reduction pipeline properties.

### Technologies
c

### Training samples
d

### Training results
e

### SED fitting

<img style="float: right;" src="/SED_fitting/SED_fits_for_agn_candidates_catalog/47499_best_model.png" alt="drawing" width="600"/>



