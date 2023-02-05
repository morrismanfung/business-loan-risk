# Author: Morris M. F. Chan
# 2023-01-31
import pandas as pd
from sklearn.model_selection import train_test_split

def main():
    df_1991 = pd.read_csv( 'data/foia-504-fy1991-fy2009-asof-221231.csv')
    df_2010 = pd.read_csv( 'data/foia-504-fy2010-present-asof-221231.csv')
    df = pd.concat( [ df_1991, df_2010], axis = 0)

    cat_columns = [
        'BorrCity', 'BorrState', 'CDC_State', 'ThirdPartyLender_State',  
        'ApprovalFiscalYear', 'DeliveryMethod', 'NaicsCode', 'NaicsDescription', 
        'FranchiseCode', 'FranchiseName', 'ProjectState', 'BusinessType', 'BusinessAge', 'LoanStatus'
    ]
    num_columns = [
        'ThirdPartyDollars', 'GrossApproval', 'TermInMonths', 'GrossChargeOffAmount', 'JobsSupported'
    ]
    columns = cat_columns + num_columns

    df = df[ columns]
    df = df[ (df[ 'LoanStatus']=='PIF') | (df[ 'LoanStatus']=='CHGOFF')]
    train, test = train_test_split( df, test_size = 0.5, random_state = 69)

    train.to_csv( 'data/train.csv')
    test.to_csv( 'data/test.csv')

if __name__ == '__main__':
    main()