# %%
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
# import os
# import re


# %%
# import torch

# print(torch.__version__)
# print(torch.cuda.is_available())


# %%
df = pd.read_csv("/Users/belladu/Desktop/IDS721 Cloud/ids721-project3-0322/enrollments.csv")
df.head()

# %%
df.shape

# %%
df.describe()

# %%
df.isna().sum()

# %%
!pip install sagemaker

# %%
# use a loop to make every non-numeric column into a one-hot encoded column
for col in df.columns:
    if df[col].dtype == "object":
        df = pd.concat([df, pd.get_dummies(df[col], prefix=col)], axis=1)
        df = df.drop(col, axis=1)
df_new = df.copy()
df_new.head()
        

# %%
# drop the rows with missing values
df_new = df.copy()
df_new.shape

# %%
# drop all nan values
df_new = df_new.select_dtypes(include=[np.number])
df_new.head()
df_new.shape


# %%
# use mean to fill the missing values: standardization
df_new = df_new.fillna(df_new.mean())
df_new.head()


# %%
# get a linear regression model to predict students5_estimated
# get a linear regression model to predict students5_estimated
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler


X = df_new.drop(['students5_estimated'], axis=1)
y = df_new['students5_estimated']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

reg = LinearRegression().fit(X_train, y_train)

y_pred = reg.predict(X_test)

print('Coefficients: \n', reg.coef_)
# The mean squared error
print("Mean squared error: %.2f"
        % mean_squared_error(y_test, y_pred))
# Explained variance score: 1 is perfect prediction
print('Variance score: %.2f' % r2_score(y_test, y_pred))

# plot the predicted values vs the actual values
plt.scatter(y_test, y_pred)
plt.xlabel("Actual values")
plt.ylabel("Predicted values")
plt.title("Actual vs Predicted values")
plt.show()

# get the residuals
residuals = y_test - y_pred
plt.scatter(y_pred, residuals)
plt.xlabel("Predicted values")
plt.ylabel("Residuals")
plt.title("Predicted vs Residuals")
plt.show()



# %%
# make training and testing data into separate csv files
X_train = pd.DataFrame(X_train)
X_test = pd.DataFrame(X_test)
y_train = pd.DataFrame(y_train)
y_test = pd.DataFrame(y_test)

X_train.to_csv('X_train.csv', index=False)
X_test.to_csv('X_test.csv', index=False)
y_train.to_csv('y_train.csv', index=False)
y_test.to_csv('y_test.csv', index=False)

# combine the training data and testing data
X_train['y_train'] = y_train
X_test['y_test'] = y_test

X_train.to_csv('train.csv', index=False)

X_test.to_csv('test.csv', index=False)

# %%
import boto3
region_name = 'us-east-1'
session = boto3.session.Session(region_name=region_name)


# %%
import sagemaker

role_arn = ""

sess = sagemaker.Session()

# get execution role
role = sagemaker.get_execution_role()


# %%
import sagemaker
from sagemaker import get_execution_role

# Set up the S3 bucket and prefix where you want to store your data
bucket = 'ids721-project3-0322'

# Upload your data to S3
# train_data = sess.upload_data(path='/Users/belladu/Desktop/IDS721 Cloud/ids721-project3-0322/train.csv', bucket=bucket, key_prefix='/train')
# test_data = sess.upload_data(path='/Users/belladu/Desktop/IDS721 Cloud/ids721-project3-0322/test.csv', bucket=bucket, key_prefix='/test')



# %%
# use sage maker to train the model
from sagemaker import get_execution_role
from sagemaker.amazon.amazon_estimator import get_image_uri
from sagemaker.estimator import Estimator

container = get_image_uri(boto3.Session().region_name, 'linear-learner')


# %%
# set the role of IAM
# role = get_execution_role()


# %%
# Set up the estimator
linear = Estimator(container,
                     role=get_execution_role(),
                        train_instance_count=1, 
                        train_instance_type='ml.m4.xlarge',
                        output_path='s3://{}/output'.format(bucket),
                        sagemaker_session=sess)
                        

# %%
# fit the model
linear.fit({'train': 's3://{}/train.csv'.format(bucket)})
linear.fit({'train': train_data})



