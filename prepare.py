
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