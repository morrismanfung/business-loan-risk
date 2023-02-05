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
from sklearn.metrics import classification_report, confusion_matrix, precision_recall_curve, precision_score, recall_score, f1_score
import seaborn as sns
import pickle
import os

def pr_curve( model, X_train, X_test, y_train, y_test):
    model.fit( X_train, y_train)

    try:
        proba = model.predict_proba( X_test)[ :, 1]
    except:
        proba = model.decision_function( X_test)
    
    precision, recall, thresholds = precision_recall_curve( y_test, proba)
    thresholds = np.append( thresholds, 1)

    plot_df = pd.DataFrame( {
        'precision': precision,
        'recall': recall,
        'thresholds': thresholds
    })

    chart = sns.scatterplot(
        data = plot_df,
        x = 'precision',
        y = 'recall'
    )

    return plot_df, chart

def better_confusion_matrix( y_test, y_hat, labels = [ 0, 1]):
    df = pd.DataFrame( confusion_matrix( y_test, y_hat, labels = labels))
    df.columns = labels
    df = pd.concat( [ df], axis = 1, keys = ['Predicted'])
    df.index = labels
    df = pd.concat( [df], axis = 0, keys = ['Actual'])
    return df


def test_scoring_metrics( y_test, y_hat, X_test):
    metrics = {
        'precision': precision_score( y_test, y_hat),
        'recall': recall_score( y_test, y_hat),
        'f1': f1_score( y_test, y_hat)
    }
    return metrics

class SVC_thld( SVC):
    def __init__( self, gamma = 'scale', C = 1.0, random_state = None, threshold = None):
        super().__init__(
            gamma = gamma,
            C = C,
            random_state = random_state
        )
        self.threshold = threshold

    def predict( self, X):
        if self.threshold == None:
            predictions = super( SVC_thld, self).predict( X)
        else:
            result = super( SVC_thld, self).decision_function( X)
            predictions = result >= self.threshold
        return predictions


class RFC_thld( RandomForestClassifier):
    def __init__( self, n_estimators = 100, max_depth = None, max_features = 'sqrt', criterion = 'gini',
        bootstrap = True, random_state = None, threshold = None):
        super().__init__( 
            n_estimators = n_estimators,
            max_depth = max_depth,
            max_features = max_features,
            criterion = criterion,
            bootstrap = bootstrap,
            random_state = random_state
        )
        self.threshold = threshold

    def predict( self, X):
        if self.threshold == None:
            predictions = super( RFC_thld, self).predict( X)
        else:
            result = super( RFC_thld, self).predict_proba( X)[ :, 1]
            predictions = result >= self.threshold
        return predictions

class NB_thld( GaussianNB):
    def __init__( self, threshold = None):
        super().__init__()
        self.threshold = threshold

    def predict( self, X):
        if self.threshold == None:
            predictions = super( NB_thld, self).predict( X)
        else:
            result = super( NB_thld, self).predict_proba( X)[ :, 1]
            predictions = result >= self.threshold
        return predictions

class LogReg_thld( LogisticRegression):
    def __init__( self, l1_ratio = 0, C = 1.0, random_state = None, threshold = None):
        super().__init__(
            penalty = 'elasticnet',
            max_iter = 2000,
            tol = 0.001,
            solver= 'saga',
            C = C,
            l1_ratio = l1_ratio,
            random_state = random_state
        )
        self.threshold = threshold

    def predict( self, X):
        if self.threshold == None:
            predictions = super( LogReg_thld, self).predict( X)
        else:
            result = super( LogReg_thld, self).predict_proba( X)[ :, 1]
            predictions = result >= self.threshold
        return predictions

class LinearSVC_thld( LinearSVC):
    def __init__( self, C = 1.0, random_state = None, threshold = None):
        super().__init__(
            dual = False,
            C = C,
            random_state = random_state
        )
        self.threshold = threshold

    def predict( self, X):
        if self.threshold == None:
            predictions = super( LinearSVC_thld, self).predict( X)
        else:
            result = super( LinearSVC_thld, self).decision_function( X)
            predictions = result >= self.threshold
        return predictions