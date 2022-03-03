import pandas as pd


''' Use read_* methods to read data to pandas '''
titanic = pd.read_csv("data\titanic.csv")

''' view data * '''
# print(titanic)

''' Use *.head(x) to see the first x rows and *.tail(x) for last x rows '''
# print(titanic.head(8))
# print(titanic.tail(8))

''' Use *.dtypes to see the datatype in every column'''
# print(titanic.dtypes)


''' Use to_* methods are used to store data '''
# titanic.to_excel("titanic.xlsx", sheet_name="passengers", index=False)

''' Use read_* methods are get back data '''
# titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")


''' Technical summary of a dataframe. '''
print(titanic.info())


'''
REMEMBER
Getting data in to pandas from many different file formats or data sources is supported by read_* functions.

Exporting data out of pandas is provided by different to_*methods.

The head/tail/info methods and the dtypes attribute are convenient for a first check.
'''
