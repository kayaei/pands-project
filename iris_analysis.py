#%%

# Etem Kaya 11-Apr-2019
# Iris Data Set Project.
# Analysing Iris Dataset with 'mean, max, min, median and mode' functions

import pandas as pd # import pandas library
import seaborn as sns # import seaborn library

# f = pd.read_csv("iris.csv") # import dataset with panda
f = sns.load_dataset("iris") # this time import dataset with seaborn

# finding the mean of each attribute
print("Mean of Sepal Length is", f["sepal_length"].mean())
print("Mean of Sepal Width is", f["sepal_width"].mean())
print("Mean of Petal Length is", f["petal_length"].mean())
print("Mean of Petal Width is", f["petal_width"].mean())
print("\n")

# finding the max value of each attribute
print("Max value of Sepal Length is", f["sepal_length"].max())
print("Max value of Sepal Width is", f["sepal_width"].max())
print("Max value of Petal Length is", f["petal_length"].max())
print("Max value of Petal Width is", f["petal_width"].max())
print("\n")

# finding the min value of each attribute
print("Min value of Sepal Length is", f["sepal_length"].min())
print("Min value of Sepal Width is", f["sepal_width"].min())
print("Min value of Petal Length is", f["petal_length"].min())
print("Min value of Petal Width is", f["petal_width"].min())
print("\n")

# finding the median of each attribute
print("Median of Sepal Length is", f["sepal_length"].median())
print("Median of Sepal Width is", f["sepal_width"].median())
print("Median of Petal Length is", f["petal_length"].median())
print("Median of Petal Width is", f["petal_width"].median())
print("\n")

# finding the mode of each attribute
print("Mode of Sepal Length is", f["sepal_length"].mode())
print("\n")
print("Mode of Sepal Width is", f["sepal_width"].mode())
print("\n")
print("Mode of Petal Length is", f["petal_length"].mode())
print("\n")
print("Mode of Petal Width is", f["petal_width"].mode())
print("\n")

# group the iris dataset by the species column
group = f.groupby("species")

# find the mean of each attribute for all 3 species
print("Mean of all 3 Species")
print(group.mean())
print("\n")

# find the max value of each attribute for all 3 species
print("Max value of all 3 Species")
print(group.max())
print("\n")

# find the min value of each attribute for all 3 species
print("Min value of all 3 Species")
print(group.min())
print("\n")

# find the median of each attribute for all 3 species
print("Median of all 3 Species")
print(group.median())
print("\n")