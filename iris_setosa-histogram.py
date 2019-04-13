#%%
# Etem Kaya 12-Apr-2019
# Iris Data Set Project.

# Histogram of Iris Setosa flower type

# import pandas, seaborn and matplotlib libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import iris dataset with Pandas
f = pd.read_csv("iris.csv")

# Split Setosa dataset from the entire Iris dataset
Setosa = f.loc[f["species"]=="setosa"]

# set style and background colour using seaborn library
sns.set(style="whitegrid")

# Histogram of Setosa Sepal Length
sns.distplot(Setosa["sepal_length"], color= "green")
plt.title('Histogram - Sepal Length of Setosa')
plt.xlabel('Setosa Sepal Length')
plt.ylabel('count')
plt.show()

# Histogram of Setosa Sepal Width
sns.distplot(Setosa["sepal_width"], color= "blue")
plt.title('Histogram - Sepal Width of Setosa')
plt.xlabel('Setosa Sepal Width')
plt.ylabel('count')
plt.show()

# Histogram of Setosa Petal Length
sns.distplot(Setosa["petal_length"], color= "orange")
plt.title('Histogram - Petal Length of Setosa')
plt.xlabel('Setosa Petal Length')
plt.ylabel('count')
plt.show()

# Histogram of Setosa Petal Width
sns.distplot(Setosa["petal_width"], color= "red")
plt.title('Histogram - Petal Width of Setosa')
plt.xlabel('Setosa Petal Width')
plt.ylabel('count')
plt.show()

# Histogram of Setosa Sepal Length and Sepal Width
sns.distplot(Setosa["sepal_length"], color= "green")
sns.distplot(Setosa["sepal_width"], color= "blue")
plt.title('Histogram - Setosa Sepal Length and Width')
plt.xlabel('Setosa Sepal Length and Width')
plt.ylabel('count')
plt.show()

# Histogram of Setosa Petal Length and Petal Width
sns.distplot(Setosa["petal_length"], color= "orange")
sns.distplot(Setosa["petal_width"], color= "red")
plt.title('Histogram - Setosa Petal Length and Width')
plt.xlabel('Setosa Petal Length and Width')
plt.ylabel('count')
plt.show()