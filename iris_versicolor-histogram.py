#%%
# Etem Kaya 12-Apr-2019
# Iris Data Set Project.

# Histogram of Iris Versicolor flower type

# import pandas, seaborn and matplotlib libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import iris dataset with Pandas
f = pd.read_csv("iris.csv")

# Split Versicolor dataset from the entire Iris dataset
Versicolor = f.loc[f["species"]=="versicolor"]

# set style and background colour using seaborn library
sns.set(style="whitegrid")

# Histogram of Versicolor 'Sepal Length'
sns.distplot(Versicolor["sepal_length"], color= "green")
plt.title('Histogram - Sepal Length of Versicolor')
plt.xlabel('Versicolor Sepal Length')
plt.ylabel('count')
plt.show()

# Histogram of Versicolor 'Sepal Width'
sns.distplot(Versicolor["sepal_width"], color= "blue")
plt.title('Histogram - Sepal Width of Versicolor')
plt.xlabel('Versicolor Sepal Width')
plt.ylabel('count')
plt.show()

# Histogram of Versicolor 'Petal Length'
sns.distplot(Versicolor["petal_length"], color= "orange")
plt.title('Histogram - Petal Length of Versicolor')
plt.xlabel('Versicolor Petal Length')
plt.ylabel('count')
plt.show()

# Histogram of Versicolor 'Petal Width'
sns.distplot(Versicolor["petal_width"], color= "red")
plt.title('Histogram - Petal Width of Versicolor')
plt.xlabel('Versicolor Petal Width')
plt.ylabel('count')
plt.show()

# Histogram of Versicolor 'Sepal Length and Sepal Width'
sns.distplot(Versicolor["sepal_length"], color= "green")
sns.distplot(Versicolor["sepal_width"], color= "blue")
plt.title('Histogram - Versicolor Sepal Length and Width')
plt.xlabel('Versicolor Sepal Length and Width')
plt.ylabel('count')
plt.show()

# Histogram of Versicolor 'Petal Length and Petal Width'
sns.distplot(Versicolor["petal_length"], color= "orange")
sns.distplot(Versicolor["petal_width"], color= "red")
plt.title('Histogram - Versicolor Petal Length and Width')
plt.xlabel('Versicolor Petal Length and Width')
plt.ylabel('count')
plt.show()