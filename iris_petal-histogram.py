#%%
# Etem Kaya 12-Apr-2019
# Iris Data Set Project.

# Histogram of Iris dataset Petal length and width

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

# Histogram of Setosa, Versicolor and Virginica 'Petal Length'
sns.distplot(Setosa["petal_length"], color= "green")
sns.distplot(Versicolor["petal_length"], color= "blue")
sns.distplot(Virginica["petal_length"], color= "orange")
plt.title('Histogram - Petal Length of Setosa, Versicolor and Virginica')
plt.xlabel('Petal_Length' + "\nSetosa, Versicolor and Virginica")
plt.ylabel('count')
plt.show()

# Histogram of Setosa, Versicolor and Virginica 'Petal Width'
sns.distplot(Setosa["petal_width"], color= "green")
sns.distplot(Versicolor["petal_width"], color= "blue")
sns.distplot(Virginica["petal_width"], color= "orange")
plt.title('Histogram - Petal Width of Setosa, Versicolor and Virginica')
plt.xlabel('Petal_Width' + "\nSetosa, Versicolor and Virginica")
plt.ylabel('count')
plt.show()

