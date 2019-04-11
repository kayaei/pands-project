#%%

# Etem Kaya 11-Apr-2019
# Iris Data Set Project.
# Analysing Iris Dataset with 'mean, max, min and median' functions

import pandas as pd # import pandas library
import seaborn as sns # import seaborn library

# f = pd.read_csv("iris.csv") # import dataset with panda
f = sns.load_dataset("iris") # this time import dataset with seaborn

# finding the mean of each attribute
print("Mean of Sepal Length is", f["sepal_length"].mean())
print("\n")
print("Mean of Sepal Width is", f["sepal_width"].mean())
print("\n")
print("Mean of Petal Length is", f["petal_length"].mean())
print("\n")
print("Mean of Petal Width is", f["petal_width"].mean())
print("\n")

# group the iris dataset by the species column
group = f.groupby("species")

# find the mean of each attribute for all 3 species
print("Mean of all 3 Species")
print(group.mean())
print("\n")