# Etem Kaya 31-Mar-2019
# Irish Data Set Project.

# Analysis of Iris Dataset

# Import pandas library
import pandas as pd

# Import dataset with panda
f = pd.read_csv('iris.csv')

print("\n" + str(f.columns))                   # column names
print("\n")
print("\n" + str(f.info()))                    # information for all columns
print("\n" + str(f.describe()))                # summary of each column
print("\n" + str(f["species"].value_counts())) # row count in each species
print("\n" + str(f.shape))                     # total row and column count
print("\n" + str(f.head()))                    # print first 5 rows
print("\n" + str(f.tail()))                    # print last 5 rows
print("\n" + str(f.sample(5)))                 # output 5 random rows

# reference https://stackoverflow.com/a/29530559
print("\n" + str(f.isnull().any()))            # find any null values

