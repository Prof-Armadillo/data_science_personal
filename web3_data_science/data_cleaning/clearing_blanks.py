import pandas as pd
# when we have a dataset with some blanks if we import them using pandas it will cause NaN values

shoes_size_data = pd.read_csv('Example_Blank_Spaces.csv', header=0, sep=',')

print(shoes_size_data)

#Prints: 
#             Name   Age  Shoe Size Nationality
# 0     John Smith  28.0       10.0    American
# 1   Maria Garcia  35.0        7.0         NaN
# 2         Li Wei   NaN        9.0     Chinese
# 3     Ahmed Khan  19.0       11.0   Pakistani
# 4     Sophie Lee  25.0        NaN      Korean
# 5    Carlos Ruiz  31.0        8.5   Colombian
# 6    Emma Wilson  43.0        7.0     British
# 7      Abdul Ali   NaN       10.5      Indian
# 8            NaN  22.0        8.0         NaN
# 9  Andrei Ivanov  29.0       11.5     Russian

# to deal with these values we can then use a data cleaning technique called dropna
#if we do it in place it affects the existing data set where as else return a new one

#shoes_size_data.dropna(axis = 0, inplace=True)


shoe_sizes_clean = shoes_size_data.dropna(axis = 0, inplace=False)

print(shoe_sizes_clean.info())

print(shoes_size_data)
print(shoe_sizes_clean)
