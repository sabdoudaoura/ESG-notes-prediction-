import numpy as np
import math
import pandas as pd
import Labels


# def float_to_int(df, column): 
#     # df is a DataFrame, column is the name of the feature to convert
#     for index, value in df[column].iteritems():
#         if not math.isnan(value):
#             df[column].iloc[index] = int(value)
        

def float_to_int(s): # s is a Series
    res = pd.Series([])
    for index, value in s.iteritems():
        if not math.isnan(value):
            res[index] = int(s[index])
        else:
            res[index] = np.nan
    return res
    
# Encoding
def encode_col(df, column, encode_dict): 
    # encode the column using the encode_dict
    df[column].map(encode_dict)


# Now we define a function that transforms the values 'Not Collected' or 'Not Adaptable' in a Series
# to np.nan to easily identify them

def transform_to_nan(df, column):
    for index, value in df[column].iteritems():
        if value == 'Not Collected' or value == 'Not Applicable':
            df[column].iloc[index] = np.nan

def to_Nan(df) :
  str_columns = df.select_dtypes('object').columns
  for column in str_columns:
      transform_to_nan(df, column)
      
def match_subIndustry(df) : 

    '''** This function fill the NaN for a spécified column based on a dictionnary**

    input

    df : pd.DataFrame
    column : str

    '''
    
    mask = df['GICSSubIndustry'].isin(['Computer Hardware', 'Computer Storage & Peripherals', 'Diversified Commercial & Professional Services', 'Real Estate Investment Trusts' ])
    for row in df[mask].index : 
        company_subIndustry = df.loc[row, 'GICSSubIndustry']
        df.loc[row, 'GICSSubIndustry'] = Labels.sub_industry_map[company_subIndustry]

def fill_sectors(df, column):
  
    '''** This function fill the NaN for a spécified column based on a dictionnary**

    input

    df : pd.DataFrame
    column : str

    '''
    mask = df[column].isna()
    for row in df[mask].index : 
        company_name = df.loc[row, 'CompanyNameAlias']
        df.loc[row, column] = Labels.sector_map[company_name][column]



def fill_first_arg(df, column_1, column_2): 

    '''** This function fill the NaN for a spécified column based on a dictionnary**

    input

    df : pd.DataFrame
    column : str

    '''

    # We want to create a Series with non nan values of s_1 
    # and replacing nan values of s_1 by values of s2
    et = 'and'
    nan_indexes = df[column_1][df[column_1].isnull()].index
    for index, value in df[column_2].iteritems():
        if value == 'Not Collected' or value == 'Not Applicable':
            if  not index in nan_indexes:
                # We will attribute value of s_1 here
                if et in df[column_1][index]:
                    df[column_2][index] = df[column_1].iloc[index].replace(et, '&')
                else:
                    df[column_2][index] = df[column_1].iloc[index]
    
def merge(df, column_1, column_2):
    '''** This function fill NaN values from column_1 with values from column_2**

    input

    df : pd.DataFrame
    column_1 : str
    column_2 : str

    return
    res : pd.Series

    '''
    res = pd.Series([])
    for index, value in df[column_1].iteritems():
        if not math.isnan(value):
            res[index] = value
        else:
            res[index] = df[column_2].iloc[index]
    return res


def fill_real_values(df, feature):
    '''** This function fill NaN values in real valued columns using feature for clustering**

    Input

    df : pd.DataFrame
    feature : str

    '''

    float_columns = df.select_dtypes(include='float').columns.tolist()

    if 'EnvRatingNumeric' in float_columns : float_columns.remove('EnvRatingNumeric')

    for column in float_columns : 

        rows = df[df[column].isna()].index
        for row in rows :
            df.loc[row, column] = df[df[feature] == df.loc[row,feature] ].mean()[column]

def remove_outliers(df): 
    '''** This function removes outliers from a DataFrame**

    input

    df : pd.DataFrame

    return
    res : pd.DataFrame

    '''
    
    outliers_columns  = ['ClimateScope3Emissions']
    for column in outliers_columns :
        lower_limit = df[column].mean() - 8*df[column].std()
        upper_limit = df[column].mean() + 8*df[column].std()
        df = df[(df[column]>lower_limit)&(df[column]<upper_limit)]
    return df


