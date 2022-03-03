import pandas as pd


titanic = pd.read_csv("data/titanic.csv")
# print(titanic.head())

'''
HOW TO SELECT A SUBSET OF THE DATAFRAME.
'''


'''
1. Select specific Columns from a DataFrame
1a. Intrested in the --Age-- Series of the DataFrame.
'''
# ages = titanic["Age"]
# print(ages.head())
# print(type(ages.head())) # Result is a pandas Series

''' Lets see the shape of the output'''
# print(ages.shape) # (891,)


'''
1b. Intrested in the --Age-- and --Sex-- Series of the titanic passengers DataFrame
'''
# age_sex = titanic[["Age", "Sex"]]
# print(age_sex)
# print(type(age_sex)) # Result is a pandas DataFrame
# print(age_sex.shape) # (891, 2)

'''
2. Filter specific Columns from a DataFrame
2b. Interested in the passengers older than 35 years.
'''
# above_35 = titanic[titanic["Age"] > 35]
# print(above_35)
# print(titanic["Age"] > 35) # Gives Series with Boolean values (True or False).
# print(above_35.shape) # (217, 12)


'''
2b. Interested in the Titanic passengers from cabin class 2 and 3.
'''
# class_23 = titanic[titanic["Pclass"].isin([2, 3])]
# print(class_23)
''' code above is same as below '''
# class_23_ = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
# print(class_23_)
''' More Row filtering'''
# class_1_above_35 = titanic[(titanic["Pclass"] == 1) & (titanic["Age"] > 35)]
# print(class_1_above_35)
''' Use .notna to filter out row values that are not Null'''
# age_no_na = titanic[titanic["Age"].notna()]
# print(age_no_na)
# print(age_no_na.shape)


'''
2c. Interested in the names of the passengers older than 35 years
'''
# above_35_names = titanic.loc[titanic["Age"] > 35, "Name"]
# print(above_35_names.head())

'''
Note: When using the column names, row labels or a condition expression,
use the loc operator in front of the selection brackets [].
For both the part before and after the comma, you can use a single label,
a list of labels, a slice of labels, a conditional expression or a colon.
Using a colon specifies you want to select all rows or columns.
'''

'''
2d. Interested in rows 10 till 25 and columns 3 to 5.
Passing slices with --iloc-- for row and columns.
'''
# print(titanic.iloc[9:25, 2:5])
# print(titanic.iloc[9:25, :]) # Same but with all columns

'''
2e. Assign a value as an entry in a row
'''
titanic.iloc[0:3, 3] = "anonymous"
print(titanic.head())



'''
REMEMBER
When selecting subsets of data, square brackets [] are used.

Inside these brackets, you can use a single column/row label, a list of column/row labels, a slice of labels, a conditional expression or a colon.

Select specific rows and/or columns using loc when using the row and column names

Select specific rows and/or columns using iloc when using the positions in the table

You can assign new values to a selection based on loc/iloc.
type property still works on pandas, and this is a type - Series.
'''

