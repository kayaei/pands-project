#%%

# Etem Kaya 12-Apr-2019
# Iris Data Set Project.
# Scatterplots of Iris Dataset

# import pandas, seaborn and matplotlib libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import iris dataset with Pandas
f = pd.read_csv("iris.csv")

# set the key parameters for the 'Sepal Lenght' scatter plot
ax = sns.scatterplot(x="sepal_length", y="sepal_width", hue="species", data=f)
# set the title of the scatter plot
plt.title("Scatter Plot - 'Sepal Length and Sepal Width' of all 3 species")
plt.show()

# set the key parameters for the 'Sepal Width' scatter plot
ax = sns.scatterplot(x="petal_length", y="petal_width", hue="species", data=f)
# set the title of the scatter plot
plt.title("Scatter Plot - 'Petal Length and Petal Width' of all 3 species")
plt.show()