# Importing the required libraries
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.metrics import mutual_info_score
from sklearn.metrics import r2_score

from sklearn.feature_extraction import DictVectorizer
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import GradientBoostingRegressor

import pickle

# This function will take average of both values
def convert(x):
    tokens = x.split('-')
    if len(tokens) == 2:
        return(float(tokens[0])+float(tokens[1]))/2
    try:
        return float(x)
    except:
        return None

def remove_pps_outliers(df):
    df_out = pd.DataFrame()
    for key, subdf in df.groupby('location'):
        m = np.mean(subdf.price_per_sqft)
        st = np.std(subdf.price_per_sqft)
        reduced_df = subdf[(subdf.price_per_sqft>(m-st)) & (subdf.price_per_sqft<=(m+st))]
        df_out = pd.concat([df_out,reduced_df],ignore_index=True)
    return df_out
    
# Function to train the model
def train(df_train, y_train):
    dicts = df_train[categorical + numerical].to_dict(orient='records')
    
    dv = DictVectorizer(sparse=False)
    X_train = dv.fit_transform(dicts)
    
    model = GradientBoostingRegressor(n_estimators=100)
    model.fit(X_train, y_train)

    return dv, model

# Function to predict
def predict(df, dv, model):
    dicts = df[categorical + numerical].to_dict(orient='records')

    X_test = dv.transform(dicts)
    y_pred = model.predict(X_test)

    return y_pred

# Data Ingestion
df = pd.read_csv('bengaluru_house_data.csv')

# Dropping less important feature
df = df.drop(columns = ['area_type','society','balcony','availability'])

# Dropping the missing value
df = df.dropna()

# Making a new feature by counting number of bedrooms and BHK
df['bhk'] = df['size'].apply(lambda x : int(x.split(' ')[0]))

# Converting the values
df['total_sqft']  =  df['total_sqft'].apply(convert)

# Very few null values just dropping
df = df.dropna()

# Dropping those values which have less than 300 sqft space per bedroom
df = df[~(df.total_sqft/df.bhk < 300)]

# Creating one more feature price_per_sqft
df["price_per_sqft"] = df["price"]*100000/df["total_sqft"]

# Removing outlier
df = remove_pps_outliers(df)

# Unique values count of location
df.location = df.location.apply(lambda x: x.strip())
location_stats = df['location'].value_counts(ascending=False)
                                             
# Creating list of location which have less than 10 properties
location_stats_less_than_10 = location_stats[location_stats<=10]

# Making location value other is there is less than 10 properties
df.location = df.location.apply(lambda x: 'other' if x in location_stats_less_than_10 else x)

# Converting data type to int
df['bath'] = df['bath'].astype('int')
df = df[df.bath < df.bhk+2]

# Drop size since we have bhk and price_per_sqft
df = df.drop(columns=['size', 'price_per_sqft'])

# Setting the validation framework
df_full_train, df_test = train_test_split(df, test_size=0.2, random_state=1)
df_train, df_val = train_test_split(df_full_train, test_size=0.25, random_state=1)

df_train = df_train.reset_index(drop=True)
df_val = df_val.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train.price.values
y_val = df_val.price.values
y_test = df_test.price.values

del df_train['price']
del df_val['price']
del df_test['price']

# Numerical and categorical features
numerical = ['total_sqft', 'bath', 'bhk']
categorical = ['location']

# Model Training
dv, model = train(df_full_train, df_full_train.price.values)
y_pred = predict(df_test, dv, model)

# Model Accuracy
score = r2_score(y_test, y_pred)
print(f'Model Score (R-squared): {score}')

# Constructing the model file name
output_file_name = f'gbr_model.bin'

# Opening file and saving the model
with open(output_file_name , 'wb') as f_out:
    pickle.dump((dv, model), f_out)

print(f"Model saved in file: {output_file_name}")
