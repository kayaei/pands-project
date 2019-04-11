# Etem Kaya 31-Mar-2019
# Iris Data Set Project.

# Analysis of Iris Dataset

# Import pandas library
import pandas as pd

# Import dataset with panda
f = pd.read_csv('iris.csv')

print(str(f.info()) + "\n") # information about the dataset
print(str(f.describe()) + "\n") # summary of each species
print(str(f.shape) + "\n") # total row and column count
print(str(f.head()) + "\n") # print first 5 rows
print(str(f.tail()) + "\n") # print last 5 rows
print(str(f.sample(5)) + "\n") # output 5 random rows
print((f.columns) + "\n") # column names of the dataset

# adopted from https://stackoverflow.com/a/29530559
print("\n" + str(f.isnull().any()) + "\n") # find any null values

# adopted from https://priagungkhusumanegara.github.io/data/Data_Visualization.html
print(f["species"].value_counts()) # row count in each species


