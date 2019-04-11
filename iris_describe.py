#%%

# Etem Kaya 11-Apr-2019
# Iris Data Set Project.
# Analyse Iris Dataset with 'pivot and describe' methods

import pandas as pd # import pandas library
import seaborn as sns # import seaborn library
import numpy as np

# f = pd.read_csv("iris.csv") # import dataset with panda
f = sns.load_dataset("iris") # this time import dataset with seaborn

# pivoting the dataset with describe method based on the species column
print("Pivot the dataframe based on the values in the 'sepal_length' column", "\n")
print(f.pivot(columns='species', values='sepal_length').describe(), "\n")
print("Pivot the dataframe based on the values in the 'sepal_width' column", "\n")
print(f.pivot(columns='species', values='sepal_width').describe(), "\n")
print("Pivot the dataframe based on the values in the 'petal_length' column", "\n")
print(f.pivot(columns='species', values='petal_length').describe(), "\n")
print("Pivot the dataframe based on the values in the 'petal_width' column", "\n")
print(f.pivot(columns='species', values='petal_width').describe(), "\n")
print("Pivot the dataframe based on the values in the 'species' column", "\n")
print(f.pivot(columns='species', values='species').describe(), "\n")

# describe entire dataset for all species
print("Describe the entire dataframe", "\n")
print(f.describe(), "\n")