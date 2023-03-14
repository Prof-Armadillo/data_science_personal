import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats



biostats_of_employees = pd.read_csv('biostats.csv', header=0, sep=',', skipinitialspace=True)


#example 1
biostats_of_employees.plot(x = 'Height (in)', y = 'Weight (lbs)', kind = 'scatter')



#Example 2
x = biostats_of_employees['Height (in)']

y = biostats_of_employees['Weight (lbs)']

slope, intercept, r, p, std_err = stats.linregress(x, y)

def myfunc(x):
    return slope * x + intercept

mymodel = list(map(myfunc, x))

plt.scatter(x,y)
plt.plot(x, mymodel)

plt.savefig('example_plot.png')
