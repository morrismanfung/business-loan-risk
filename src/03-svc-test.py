# Author: Morris M. F. Chan918
# 2023-02-05

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

from shortcut import SVC_thld, better_confusion_matrix, test_scoring_metrics

def main():
    df_train = pd.read_csv( 'data/train_processed.csv')
    df_test = pd.read_csv( 'data/test_processed.csv')
    X_train, y_train = df_train.drop( 'ChargedOff', axis = 1), df_train[ 'ChargedOff']
    X_test, y_test = df_test.drop( 'ChargedOff', axis = 1), df_test[ 'ChargedOff']
    cv_scoring_metrics = [ 'precision', 'recall', 'f1']

    column_transformer = load( 'src/saved-obj/column-transformer.pkl')

    with open( 'src/saved-obj/01-svc_dict_tmp.pkl', 'rb') as f:
        svc_dict = load( f)
    best_params = svc_dict[ 'best_params']

    thld = float( pd.read_csv( 'src/saved-obj/thlds.csv', index_col = 0).loc[ 'SVC'])

    pipe_svc_opt = final_svc( column_transformer, best_params, thld)
    svc_dict[ 'cv_scores'] = cross_validate( pipe_svc_opt, X_train, y_train, cv = 5, scoring = cv_scoring_metrics, return_train_score = True)
    svc_dict[ 'test_scores'] = model_testing( pipe_svc_opt, X_train, y_train, X_test, y_test)

    with open( 'src/saved-obj/01-svc_dict.pkl', 'wb') as f:
        dump( svc_dict, f)
    
    '''
    with open( 'bin/04-svc-test', 'w') as f:
        f.close()
    '''

def final_svc( column_transformer, best_params, thld):
    pipe_svc_opt = make_pipeline( column_transformer,
                              SVC_thld( gamma = best_params[ 'svc_thld__gamma'],
                                   C = best_params[ 'svc_thld__C'],
                                   threshold = thld,
                                   random_state = 69))

    return pipe_svc_opt

def model_testing( pipe_svc_opt, X_train, y_train, X_test, y_test):
    pipe_svc_opt.fit( X_train, y_train)
    y_hat_svc_opt = pipe_svc_opt.predict( X_test)

    confusion_matrix_ = better_confusion_matrix( y_test, y_hat_svc_opt, labels = [ True, False])
    confusion_matrix_.to_csv( 'src/saved-obj/01-svc_confusion_matrix.csv')

    classification_report_ = pd.DataFrame( classification_report( y_test, y_hat_svc_opt, output_dict = True))
    classification_report_.to_csv( 'src/saved-obj/01-svc_classification_report.csv')
    return test_scoring_metrics( y_test, y_hat_svc_opt, X_test)

if __name__ == '__main__':
    main()