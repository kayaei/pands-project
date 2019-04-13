#%%
# Etem Kaya 12-Apr-2019
# Iris Data Set Project.

# Histogram of Iris Virginica flower type

# import pandas, seaborn and matplotlib libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import iris dataset with Pandas
f = pd.read_csv("iris.csv")

# Split Virginica dataset from the entire Iris dataset
Virginica = f.loc[f["species"]=="virginica"]

# set style and background colour using seaborn library
sns.set(style="whitegrid")

# Histogram of Virginica 'Sepal Length'
sns.distplot(Virginica["sepal_length"], color= "green")
plt.title('Histogram - Sepal Length of Virginica')
plt.xlabel('Virginica Sepal Length')
plt.ylabel('count')
plt.show()

# Histogram of Virginica 'Sepal Width'
sns.distplot(Virginica["sepal_width"], color= "blue")
plt.title('Histogram - Sepal Width of Virginica')
plt.xlabel('Virginica Sepal Width')
plt.ylabel('count')
plt.show()

# Histogram of Virginica 'Petal Length'
sns.distplot(Virginica["petal_length"], color= "orange")
plt.title('Histogram - Petal Length of Virginica')
plt.xlabel('Virginica Petal Length')
plt.ylabel('count')
plt.show()

# Histogram of Virginica 'Petal Width'
sns.distplot(Virginica["petal_width"], color= "red")
plt.title('Histogram - Petal Width of Virginica')
plt.xlabel('Virginica Petal Width')
plt.ylabel('count')
plt.show()

# Histogram of Virginica 'Sepal Length and Sepal Width'
sns.distplot(Virginica["sepal_length"], color= "green")
sns.distplot(Virginica["sepal_width"], color= "blue")
plt.title('Histogram - Virginica Sepal Length and Width')
plt.xlabel('Virginica Sepal Length and Width')
plt.ylabel('count')
plt.show()

# Histogram of Virginica 'Petal Length and Petal Width'
sns.distplot(Virginica["petal_length"], color= "orange")
sns.distplot(Virginica["petal_width"], color= "red")
plt.title('Histogram - Virginica Petal Length and Width')
plt.xlabel('Virginica Petal Length and Width')
plt.ylabel('count')
plt.show()