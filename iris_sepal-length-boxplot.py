#%%
# Etem Kaya 09-Apr-2019
# Iris Data Set Project.

# import pandas and seaborn libraries
import pandas as pd
import seaborn as sns

# set style and colour using seaborn library
sns.set(style="ticks", color_codes=True)

# import iris dataset with Pandas
f = pd.read_csv("iris.csv")

# boxplot sepal lenght
sns.boxplot(x="species", y="sepal_length", data=f)