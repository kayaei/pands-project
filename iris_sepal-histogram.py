#%%
# Etem Kaya 12-Apr-2019
# Iris Data Set Project.

# Histogram of Iris dataset Sepal length and width

# import pandas, seaborn and matplotlib libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import iris dataset with Pandas
f = pd.read_csv("iris.csv")

# Split Setosa, Versicolor and Virginica dataset from the entire Iris dataset
Setosa = f.loc[f["species"]=="setosa"]
Versicolor = f.loc[f["species"]=="versicolor"]
Virginica = f.loc[f["species"]=="virginica"]

# set style and background colour using seaborn library
sns.set(style="darkgrid")

# Histogram of Setosa, Versicolor and Virginica 'sepal Length'
sns.distplot(Setosa["sepal_length"], color= "green")
sns.distplot(Versicolor["sepal_length"], color= "blue")
sns.distplot(Virginica["sepal_length"], color= "orange")
plt.title('Histogram - sepal Length of Setosa, Versicolor and Virginica')
plt.xlabel('sepal_Length' + "\nSetosa, Versicolor and Virginica")
plt.ylabel('count')
plt.show()

# Histogram of Setosa, Versicolor and Virginica 'sepal Width'
sns.distplot(Setosa["sepal_width"], color= "green")
sns.distplot(Versicolor["sepal_width"], color= "blue")
sns.distplot(Virginica["sepal_width"], color= "orange")
plt.title('Histogram - sepal Width of Setosa, Versicolor and Virginica')
plt.xlabel('sepal_Width' + "\nSetosa, Versicolor and Virginica")
plt.ylabel('count')
plt.show()

