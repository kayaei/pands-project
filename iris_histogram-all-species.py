#%%
# Etem Kaya 12-Apr-2019
# Iris Data Set Project.

# Histogram iris dataset

# import pandas, seaborn and matplotlib libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
# import iris dataset with Pandas
f = pd.read_csv("iris.csv")

# set style and background colour using seaborn library
sns.set(style="darkgrid")

sns.distplot(f["sepal_length"], color= "green")
plt.title('Histogram - Sepal Length of All Species')
plt.xlabel('Sepal_Length')
plt.ylabel('count')
plt.show()

sns.distplot(f["sepal_width"], color= "blue")
plt.title('Histogram - Sepal Width of All Species')
plt.xlabel('Sepal_Width')
plt.ylabel('count')
plt.show()

sns.distplot(f["petal_length"], color= "orange")
plt.title('Histogram - Petal Length of All Species')
plt.xlabel('Petal_Length')
plt.ylabel('count')
plt.show()

sns.distplot(f["petal_width"], color= "red")
plt.title('Histogram - Petal Width of All Species')
plt.xlabel('Petal_Width')
plt.ylabel('count')
plt.show()