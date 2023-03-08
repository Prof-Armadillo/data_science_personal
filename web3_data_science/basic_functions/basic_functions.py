# importing of libraries
import numpy as np
import pandas as pd

# input of dataset using pandas
biostats_of_employees = pd.read_csv('biostats.csv', header=0, sep=',')
# note the blank space before Age was hidden till pasting name
ages = biostats_of_employees[' "Age"']
# get the max value of a data set
max_age = max(ages)
print(max_age)
# get the min value of a data set
min_age = min(ages)
print(min_age)
# using numpy we can calculate an average
mean_age = np.mean(ages)
print(round(mean_age, 0))
# finally we can use the head tool to show the first 5 lines of a dataset 
print(ages.head())
