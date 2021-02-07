
#import libraries
from flask import Flask, escape, request
import pandas as pd
import numpy as np
from pyod.models.knn import KNN



# Reading the downloaded content and turning it into a pandas dataframe
df = pd.read_csv("https://github.com/DawnSfuuuuza/MSDS343/blob/main/Project.csv")
# Printing out the first 5 rows of the dataframe
print (df.head())


project_df.info(verbose=True)


# Segregate the transfer data and the class labels 
X = project_df['Total'].values.reshape(-1,1)
y = project_df['Class'].values


# Train kNN detector
clf = KNN(contamination=0.02, n_neighbors=5)
clf.fit(X)



# Get the prediction labels of the training data
y_train_pred = clf.labels_     
# Outlier scores
y_train_scores = clf.decision_scores_


# Import the utility function for model evaluation
from pyod.utils import evaluate_print
# Evaluate on the training data
evaluate_print('KNN', y, y_train_scores)


# A total of $1256
X_test_abnormal = np.array([[1256.]])
# Predict
clf.predict(X_test_abnormal)


# A total of $51896
X_test_abnormal = np.array([[51896.]])
# Predict
clf.predict(X_test_abnormal)
