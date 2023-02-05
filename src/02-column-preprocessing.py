# Author: Morris M. F. Chan
# 2023-02-04

import numpy as np
import pandas as pd
from sklearn.model_selection import cross_val_score, cross_validate, train_test_split, GridSearchCV, RandomizedSearchCV
from sklearn.preprocessing import StandardScaler, FunctionTransformer, OneHotEncoder
from sklearn.pipeline import Pipeline, make_pipeline
from sklearn.compose import make_column_transformer
from sklearn.linear_model import LogisticRegression
from sklearn.feature_selection import RFE
from sklearn.impute import SimpleImputer
from pickle import dump

def main():
    df_train = pd.read_csv( 'data/train.csv')
    df_train_processed = preprocess( df_train)
    df_train_processed.to_csv( 'data/train_processed.csv')
    df_test = pd.read_csv( 'data/test.csv')
    df_test_processed = preprocess( df_test)
    df_test_processed.to_csv( 'data/test_processed.csv')

    X_train, y_train = df_train.drop( 'LoanStatus', axis = 1), df_train[ 'LoanStatus']
    X_test, y_test = df_test.drop( 'LoanStatus', axis = 1), df_test[ 'LoanStatus']
    scoring_metrics = [ 'precision', 'recall', 'f1']

    cols = {
        'cols_std':[ 'TermInMonths', 'JobsSupported'],
        'cols_log_std': [ 'ThirdPartyDollars'],
        'cols_one_hot': [ 'BorrState', 'DeliveryMethod', 'NasicsSector', 'BusinessType'],
        'cols_passthrough': [ 'Franchise']
    }

    column_transformer = column_transformer_pre_selection( X_train, cols)
    with open( 'src/saved-obj/column-transformer.pkl', 'wb') as f:
        dump( column_transformer, f)

def preprocess( df):
    df[ 'NasicsSector'] = df[ 'NaicsCode'].astype( str).str[:2].replace( 'na', '00')
    df[ 'Franchise'] = ~df[ 'FranchiseCode'].isna()
    return df

def column_transformer_pre_selection( X_train, cols):
    log_transformer = FunctionTransformer( np.log)
    pipe_log_std = make_pipeline(
        SimpleImputer( strategy='median'), log_transformer, StandardScaler()
    )

    column_transformer_pre = make_column_transformer(
        ( make_pipeline( SimpleImputer( strategy='median'), StandardScaler()), cols[ 'cols_std']),
        ( pipe_log_std, cols[ 'cols_log_std']),
        ( make_pipeline( SimpleImputer( strategy='constant', fill_value = 'NA'), OneHotEncoder( handle_unknown = 'ignore')), cols[ 'cols_one_hot']),
        ( 'passthrough', cols['cols_passthrough'])
    )
    
    return column_transformer_pre

if __name__ == '__main__':
    main()
