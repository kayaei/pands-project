# Project 2019

## Analysis of Fisher's Iris Data Set

### Author: Etem Kaya

### Institution: GMIT Ireland

### Course: Higher Diploma in Data Analytics

### Module: Programming & Scripting

### Year and Semester: 2019 - 01

### Software and Version: Python - Version 3.7

This repository contains my research, investigation and exploration of the Fisher's Iris Dataset along withy my analysis using Python programming language required for Project 2019, "Programming and Scripting" at GMIT.

See this link for the instructions: <https://github.com/kayaei/pands-project/blob/master/project.pdf>.

## How To Download This Repository

1. Go to my repository at [GitHub](https://github.com/kayaei/pands-project).
2. Click the download button to download it.

## How To Run The Code

1. First install the Python (recommended to install it through Anaconda as it comes with some of the built in libraries).
2. Install the Visual Studio Code.
3. Install a command line interpreter (Cmder is recommended but others can also be used).
4. Install the necessary Python libraries e.g. 'Pandas, Matplotlib, Numpy, Seaborn etc.) as required.

## 1. Introduction

### 1.1. Iris Dataset

The Iris flower data set is a multivariate data set introduced by the British statistician and biologist Ronald Fisher in his 1936 paper. Ronald Fisher  (17 February 1890 – 29 July 1962) was a British statistician and geneticist. For his work in statistics, he has been described as "a genius who almost single-handedly created the foundations for modern statistical science".

This dataset is by far one of the best known and commonly used datasets in the Data Science as it is very famous and widely used by everyone trying to learn machine learning and statistics. It is sometimes called Anderson's Iris data set because Edgar Anderson collected the data to quantify the morphologic variation of Iris flowers of three related species.

The dataset consists of 50 samples from each of three species of Iris ([Setosa](https://github.com/kayaei/pands-project/blob/master/iris_setosa.jpg), [Versicolor](https://github.com/kayaei/pands-project/blob/master/iris_versicolor.jpg) and [Virginica](https://github.com/kayaei/pands-project/blob/master/iris_virginica.jpg)). 

Four features were measured from each sample: the length and the width of the [Sepals and Petals](https://github.com/kayaei/pands-project/blob/master/iris_petal-sepal.jpg), in centimeters. The fifth column is the species names of the flower observed. Based on the combination of these four features, Fisher developed a linear discriminant model to distinguish the species from each other, and based on Fisher's linear discriminant model, this data set became a typical test case for many statistical classification techniques in machine learning.
For more information on this dataset, refer to [Wikipedia](https://en.wikipedia.org/wiki/Iris_flower_data_set).

Iris Flower Species;

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_flower.jpg "Iris Flower Species")
![alt text](https://github.com/kayaei/pands-project/blob/master/iris_petal-sepal.jpg "Iris Flower Sepal and Petal")

### 1.2. Objectives

The objective of this project is to research and explore Fisher's Iris Dataset and write Python code to analyse the dataset, and finally summarise it with our findings and conclusion.

## 2.  Research and Analysis of Iris Dataset

### 2.1.  Analysis of Iris Dataset

#### 2.1.1.   Pyton Libraries

In my Iris Dataset analysis, I used the following libraries;

##### Pandas

The Panda is a very useful library when analyzing data with Python and is one of the most widely used packaged in data science. The pandas is a library and used for importing labelled data such as the iris data set. It makes data such as csv files much easier to work with as it will take in a a csv file and creates a python object. It is an open source. Further information can be found at the <http://pandas.pydata.org/>.

##### Numpy

The NumPy is a fundamental package for scientific computation in python. It is particularly useful as a container for multidimensional data which makes NumPy arrays easy to work with, so it is much faster and easier to manipulate the NumPy arrays. This allows NumPy to seamlessly integrate with a wide variety of databases. NumPy is particularly useful for importing the dataset as an array (matrix) or list on which various functions could be applied. For more information, refer to <https://docs.scipy.org/doc/numpy/index.html> and <https://www.numpy.org/>.

##### Matplotlib

The Matplotlib python library is used to make charts such as histograms, plots and bar charts. The pyplot module is commonly used to generate some rich histograms graphs from the dataset given. For further information, refer to <https://matplotlib.org/>

##### Seaborn

The Seaborn is a Python visualization library based on matplotlib. It provides a high-level interface for drawing attractive statistical graphics. Further information can be found at <https://seaborn.pydata.org/index.html> and <https://seaborn.pydata.org/generated/seaborn.PairGrid.html#seaborn.PairGrid>.

##### Scikitlearn

Although I didn’t need to use the Scikitlearn, it is a very useful library for carrying out machine learning in python as it contains many machine learning models which may be used to explore data sets. Scikitlearn already has built in code to handle the machine learning analysis of large data sets. Further information can be found at <http://scikit-learn.org/stable/tutorial/basic/tutorial.html>.

#### 2.1.2.  Reading the CSV File

I downloaded the Iris dataset from the <https://gist.github.com/curran/a08a1080b88344b0c8a7> GitHub repository. Once downloaded, I then stored it in a CSV file called 'iris_dataset.csv'. I mostly used the Pandas library to read the content of my 'iris_dataset' csv file by using the (f = pd.read_csv("iris_dataset.csv")) script in my python code and this worked well. In few occasions, I also used the Seaborn library to read the csv file with the (f = sns.load_dataset("iris")) script. This dataset I downloaded already included the column names, so I did not need to write any additional code to add the column names in my python scripts. However, as part of my research, I have found few different ways to add missing column names, but I did not need it in my case anyway. Here are the two examples of my python scripts to read the csv file with Pandas and Seaborn libraries;

```python
# import pandas library
import pandas as pd
# import seaborn library
import seaborn as sns

# load dataset with panda
f = pd.read_csv("iris.csv")

# load dataset with seaborn
f = sns.load_dataset("iris")
```

#### 2.1.3. Summary of the Dataset

I developed the below python script to summarise the Iris Dataset in brief. Here is the 'Summary' python script;

```pyton
# Etem Kaya 31-Mar-2019
# Iris Data Set Project.

# Analysis of Iris Dataset

# Import pandas library
import pandas as pd

# Import dataset with panda
f = pd.read_csv('iris.csv')

print(str(f.info()) + "\n") # information about the dataset
print(str(f.describe()) + "\n") # summary of each species
print(str(f.shape) + "\n") # total row and column count
print(str(f.head()) + "\n") # print first 5 rows
print(str(f.tail()) + "\n") # print last 5 rows
print(str(f.sample(5)) + "\n") # output 5 random rows
print((f.columns), "\n") # column names of the dataset

# adopted from https://stackoverflow.com/a/29530559
print("\n" + str(f.isnull().any()) + "\n") # find any null values

# adopted from https://priagungkhusumanegara.github.io/data/Data_Visualization.html
print(f["species"].value_counts()) # row count in each species
```

The above python script will give a quick snapshot of the following charecteristics of the Iris dataset;

##### Info

A brief information of the entire dataset e.g. name of all columns, total number of rows in each column, datatype in each column, total number of columns, data range and memory usage.

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_information.jpg "Information of the dataset")

##### Description

A statistical summary of each numeric columns e.g. 'column names, row count, mean, min, max, standard deviation, 25%th, 50%th and 75%th percentile' for numeric columns.

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_description.jpg "Description of the dataset")

##### Shape

Dimension of the dataset e.g. the total number of rows and column in the dataset.

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_shape.jpg "Dimension of the dataset")

##### Head

Lists the top 5 rows from the dataset.

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_head.jpg "Top 5 rows of the dataset")

##### Tail

Lists Last 5 rows from the dataset.

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_tail.jpg "Last 5 rows of the dataset")

##### Sample

Lists Random 5 rows from the dataset.

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_sample.jpg "Random 5 rows of the dataset")

##### Columns

Lists the column names of the dataset

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_columns.jpg "Column names of the dataset")

##### IsNull

Finds the null values of the dataset

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_isnull.jpg "Null values of the dataset")

##### Value_Counts

Gives the row count of the dataset

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_row-count.jpg "Row count of the dataset")

#### 2.1.4. Statistics of the dataset

I developed the below python script to statictically deep dive into the Iris dataset. This code will give the following most widely used statictical attributes of the Iris dataset;

##### i. Mean

Mean of each numeric columns (sepal_length, sepal_width, petal_length, petal_width). I used a few different ways to find the mean value of the numeric columns of the dataset. This included 'loc' and 'iloc' methods from the Seaborn library. Here is the 'Mean' python script;

```python
# Etem Kaya 11-Apr-2019
# Iris Data Set Project.
# Analysing Iris Dataset with 'mean, max, min and median' functions

import pandas as pd # import pandas library
import seaborn as sns # import seaborn library

# f = pd.read_csv("iris.csv") # import dataset with panda
f = sns.load_dataset("iris") # this time import dataset with seaborn

# finding mean of each attribute with pandas
print("Finding mean using pandas", "\n")
print("Mean of Sepal Length is", f["sepal_length"].mean())
print("Mean of Sepal Width is", f["sepal_width"].mean())
print("Mean of Petal Length is", f["petal_length"].mean())
print("Mean of Petal Width is", f["petal_width"].mean())
print("\n")

# group the iris dataset by the species category
group = f.groupby("species")

# finding mean of each attribute for all 3 species using group function
print("Finding mean using 'group' function", "\n")

print("Mean of all 3 Species")
print(group.mean())
print("\n")

# finding mean by splitting the dataset with loc function

print("Finding mean of species using 'loc' function", "\n")

print("Mean of Setosa species")
print(f.loc[f["species"]=="setosa"].mean()) # mean of setosa using loc function
print("\n")
print("Mean of Versicolor species")
print(f.loc[f["species"]=="versicolor"].mean()) # mean of versicolor using loc function
print("\n")
print("Mean of Virginica species")
print(f.loc[f["species"]=="virginica"].mean()) # mean of virginica using loc function
print("\n")

# another way of finding mean by splitting the dataset with iloc function
print("Finding mean of species using 'iloc' function", "\n")

print("Mean of Setosa species")
print(f.iloc[0:50].mean()) # mean of setosa using iloc function
print("\n")
print("Mean of Versicolor species")
print(f.iloc[50:100].mean()) # mean of versicolor using iloc function
print("\n")
print("Mean of Virginica species")    
print(f.iloc[100:150].mean()) # mean of virginica using iloc function
```

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_mean.jpg "Mean of the dataset")

##### ii. Statisticals

Statistical summary of the dataset e.g. mean, max, min, mode and median of each numeric colums (sepal_length, sepal_width, petal_length, petal_width). I used a few different ways to find these statistical attributes. Here is the 'Statistical' python script;

```python
# Etem Kaya 11-Apr-2019
# Iris Data Set Project.
# Analysing Iris Dataset with 'mean, max, min, median and mode' functions

import pandas as pd # import pandas library
import seaborn as sns # import seaborn library

# f = pd.read_csv("iris.csv") # import dataset with panda
f = sns.load_dataset("iris") # this time import dataset with seaborn

# finding the mean of each attribute
print("Mean of Sepal Length is", f["sepal_length"].mean())
print("Mean of Sepal Width is", f["sepal_width"].mean())
print("Mean of Petal Length is", f["petal_length"].mean())
print("Mean of Petal Width is", f["petal_width"].mean())
print("\n")

# finding the max value of each attribute
print("Max value of Sepal Length is", f["sepal_length"].max())
print("Max value of Sepal Width is", f["sepal_width"].max())
print("Max value of Petal Length is", f["petal_length"].max())
print("Max value of Petal Width is", f["petal_width"].max())
print("\n")

# finding the min value of each attribute
print("Min value of Sepal Length is", f["sepal_length"].min())
print("Min value of Sepal Width is", f["sepal_width"].min())
print("Min value of Petal Length is", f["petal_length"].min())
print("Min value of Petal Width is", f["petal_width"].min())
print("\n")

# finding the median of each attribute
print("Median of Sepal Length is", f["sepal_length"].median())
print("Median of Sepal Width is", f["sepal_width"].median())
print("Median of Petal Length is", f["petal_length"].median())
print("Median of Petal Width is", f["petal_width"].median())
print("\n")

# finding the mode of each attribute
print("Mode of Sepal Length is", f["sepal_length"].mode())
print("\n")
print("Mode of Sepal Width is", f["sepal_width"].mode())
print("\n")
print("Mode of Petal Length is", f["petal_length"].mode())
print("\n")
print("Mode of Petal Width is", f["petal_width"].mode())
print("\n")

# group the iris dataset by the species column
group = f.groupby("species")

# find the mean of each attribute for all 3 species
print("Mean of all 3 Species")
print(group.mean())
print("\n")

# find the max value of each attribute for all 3 species
print("Max value of all 3 Species")
print(group.max())
print("\n")

# find the min value of each attribute for all 3 species
print("Min value of all 3 Species")
print(group.min())
print("\n")

# find the median of each attribute for all 3 species
print("Median of all 3 Species")
print(group.median())
print("\n")
```

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_statistical.jpg "Statistical of the dataset")

##### iii. Pivot and Describe

Similiar to above statistical summary of the dataset with few more attributes e.g. 'row count, mean, standard deviation, min, max, 25%th, 50%th and 75%th percentiles' of each numeric colums (sepal_length, sepal_width, petal_length, petal_width) as well as each species. I used the 'Pivot and Describe' methods from the Seaborn library to find the above statistical attributes. Here is the 'Pivot and Describe' python script;

```python
# Etem Kaya 11-Apr-2019
# Iris Data Set Project.
# Analyse Iris Dataset with 'pivot and describe' methods

import pandas as pd # import pandas library
import seaborn as sns # import seaborn library
import numpy as np

# f = pd.read_csv("iris.csv") # import dataset with panda
f = sns.load_dataset("iris") # this time import dataset with seaborn

# pivoting the dataset with describe method based on the species column
print("Pivot the dataframe based on the values in the 'sepal_length' column", "\n")
print(f.pivot(columns='species', values='sepal_length').describe(), "\n")
print("Pivot the dataframe based on the values in the 'sepal_width' column", "\n")
print(f.pivot(columns='species', values='sepal_width').describe(), "\n")
print("Pivot the dataframe based on the values in the 'petal_length' column", "\n")
print(f.pivot(columns='species', values='petal_length').describe(), "\n")
print("Pivot the dataframe based on the values in the 'petal_width' column", "\n")
print(f.pivot(columns='species', values='petal_width').describe(), "\n")
print("Pivot the dataframe based on the values in the 'species' column", "\n")
print(f.pivot(columns='species', values='species').describe(), "\n")

# describe entire dataset for all species
print("Describe the entire dataframe", "\n")
print(f.describe(), "\n")
```

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_describe.jpg "Pivot and Describe of the dataset")

### 2.2.   Visulasation of Iris Dataset

#### 2.2.1.  Scatter Plots

#### 2.2.2.  Box Plots

I used the Boxplot method to plot the dataset and analyse it whether it is symmetric or skewed to the left or right. As we know from Data Analytics, a Boxplot is the visual representation of the statistical five number summary of a given data set. The five number summary includes;

1. Min
2. First Quartile
3. Median (Second Quartile)
4. Third Quartile
5. Max
In a boxplot, the symmetric dataset shows the median roughly in the middle of the box. The median is generally shown by a solid line that cuts through the box in the boxplot. If the dataset is skewed, it shows a lopsided boxplot where the median cuts the box into two unequal pieces. If the longer part of the box is to the right (or above) the median, the data is said to be skewed right. If the longer part is to the left (or below) the median, the data is skewed left.

The following are the 3 Boxplots that I generated for this project using Python;

##### i. Boxplot All Species

The purpose of this to boxplot the entire dataset concidering all 3 species *Setosa, Versicolor and Virginica* treated as one dataset with all 4 attributes *Sepal_length, Sepal_Width, Petal_length, Petal_Width* so all 4 boxplots is shown in a single graph. Here is the *Boxplot-All-Species* python script;

```python
# Etem Kaya 08-Apr-2019
# Iris Data Set Project.

# Boxplot iris dataset
# import pandas, seaborn and matplotlib libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import iris dataset with Pandas
f = pd.read_csv("iris.csv")

# set the boxplot graph for iris flower species
plt.figure(figsize = (10, 8)) # set the graph size
plt.title("Iris Flower Species BoxPlot") # title of the plot

# set the boxplot style
sns.set(style="darkgrid", color_codes=True) # set the background colour
sns.boxplot(data=f) # set the dataset to plot     

# plot the data
plt.show()
```

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_boxplot-all-species.jpg "Boxplot-All-Species")

##### ii. Boxplot Grouped

The purpose of this to boxplot Iris dataset on 4 different graphs based on the 3 Iris flower species *Setosa, Versicolor and Virnigica* treated seperately with all 4 attributes *Sepal_length, Sepal_Width, Petal_length, Petal_Width*. This results in having 4 seperate graphs with each containing 3 boxplots so a total of 12 individual boxplots altogether. Here is the *Boxplot-Grouped* python script;

```python
# Etem Kaya 09-Apr-2019
# Iris Data Set Project.

# Boxplot iris dataset
# import pandas and seaborn libraries
import pandas as pd
import seaborn as sns

# set style and colour using seaborn library
sns.set(style="darkgrid", color_codes=True)

# import iris dataset with Pandas
f = pd.read_csv("iris.csv")

# boxplot grouped by species
f.boxplot(by='species',figsize=(12,8))
```

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_boxplot-group-all-species.jpg "Boxplot-Grouped")

##### iii. Boxplot Sepal

The purpose of this to boxplot the Iris dataset on 2 different graphs based on the 3 Iris flower species *Setosa, Versicolor and Virnigica*, treated seperately based on *Sepal* attribute only with its 2 sub-attributes *Sepal_length and Sepal_Width*. This results in having 2 seperate graphs with each containing 3 boxplots so a total of 6 individual boxplots altogether. Here is the *Boxplot-Sepal* python script;

```python
# Etem Kaya 09-Apr-2019
# Iris Data Set Project.

# import pandas, seaborn and matplotlib libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# set style and colour using seaborn library
sns.set(style="ticks", color_codes=True)

# import iris dataset with Pandas
f = pd.read_csv("iris.csv")

# boxplot sepal lenght
sns.boxplot(x="species", y="sepal_length", data=f)
plt.show()

# boxplot sepal width
sns.boxplot(x="species", y="sepal_width", data=f)
plt.show()
```

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_boxplot-sepal.jpg "Boxplot-Sepal")

##### iiii. Boxplot Petal

The purpose of this to boxplot the Iris dataset on 2 different graphs based on the 3 Iris flower species *Setosa, Versicolor and Virnigica* treated seperately based on *Petal* attribute only with its 2 sub-attributes *Petal_length and Petal_Width*. This results in having 2 seperate graphs with each containing 3 boxplots so a total of 6 individual boxplots altogether. Here is the *Boxplot-Petal* python script;

```python
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
```

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_boxplot-petal.jpg "Boxplot-Petal")

#### 2.2.3.  Histograms

I used the Histogram method to graphically summarize and display the distribution of the Iris data set. As we know from Data Analytics, a histogram  is a vertical bar chart that depicts the distribution of a set of data and can be constructed by segmenting the range of the data into equal sized bins (e.g. segments, groups or classes). The vertical axis of the histogram is labeled "Count or Frequency" and indicates how many times the event occurred (the number of counts for each bin).

On the other hand ,the horizontal axis of the histogram is labeled with the range of the numerical variables from our dataset. We then determine the number of data points that reside within each bin and that is how we construct the histogram chart. We used the histogram when we want to;
• Summarize large data sets graphically
• Compare measurements with specifications
• Communicate information graphically
• Assist in decision making

The following are the 3 types Histograms that I generated for this project using Python;

##### i. Histogram All Species

The purpose of this Histogram is to present the entire dataset concidering all 3 species *Setosa, Versicolor and Virginica* treated as one dataset with its 4 different attributes *Sepal_length, Sepal_Width, Petal_length, Petal_Width*, so each attribute is shown in a sperate histogram so a total of 4 histograms altogether. Here is the *Histogram-All-Species* python script;

```python
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
```

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_histogram-all-species.jpg "Histogram-All-Species")

##### ii. Histogram Grouped

The purpose of this Histogram is to present the entire dataset concidering all 3 species *Setosa, Versicolor and Virginica* treated as one dataset with all 4 attributes *Sepal_length, Sepal_Width, Petal_length, Petal_Width*, so each attribute is being the X axis in each histogram shown so a total of 4 histograms all grouped together and shown in a single graph. Here is the *Histogram-Grouped* python script;

```python
# Etem Kaya 11-Apr-2019
# Iris Data Set Project.
# Group Histogram graphs of Iris Dataset

# import pandas, seaborn and matplotlib libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import dataset with pandas
f = pd.read_csv("iris.csv")

# set the backround colur of the histogram graph
sns.set(style="whitegrid")

# set the bar colour, figure size and bin size of the graphs
f.hist(color = "green", figsize = (12, 8), bins = 18)
# plot the graph
plt.show()
```

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_histogram-group-all-species.jpg "Histogram-Grouped")

##### iii. Histogram Sepal

The purpose of this Histogram is to present each Iris species *Setosa, Versicolor and Virginica* seperately with each species having its own histogram so 3 histograms shown together. The variable of the histogram on the X axis is the *Sepal* attribute of the dataset. Since the *Sepal* has 2 sub-attributes *Sepal_Length* and *Sepal_Width*, the X axis of each graph is *Sepal_Length* and *Sepal_Width* respectively. So there are 2 seperate graphs with each showing 3 histograms one for each species of Iris flower dataset so a total of 6 histograms. Here is the *Histogram-Sepal* python script;

```python
# Etem Kaya 12-Apr-2019
# Iris Data Set Project.

# Histogram of Iris dataset Sepal length and width

# import pandas, seaborn and matplotlib libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import iris dataset with Pandas
f = pd.read_csv("iris.csv")

# split 'Setosa, Versicolor and Virginica' dataset from the entire Iris dataset
Setosa = f.loc[f["species"]=="setosa"]
Versicolor = f.loc[f["species"]=="versicolor"]
Virginica = f.loc[f["species"]=="virginica"]

# set style and background colour using seaborn library
sns.set(style="darkgrid")

# Histogram of 'Setosa, Versicolor and Virginica' Sepal Length
sns.distplot(Setosa["sepal_length"], color= "green")
sns.distplot(Versicolor["sepal_length"], color= "blue")
sns.distplot(Virginica["sepal_length"], color= "orange")
plt.title("Histogram - Sepal Length of 'Setosa, Versicolor and Virginica'")
plt.xlabel('Sepal_Length' + "\nSetosa, Versicolor and Virginica")
plt.ylabel('count')
plt.show()

# Histogram of 'Setosa, Versicolor and Virginica' Sepal Width
sns.distplot(Setosa["sepal_width"], color= "green")
sns.distplot(Versicolor["sepal_width"], color= "blue")
sns.distplot(Virginica["sepal_width"], color= "orange")
plt.title("Histogram - Sepal Width of 'Setosa, Versicolor and Virginica'")
plt.xlabel('Sepal_Width' + "\nSetosa, Versicolor and Virginica")
plt.ylabel('count')
plt.show()
```

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_histogram-sepal.jpg "Histogram-Sepal")

##### iiii. Histogram Petal

The purpose of this Histogram is to present each Iris species *Setosa, Versicolor and Virginica* seperately with each species having its own histogram so 3 histograms shown together. The variable of the histogram on the X axis is the *Petal* attribute of the dataset. Since the *Petal* has 2 sub-attributes *Petal_Length* and *Petal_Width*), the X axis of each graph is *Petal_Length* and *Petal_Width* respectively. So there are 2 seperate graphs with each showing 3 histograms one for each species of Iris flower dataset so a total of 6 histograms. Here is the *Histogram-Petal* python script;

```python
# Etem Kaya 12-Apr-2019
# Iris Data Set Project.

# Histogram of Iris dataset Petal length and width

# import pandas, seaborn and matplotlib libraries
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# import iris dataset with Pandas
f = pd.read_csv("iris.csv")

# split Setosa, Versicolor and Virginica dataset from the entire Iris dataset
Setosa = f.loc[f["species"]=="setosa"]
Versicolor = f.loc[f["species"]=="versicolor"]
Virginica = f.loc[f["species"]=="virginica"]

# set style and background colour using seaborn library
sns.set(style="darkgrid")

# Histogram of 'Setosa, Versicolor and Virginica' Petal Length
sns.distplot(Setosa["petal_length"], color= "green")
sns.distplot(Versicolor["petal_length"], color= "blue")
sns.distplot(Virginica["petal_length"], color= "orange")
plt.title("Histogram - Petal Length of 'Setosa, Versicolor and Virginica'")
plt.xlabel('Petal_Length' + "\nSetosa, Versicolor and Virginica")
plt.ylabel('count')
plt.show()

# Histogram of 'Setosa, Versicolor and Virginica' Petal Width
sns.distplot(Setosa["petal_width"], color= "green")
sns.distplot(Versicolor["petal_width"], color= "blue")
sns.distplot(Virginica["petal_width"], color= "orange")
plt.title("Histogram - Petal Width of 'Setosa, Versicolor and Virginica'")
plt.xlabel('Petal_Width' + "\nSetosa, Versicolor and Virginica")
plt.ylabel('count')
plt.show()
```

![alt text](https://github.com/kayaei/pands-project/blob/master/iris_histogram-petal.jpg "Histogram-Petal")

## 3  References

1. Iris Flower Data set - <https://en.wikipedia.org/wiki/Iris_flower_data_set>
2. Iris setosa photo - <https://en.wikipedia.org/wiki/Iris_setosa#/media/File:Kosaciec_szczecinkowaty_Iris_setosa.jpg>
3. Iris versicolor photo - <https://en.wikipedia.org/wiki/Iris_versicolor#/media/File:Blue_Flag,_Ottawa.jpg>
4. Iris virginica photo - <https://en.wikipedia.org/wiki/Iris_virginica#/media/File:Iris_virginica_2.jpg>
5. Iris setosa species - <https://en.wikipedia.org/wiki/Iris_setosa>
6. Iris versicolor species - <https://en.wikipedia.org/wiki/Iris_versicolor>
7. Iris virginica species - <https://en.wikipedia.org/wiki/Iris_virginica>
8. Iris Flower Data set '.csv' file - <https://gist.github.com/curran/a08a1080b88344b0c8a7>
9. UCI Machine Learning Repository - <https://archive.ics.uci.edu/ml/datasets/iris>
10. <https://www.kaggle.com/uciml/iris>
11. <https://www.kaggle.com/jchen2186/machine-learning-with-iris-dataset>
12. <https://www.ritchieng.com/machine-learning-iris-dataset/>
13. <https://stackoverflow.com/a/29530559>
14. <https://priagungkhusumanegara.github.io/data/Data_Visualization.html>
15. <https://machinelearningmastery.com/machine-learning-in-python-step-by-step/>
