# Importing the required libraries
import numpy as np
import pandas as pd

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

import pickle

# Function to train the model
def train(df_train, y_train):
    model = RandomForestClassifier()
    model.fit(df_train, y_train)

    return model

# Function to predict
def predict(df_test, model):
    y_pred = model.predict(df_test)

    return y_pred

# Data Ingestion
df = pd.read_csv('apple_quality_data.csv')

# Convert column name in snake case form
df.columns = [col.lower().replace(' ', '_') for col in df.columns]

# Dropping less important feature
df = df.drop(columns=['a_id'])

# Dropping the missing value
df = df.dropna()

# Converting acidity data type to float
df['acidity'] = df['acidity'].astype(float)

# Encoding the target variable
df['quality'] = df['quality'].map({'good': 1, 'bad': 0})

# Setting the validation framework
df_train, df_test = train_test_split(df, test_size=0.2, random_state=1)

df_train = df_train.reset_index(drop=True)
df_test = df_test.reset_index(drop=True)

y_train = df_train.quality.values
y_test = df_test.quality.values

del df_train['quality']
del df_test['quality']

# Model Training
model = train(df_train, y_train)
y_pred = predict(df_test, model)

# Calculating the model accuracy score
model_accuracy = accuracy_score(y_test, y_pred)
print(f"Random Forest Classifier Accuracy: {model_accuracy:.2f}")

# Constructing the model file name
output_file_name = f'rfc_model.bin'

# Opening file and saving the model
with open(output_file_name , 'wb') as f_out:
    pickle.dump(model, f_out)

print(f"Model saved in file: {output_file_name}")