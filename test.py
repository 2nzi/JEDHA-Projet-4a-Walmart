#%%
import pandas as pd 
import sys
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.pipeline import Pipeline
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler, LabelEncoder
from sklearn.compose import ColumnTransformer
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import warnings
from sklearn.linear_model import LinearRegression
import plotly.express as px
import plotly.graph_objects as go
import plotly.figure_factory as ff
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error

warnings.filterwarnings(
    "ignore", category=DeprecationWarning
)  # to avoid deprecation warnings



df = pd.read_csv("Walmart_Store_sales.csv")


# Assuming you have imported all necessary libraries

# Separate features and target
target = 'Weekly_Sales'
features = ['Store', 'Holiday_Flag', 'Temperature', 'Fuel_Price', 'CPI', 'Unemployment']
df.dropna(subset=[target], inplace=True)

Y = df[target]
X = df[features]

# Split the data into training and testing sets
X_train, X_test, Y_train, Y_test = train_test_split(X, Y, train_size=0.8, test_size=0.2, random_state=0)

# Define a pipeline with an imputer to handle missing values
pipeline = Pipeline([
    ('imputer', SimpleImputer(strategy='median')),
    ('regressor', LinearRegression())
])

# Train the model
pipeline.fit(X_train, Y_train)

# Predictions
Y_train_pred = pipeline.predict(X_train)
Y_test_pred = pipeline.predict(X_test)

print(
    "Accuracy on training set : ", pipeline.score(X_train, Y_train)
)  # Here, the features must be passed first, and then the true label
print("Accuracy on test set : ", pipeline.score(X_test, Y_test))

# %%
