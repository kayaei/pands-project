#%%
# Etem Kaya 09-Apr-2019
# Irish Data Set Project.

# import pandas and seaborn libraries
import pandas as pd
import seaborn as sns

# set style and colour using seaborn library
sns.set(style="darkgrid", color_codes=True)

# import iris dataset with Pandas
f = pd.read_csv("iris.csv")

# boxplot petal lenght
sns.boxplot(x="species", y="petal_length", data=f)