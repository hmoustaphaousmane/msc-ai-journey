import pandas as pd
import numpy as np
from sklearn.preprocessing import LabelEncoder, MinMaxScaler

data = {
    'Age': [23, 25, np.nan, 30, 28],
    'Salary': [25000, 30000, 28000, np.nan, 45000],
    'Gender': ['Male', 'Female', 'Female', 'Male', 'Female',]
}

df = pd.DataFrame(data)

print("Original Dataset")
print(df)

# Fill missing values
df['Age'].fillna(df['Age'].mean(), inplace=True)
df['Salary'].fillna(df['Salary'].mean(), inplace=True)

# Encoding
encoder = LabelEncoder()
df['Gender'] = encoder.fit_transform(df['Gender'])

# Normalization
scaler = MinMaxScaler()
df[['Age', 'Gender']] = scaler.fit_transform(df[['Age', 'Gender']])

print("Processed Data")
print(df)
