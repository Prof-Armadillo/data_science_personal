#Importing modules should be declared on new lines
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

#Once imported we can then use modules by reference
biostats_of_employees = pd.read_csv("biostats.csv", header=0, sep=",")

print(biostats_of_employees)
