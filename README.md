
![](img_w.jpeg?raw=true "Optional Title")

## Active Galactic Nuclei catalog from the AKARI NEP Wide field

**Publication supplement**

* **Status**: submitted to Astronomy & Astrophysics
* **arXiv.org**: to be announced


### Table of contents
* [Description of the project](#description-of-the-project)
* [AGN catalog](#agn-catalog)
   * [Catalog description](#catalog-description)
   * [SED fitting results](#sed-fitting-results)
* [Classifier training](#classifier-training)
   * [Technologies](#technologies)
   * [Training samples](#training-samples)
   * [Training results](#training-results)


### Description of the project
* **Context**. The North Ecliptic Pole (NEP) field provides a unique set of panchromatic data, well suited for active galactic nuclei (AGN) studies. Selection of AGN candidates is often based on mid-infrared (MIR) measurements. Such method, despite its effectiveness, strongly reduces a catalog volume due to the MIR detection condition. Modern machine learning techniques can solve this problem by finding similar selection criteria using only optical and near-infrared (NIR) data.
* **Aims**. Aims of this work were to create a reliable AGN candidates catalog from the NEP field using a combination of optical  SUBARU/HSC and NIR AKARI/IRC data and, consequently, to develop an efficient alternative for the MIR-based AKARI/IRC selection technique.
* **Methods**. A set of supervised machine learning algorithms was tested in order to perform an efficient AGN selection. Best of the models were formed into a majority voting scheme, which used the most popular classification result to produce the final AGN catalog. Additional analysis of catalog properties was performed in form of the spectral energy distribution (SED) fitting via the CIGALE software.
* **Results**. The obtained catalog of 465 AGN candidates (out of 33 119 objects) is characterized by 73% purity and 64% completeness. This new classification shows consistency with the  MIR-based selection. Moreover, 76% of the obtained catalog can be found only with the new method due to the lack of MIR detection for most of the new AGN candidates. Training data, codes and final catalog are available via the github repository. Final AGN candidates catalog is also available via the CDS service.
* **Conclusions**. New selection methods presented in this paper proves to be a better alternative for the MIR color AGN selection. Machine learning techniques not only show similar effectiveness, but also involve less demanding optical and NIR observations, substantially increasing the volume of available data samples.


### AGN catalog
Final catalog of AGN candidates can be found in **agn_candidates_catalog.csv** file.

#### Catalog description:
* **RA**, **DEC** - Position of the object (J2000).
* **AKR_ID** - ID of the object in the AKARI database.
* **HSC_ID** - ID of the object in the North Ecliptic Pole SUBARU/HSC catalog (Goto et al. 2017, Oi et al. 2020, Kim et al. 2020).
* **Gm**  - object brightness measured in G filter of SUBARU/HSC instrument. Value is presented in the AB magnitude system. Reader can also find measurements of **Rm**, **Im**, **Zm**, **Ym** filters respectively.
* **Gme** - **Gm** measurement uncertainty. **Rme**, **Ime**, **Zme**, **Yme** uncertainties correspond the remaining SUBARU/HSC filters. These uncertainties are understimated due to the SUBARU/HSC data reduction pipeline properties.
* **N2m**, **N3m**, **N4m** - object brightness measured in the near-IR filters of AKARI/IRC instrument (AB magnitude system). The **me** column contains measurement uncertainy of a corresponding filter (e.g. **N2me** is a measurement error of **N2m**).
* **S7m**, **S9m**, **S11m**, **L15m**, **L18m**, **L24m** - object brightness measured in the mid-IR filters of AKARI/IRC instrument (AB magnitude system). The **me** column contains measurement uncertainy of a corresponding filter.
* **sum_y** - sum of predictions from the voting scheme (see paper for more information).
* **pred_y** - final classifier prediction. **1** - AGN, **0** - not AGN. In the case of final AGN catalog all are equal 1.

#### SED fitting results
The **SED_fitting** directory contains images of the SED template fitting results performed with the [CIGALE](https://cigale.lam.fr/) software for the AGN catalog. **Number in the name of PNG file** correspond to the AKARI ID (**AKR_ID**) of the object. Details about models and parameter values used in this work can be found in the paper.

<img style="float: right;" src="/SED_fitting/47499_best_model.png" alt="drawing" width="400"/>


### Technologies
All the codes were written in Python 3. We used [Numpy](https://numpy.org/) and [Pandas](https://pandas.pydata.org/) for data manipulation and [Matplotlib](https://matplotlib.org/) to visualize the results. The ML part of the project was based on [scikit-learn](https://scikit-learn.org/stable/) and [XGBoost](https://xgboost.ai/) libraries. The spectral energy distribution fitting was donve via [CIGALE](https://cigale.lam.fr/) software.

### Training samples
Are available in **training_samples** directory.
* **training_sample.csv** - objects used for training in the main part of the paper.
* **training_sample_for_2nd_iteration_experiment.csv** - subset of training_sample.csv with mid-IR measurements. It was used for the second iteration experiment (see paper).

#### CSV files description:
* **Fm**, **Fme** - AB magnitude brighteness and its measurement uncertainty for a corresponding "F" filter. Same notation as in the AGN candidates catalog described above.
* **F1-F2** - colors created from "F1" and "F2" filters. In this case **m** was removed from the filter names to increase readability.
* **specz** - spectroscopic redshift.
* **clss** - class of the object based on spectroscopic or X-ray measurements.
* **Y** - label of the object based on spectroscopic or X-ray measurements. **1**-AGN, **0**- not AGN. **WARNING:** do not confuse Y label with Ym brightness. 
* **sum_y** - sum of predictions from the voting scheme obtained via 5-fold cross validation (see paper).
* **y_pred** - final prediction of the voting scheme classifier obtained via 5-fold cross validation (see paper).
* **fuzzy_dist** - instance weights based on the distance from a class center (see paper for more details).
* **fuzzy_err** - instance weights based on measurement uncertainties in a particular class (see paper for more details).


### Training results
The **training_results** directory contains detailed information about training of classifiers. Directory tree is structured as follows:
* **main_training** - contains information from the training of main classifiers used to produce fingal catalog of AGN candidates.
* **second_interation_experiment_training** - results from the second iteration experiment.
    * **clfname_clsbalance** - directory containing training results of the **clfname** classifier (*SVM* for support vector machine, *XGB* for XGBoost, *RF* for random forest, *ET* for extremely randomized trees, *logistic* for logistic regression, *hard_voting* for majority voting scheme, *stacked_classifier* for soft voting scheme based on probabilties obtained via logistic regression) with (*balanced*) or without (*non_balanced*) class weights **clsbalance**.
        * **instance_weight** - if classifier was using instance weights (**fuzzy_err* - instance weights based on measurement uncertainty, **fuzzy_dist** - instance weights based on distance from the class center, **normal** - no instance weights).
            * **best_params** - best model parameters obtained during training.
            * **gs_results** - detailed metric values obtained during grid search.
            * **metrics** - mean values obtained from **gs_results** data.
            * **std** - standard deviation obtained from **gs_results** data.
            * **pr_curve** - precision-recall curve (available if classifier was performing probability estimation).
            * **training_prediction** - prediction performed on the data during 5-fold cross validation.




