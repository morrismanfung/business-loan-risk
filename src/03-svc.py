# Author: Morris M. F. Chan
# 2023-02-04

import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score, cross_validate, train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_curve
from pickle import dump, load
import os

# from functions import *
from shortcut import SVC_thld, pr_curve

def main():
    df_train = pd.read_csv( 'data/train_processed.csv')
    df_test = pd.read_csv( 'data/test_processed.csv')
    X_train, y_train = df_train.drop( 'ChargedOff', axis = 1), df_train[ 'ChargedOff']
    X_test, y_test = df_test.drop( 'ChargedOff', axis = 1), df_test[ 'ChargedOff']
    cv_scoring_metrics = [ 'precision', 'recall', 'f1']

    with open( 'src/saved-obj/column-transformer.pkl', 'rb') as f:
        column_transformer = load( f)

    pipe_svc = make_pipeline( column_transformer, SVC_thld( random_state = 69))
    best_params = hyperparameter_optimization( pipe_svc, X_train, y_train)
    pipe_svc_opt = make_pipeline( column_transformer,
                                  SVC_thld( gamma = best_params[ 'svc_thld__gamma'],
                                            C = best_params[ 'svc_thld__C'],
                                            random_state = 69))

    svc_dict = {
        'best_params': best_params
    }

    with open( 'src/saved-obj/01-svc_dict_tmp.pkl', 'wb') as f:
        dump( svc_dict, f)
    
    threshold_tuning( pipe_svc_opt, X_train, y_train)

    '''
    with open( 'bin/04-svc', 'w') as f:
        f.close()
    '''

def hyperparameter_optimization( pipe_svc, X_train, y_train):
    param_dist = {
        'svc_thld__C': [ 10**x for x in range( -2, 2)],
        'svc_thld__gamma': [ 10**x for x in range( -2, 2)]
    }

    random_search_svc = RandomizedSearchCV(
        pipe_svc, param_dist, n_iter = 10, cv = 5, scoring = 'f1', n_jobs=-1, return_train_score = True, random_state = 69
    )

    random_search_svc.fit( X_train, y_train)
    return random_search_svc.best_params_

def threshold_tuning( pipe_svc_opt, X_train, y_train):
    X_cv_train, X_cv_test, y_cv_train, y_cv_test = train_test_split(
        X_train, y_train, test_size = 0.2, stratify = y_train, random_state = 69)
    pr_curve_df, pr_curve_img = pr_curve( pipe_svc_opt, X_cv_train, X_cv_test, y_cv_train, y_cv_test)
    pr_curve_df.to_csv( 'src/saved-obj/01-svc-thlds.csv')
    pr_curve_img.get_figure().savefig( 'src/saved-obj/01-svc-pr-curve.png')

if __name__ == '__main__':
    main()