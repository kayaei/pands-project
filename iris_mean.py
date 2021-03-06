#%%

# Etem Kaya 11-Apr-2019
# Iris Data Set Project.
# Analysing Iris Dataset with 'mean, max, min and median' functions

import pandas as pd # import pandas library
import seaborn as sns # import seaborn library

# f = pd.read_csv("iris.csv") # import dataset with panda
f = sns.load_dataset("iris") # this time import dataset with seaborn

# finding mean of each attribute with pandas
print("Finding mean using pandas", "\n")
print("Mean of Sepal Length is", f["sepal_length"].mean())
print("Mean of Sepal Width is", f["sepal_width"].mean())
print("Mean of Petal Length is", f["petal_length"].mean())
print("Mean of Petal Width is", f["petal_width"].mean())
print("\n")

# group the iris dataset by the species category
group = f.groupby("species")

# finding mean of each attribute for all 3 species using group function
print("Finding mean using 'group' function", "\n")

print("Mean of all 3 Species")
print(group.mean())
print("\n")

# finding mean by splitting the dataset with loc function

print("Finding mean of species using 'loc' function", "\n")

print("Mean of Setosa species")
print(f.loc[f["species"]=="setosa"].mean()) # mean of setosa using loc function
print("\n")
print("Mean of Versicolor species")
print(f.loc[f["species"]=="versicolor"].mean()) # mean of versicolor using loc function
print("\n")
print("Mean of Virginica species")
print(f.loc[f["species"]=="virginica"].mean()) # mean of virginica using loc function
print("\n")

# another way of finding mean by splitting the dataset with iloc function
print("Finding mean of species using 'iloc' function", "\n")

print("Mean of Setosa species")
print(f.iloc[0:50].mean()) # mean of setosa using iloc function
print("\n")
print("Mean of Versicolor species")
print(f.iloc[50:100].mean()) # mean of versicolor using iloc function
print("\n")
print("Mean of Virginica species")    
print(f.iloc[100:150].mean()) # mean of virginica using iloc function