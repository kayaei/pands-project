#%%
# Etem Kaya 09-Apr-2019
# Iris Data Set Project.

# Boxplot iris dataset
# import pandas and seaborn libraries
import pandas as pd
import seaborn as sns

# set style and colour using seaborn library
sns.set(style="darkgrid", color_codes=True)

# import iris dataset with Pandas
f = pd.read_csv("iris.csv")

# boxplot grouped by species
f.boxplot(by='species',figsize=(12,8))