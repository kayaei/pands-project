#%%

# Etem Kaya 11-Apr-2019
# Irish Data Set Project.
# Analysing Iris Dataset with 'mean, max, min and median' functions

import pandas as pd #pandas module imported
import seaborn as sns

# f = pd.read_csv("iris.csv") #import dataset with panda
f = sns.load_dataset("iris") #import dataset with seaborn

print("Mean of Sepal Length is", f["sepal_length"].mean())
print("\n")
print("Mean of Sepal Width is", f["sepal_width"].mean())
print("\n")
print("Mean of Petal Length is", f["petal_length"].mean())
print("\n")
print("Mean of Petal Width is", f["petal_width"].mean())
print("\n")

group = f.groupby("species")

print("Mean of all 3 Species")
print(group.mean())
print("\n")

print("Max value of all 3 Species")
print(group.max())
print("\n")

print("Min value of all 3 Species")
print(group.min())
print("\n")

print("Median of all 3 Species")
print(group.median())
print("\n")