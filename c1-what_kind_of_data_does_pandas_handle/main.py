import pandas as pd

'''
Use the pd.DataFrame() method to create a pandas dataframe
passing an object as argument with keys representing column headers
and values as arrays representing columns data.
'''
df = pd.DataFrame({
    "Name": ["Braund, Mr. Owen Harris",
            "Allen, Mr. William Henry",
            "Bonnell, Miss. Elizabeth",
    ],
    "Age": [22, 35, 54],
    "Gender": ["male", "male", "female"],
})

''' View dataframe '''
print(df)

''' A column is called a Series and you can access it as 
df["Series-header-name"] '''
# print(df["Name"])

'''Use .dtype attribute to access a series datatype'''
# print(df["Name"].dtype)

''' Creating a Series from scratch '''
# ages = pd.Series([22, 35, 58], name="Age")
# print(ages)



''' DOING SOMETHING ON THE DATAFRAMES AND SERIES '''

''' Get and Show max age of passengers '''
# print(df["Age"].max())

''' Get numerical data from the dataframe.
Note: This only outputs for  series with numerial datatypes (int or floats). '''
# print(df.describe())


'''
REMEMBER
Import the package, aka import pandas as pd

A table of data is stored as a pandas DataFrame

Each column in a DataFrame is a Series

You can do things by applying a method to a DataFrame or Series
'''