#%%
# Etem Kaya 09-Apr-2019
# Irish Data Set Project.

# import pandas, seaborn and matplotlib libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# set style and colour using seaborn library
sns.set(style="darkgrid", color_codes=True)

# import iris dataset with Pandas
f = pd.read_csv("iris.csv")

# boxplot petal lenght
sns.boxplot(x="species", y="petal_length", data=f)
plt.show()

# boxplot petal width
sns.boxplot(x="species", y="petal_width", data=f)
plt.show()