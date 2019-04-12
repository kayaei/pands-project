#%%

# Etem Kaya 11-Apr-2019
# Iris Data Set Project.
# Group Histogram graphs of Iris Dataset

# import pandas, seaborn and matplotlib libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import dataset with pandas
f = pd.read_csv("iris.csv") 

# set the backround colur of the histogram graph
sns.set(style="whitegrid")

# set the bar colour, figure size and bin size of the graphs
f.hist(color = "green", figsize = (12, 8), bins = 18)
# plot the graph
plt.show()            