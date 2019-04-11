# Etem Kaya 08-Apr-2019
# Iris Data Set Project.

# Print Iris Dataset in Tabular format

# import pandas library
import pandas as pd

# import csv file with pandas
iris = pd.read_csv('iris.csv') 

print(iris) # print the entire dataset

# convert csv file to a dataframe
df = pd.DataFrame(iris) 

print(df) # print the dataframe

