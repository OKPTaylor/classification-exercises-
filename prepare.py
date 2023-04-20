
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import scipy.stats as stats
import pandas as pd
from sklearn.model_selection import train_test_split

#this is a function to split your data into train, validate, and test sets

def split_function(df_name, target_varible_column_name):
    train, test = train_test_split(df_name,
                                   random_state=123, #can be whatever you want
                                   test_size=.20,
                                   stratify= df_name[target_varible_column_name])
    
    train, validate = train_test_split(train,
                                   random_state=123,
                                   test_size=.25,
                                   stratify= train[target_varible_column_name])
    return train, validate, test

#call should look like: 
#train_df_name, validate_df_name, test_df_name = split_function(df_name, 'target_varible_column_name')

#This function is for running through catagorical on catagorical features graphing and running the chi2 test on them
def cat_on_cat_graph_loop(dataframe_name, dataframe_train_name, col_cat):
    for col in col_cat:
        print()
        print(col.upper())
        print(dataframe_name[col].value_counts())
        print(dataframe_name[col].value_counts(normalize=True))
        dataframe_name[col].value_counts().plot.bar()
        plt.show()
        print()
        print()
        print(f'HYPOTHESIZE')
        print(f"H_0: {col.lower().replace('_',' ')} does not survival")
        print(f"H_a: {col.lower().replace('_',' ')} affects survival")
        print()
        print(f'VISUALIZE')
        sns.barplot(x=dataframe_train_name[col], y=dataframe_train_name['survived'])
        plt.title(f"{col.lower().replace('_',' ')} vs Survive")
        plt.show()
        print()
        print('ANALYZE and SUMMARIZE')
        observed = pd.crosstab(dataframe_train_name[col], dataframe_train_name.survived)
        chi2Test(observed)
        print()
        print()
#the call should be: prep.cat_on_cat_graph_loop(dataframe_name, dataframe_train_name, col_cat)        

#this funciton works in this module to run the chi2 test with the above function
def chi2Test(observed):
    alpha = 0.05
    chi2, pval, degf, expected = stats.chi2_contingency(observed)
    print('Observed')
    print(observed.values)
    print('\nExpected')
    print(expected.astype(int))
    print('\n----')
    print(f'chi^2 = {chi2:.4f}')
    print(f'p-value = {pval:.4f}')
    print('----')
    if pval < alpha:
        print ('We reject the null hypothesis.')
    else:
        print ("We fail to reject the null hypothesis.")
# prep.chi2Test(observed) is the call 