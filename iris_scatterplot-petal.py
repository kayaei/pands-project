#%%

# Etem Kaya 12-Apr-2019
# Iris Data Set Project.
# Scatterplots for the 'Petal' category of the Iris dataset

# import pandas, seaborn and matplotlib libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import iris dataset with Pandas
f = pd.read_csv("iris.csv")

# split 'Setosa, Versicolor and Virginica' from the entire Iris dataset
Setosa = f.loc[f["species"]=="setosa"]
Versicolor = f.loc[f["species"]=="versicolor"]
Virginica = f.loc[f["species"]=="virginica"]

# set the parameters for the 'Setosa - Petal' scatter plot
ax = sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=Setosa)
# set the title of the scatter plot
plt.title("Scatter Plot - 'Petal Length and Petal Width' of Setosa")
plt.xlabel('petal_length' + "\nSetosa")
plt.show()

# set the parameters for the 'Versicolor - Petal' scatter plot
ax = sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=Versicolor)
# set the title of the scatter plot
plt.title("Scatter Plot - 'Petal Length and Petal Width' of Versicolor")
plt.xlabel('petal_length' + "\nVersicolor")
plt.show()

# set the parameters for the 'Virginica - Petal' scatter plot
ax = sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=Virginica)
# set the title of the scatter plot
plt.title("Scatter Plot - 'Petal Length and Petal Width' of Virginica")
plt.xlabel('petal_length' + "\nVirginica")
plt.show()