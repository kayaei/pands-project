#%%

# Etem Kaya 11-Apr-2019
# Iris Data Set Project.
# Analysing Iris Dataset with 'mean, max, min and median' functions

import pandas as pd # import pandas library
import seaborn as sns # import seaborn library

f = pd.read_csv("iris.csv") # import dataset with panda

# split the dataset based on the species category with iloc function
print(f.iloc[0:50])
print("\n")
print(f.iloc[50:100])
print("\n")
print(f.iloc[100:150])

# another way of splitting the dataset with loc function
print(f.loc[f["species"]=="setosa"])
print("\n")
print(f.loc[f["species"]=="versicolor"])
print("\n")
print(f.loc[f["species"]=="virginica"])
print("\n")
