# To work with data frames we generally use pandas
import pandas as pd

# here we are declaring our data into arrays based on the columns.
data_arrays = {'Name': ["Sam", "Mike", "Steve", "Dave"],
               'Sex': ["M", "M", "M", "M"], 'Age': [26, 44, 56, 48]}

# Then we use the DataFrame method of the pd library to frame our data automatically.
data_frame = pd.DataFrame(data=data_arrays)

# We can then visualize the data if we pass it to a print function.
print(data_frame)
# results in:
#     Name Sex  Age
# 0    Sam   M   26
# 1   Mike   M   44
# 2  Steve   M   56
# 3   Dave   M   48

# We can then use the shape method of dataframes to get infomation about our data
count_row = data_frame.shape[0] # Counts the rows when using the 0 argument
count_column = data_frame.shape[1] # Counts the columns when using the 1 argument

print(f'There are {count_row} rows.')
print(f'There are {count_column} columns.')
