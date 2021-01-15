
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
* **Context**. The North Ecliptic Pole (NEP) field provides a unique set of panchromatic data, well suited for active galactic nuclei (AGN)
studies. Spectroscopic target selection of AGN candidates in the NEP field in the past was based on mid-IR (MIR) measurements
performed by the AKARI satellite. This method, despite its effectiveness, strongly reduces a catalog volume due to the MIR detection
condition. Recently performed SUBARU/HSC observations of the NEP region enable to construct a large optical and near-IR (NIR)
combined NEP catalog. Such a combination reflects properties of data products which will be provided by synergies with upcoming
missions such as Vera C. Rubin Observatory and Euclid. Modern machine learning techniques permit the efficient selection of AGN,
without usage of MIR measurement.
* **Aims**. Aims of this work were to create a reliable AGN candidate catalog from the NEP field based on a combination of optical
SUBARU/HSC and near-IR AKARI/IRC data and, consequently, to create an efficient alternative for the MIR-based selection technique.
* **Methods**. A set of supervised machine learning algorithms was tested in order to perform efficient AGN selection: linear models in the
form of logistic regression classifier, non-linear models in the form of support vector machine classifier and ensemble methods in the
form of random forest, extremely randomized trees and boosted trees classifiers. Each type of a classifier was tested in a non-balanced
and class-balanced setup. Additionally two different instance-weighting schemes were applied: error-based weighting incorporating
measurement uncertainties into the classification process and distance-based weighting focused on the distance from the class center
in feature space. A set of the best classifiers was formed into a voting scheme, which produced the final AGN catalog. In order to
avoid extrapolation during generalization, the unlabeled data set was limited to a training sample shape with the minimum covariance
determinant algorithm. Additional analysis of catalog properties was performed by spectral energy distribution (SED) fitting via the
CIGALE software.
* **Results**. The final catalog of 465 AGN candidates (out of 33 119 objects) characterized by 73% purity and 64% completeness was
created. This new classification shows consistency with previous, MIR-based, selection in terms of purity and completeness. Moreover,
76% of the obtained catalog can be detected only with the new method, due to the lack of MIR detection for most of the new AGN
candidates. Training data, codes and final catalog are available via the github repository. Final AGN candidates catalog is also available
via CDS and Virtual Observatory services.
* **Conclusions**. New selection methods presented in this paper proved to be a better alternative for MIR color AGN selection. Machine
learning techniques not only show similar effectiveness, but involve less demanding optical and NIR observations, substantially
increasing the volume of available data samples.


### AGN catalog
b

### Technologies
c

### Training samples
d

### Training results
e

### SED fitting

<img style="float: right;" src="/SED_fitting/SED_fits_for_agn_candidates_catalog/47499_best_model.png" alt="drawing" width="600"/>



