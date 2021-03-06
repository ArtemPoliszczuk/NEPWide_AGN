import pandas as pd
import numpy as np
import os

from sklearn.dummy import DummyClassifier
from sklearn import preprocessing
# import sklearn.metrics as skmetrics

import warnings
warnings.filterwarnings("ignore", category=UserWarning)

import training_utils

experiment_name = "dummy"
print(experiment_name)

#----------------- Data: --------------------
train_path = "vis_nir_mir_training.csv"
general_path = "vis_nir_mir_general.csv"

training_data = pd.read_csv(train_path, index_col=0)
general_data = pd.read_csv(general_path, index_col=0)

#----------------- Columns: -----------------
# columns to preserve in the output file:
info_columns = ['HSC-ID', 'AKR_ID','specz', 'clss']

# fuzzy options to test:
fuzzy_options = ["normal"]

# Features:
features = ["S11-L18", "Z-N4", "S9-L18", "S9-L15", "Ym-N4", "I-N4", "S11-L15", "R-L18", "I-L18", "R-N4"]
fuzzy_dist_column = ["fuzzy_dist"]
fuzzy_err_column = ["fuzzy_err"]
output_path = "./results/second_loop"


#------------------------------------ TRAINING: --------------------------------------
train_X = training_data[features].values
general_X = general_data[features].values

for fuzzy_option in fuzzy_options:
    
    print(fuzzy_option)
    
    clf = DummyClassifier(strategy="stratified")
    
    metrics, std = training_utils.evaluate_on_cv(training_data, train_X, clf, 
                                                 fuzzy_option, fuzzy_dist_column, fuzzy_err_column)
    pr_curve = training_utils.predict_and_pr_curve_on_cv(training_data, train_X, clf,
                                                        fuzzy_option, fuzzy_dist_column, fuzzy_err_column)
    
    # fit to the data:
    if fuzzy_option == "normal":
        clf.fit(X=train_X, y=training_data["Y"])
    elif fuzzy_option == "fuzzy_dist":
        clf.fit(X=train_X, y=training_data["Y"],
                   sample_weight=training_data[fuzzy_dist_column].values.T[0])
    elif fuzzy_option == "fuzzy_err":
         clf.fit(X=train_X, y=training_data["Y"],
                    sample_weight=training_data[fuzzy_err_column].values.T[0])
    else:
        print("wrong fuzzy option")
        
    # generalization:
    general_data["y_pred"] = clf.predict(general_X)
    general_data["y_prob_positive_class"] = clf.predict_proba(general_X)[:, 1] 
    
    training_utils.save_results(output_path, experiment_name, fuzzy_option,
                 training_data, general_data, metrics, std, pr_curve, pd.DataFrame(), pd.DataFrame(),
                 info_columns, features)
    
print("done.")

