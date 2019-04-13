#%%
# Etem Kaya 08-Apr-2019
# Iris Data Set Project.

# Boxplot iris dataset
# import pandas, seaborn and matplotlib libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import iris dataset with Pandas
f = pd.read_csv("iris.csv")

# set the boxplot graph for iris flower species
plt.figure(figsize = (10, 8)) # set the graph size
plt.title("Iris Flower Species BoxPlot") # title of the plot

# set the boxplot style
sns.set(style="darkgrid", color_codes=True) # set the background colour
sns.boxplot(data=f) # set the dataset to plot     

# plot the data
plt.show()
