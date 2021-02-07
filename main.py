
from flask import Flask, escape, request
import pandas as pd



# Reading the downloaded content and turning it into a pandas dataframe

df = pd.read_csv("https://github.com/DawnSfuuuuza/MSDS343/blob/main/Project.csv")

# Printing out the first 5 rows of the dataframe

print (df.head())
