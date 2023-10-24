## Lecture 5 Script

#S1
# Importing libraries
import numpy as np
import pandas as pd
from pandas import DataFrame # we use DataFrame a lot, so let's import it directly

# Creating a DataFrame
data = {"state": ["Ohio", "Ohio", "Ohio", "Nevada", "Nevada", "Nevada"],
        "year": [2000, 2001, 2002, 2001, 2002, 2003],
        "pop": [1.5, 1.7, 3.6, 2.4, 2.9, 3.2]}
frame = pd.DataFrame(data)
frame

#S2
# Observe the first 5 rows
frame.head()

# Observe the last 5 rows
frame.tail()

#S3
# Order the columns
pd.DataFrame(data, columns=["year", "state", "pop"])

# Create a new column
frame2 = pd.DataFrame(data, columns=["year", "state", "pop", "debt"])
frame2
frame2.columns # get the column names

#S4
# Get a column
frame2["state"]
frame2.year

# Get a row
frame2.loc[1]
frame2.iloc[2]

#S5
# Modify a column
frame2["debt"] = 16.5
frame2

frame2["debt"] = np.arange(6.) 

val = pd.Series([-1.2, -1.5, -1.7], index=[2, 4, 5])
frame2["debt"] = val
frame2

#S6
# Delete a column
frame2["eastern"] = frame2["state"] == "Ohio"
frame2

del frame2["eastern"]
frame2.columns

#S7
# Create a DataFrame from a nested dict of dicts
populations = {"Nevada": {2001: 2.4, 2002: 2.9},
       "Ohio": {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame3 = pd.DataFrame(populations)
frame3

# Transpose the DataFrame
frame3.T

#S8
# Recall frame3
frame3
frame3.columns
# Indexing
"Ohio" in frame3.columns
2003 in frame3.index

#S9
# Create a DataFrame from a dict of Series
frame = pd.DataFrame(np.arange(9).reshape((3, 3)),
   index=["a", "c", "d"],
   columns=["Ohio", "Texas", "California"])
frame

# Row reindexing
frame2 = frame.reindex(index=["a", "b", "c", "d"])
frame2

# Columns can be reindexed with the columns keyword
states = ["Texas", "Utah", "California"]
frame.reindex(columns=states)
# Another way to do it
frame.reindex(states, axis="columns")

#S10
# Dropping entries from an axis
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
   index=["Ohio", "Colorado", "Utah", "New York"],
   columns=["one", "two", "three", "four"])
data

# Drop rows
data.drop(index=["Colorado", "Ohio"])
# Drop columns
data.drop(columns=["two"])
# 
data.drop("two", axis=1)
data.drop(["two", "four"], axis="columns")

#S11
# Indexing, selection, and filtering
data = pd.DataFrame(np.arange(16).reshape((4, 4)),
   index=["Ohio", "Colorado", "Utah", "New York"],
   columns=["one", "two", "three", "four"])
data

data["two"] # get a column
data[["three", "one"]] # get multiple columns
data[:2] # get the first two rows
data[data["three"] > 5] # get rows where the value in column "three" is greater than 5
data < 5 # get a boolean DataFrame
data[data < 5] = 0 # set values less than 5 to 0
data

#S12
# Selecting with loc and iloc
data.loc["Colorado"]
data.loc["Colorado", ["two", "three"]]
data.iloc[2, [3, 0, 1]]
data.iloc[2]
data.iloc[[1, 2], [3, 0, 1]]
data.loc[: "Utah", "two"]
data.iloc[:, :3][data.three > 5]
data.loc[data.three >= 2]

#S13
# Arithmetic and data alignment
df1 = pd.DataFrame(np.arange(9.).reshape((3, 3)), columns=list("bcd"),
   index=["Ohio", "Texas", "Colorado"])

df2 = pd.DataFrame(np.arange(12.).reshape((4, 3)), columns=list("bde"),
   index=["Utah", "Ohio", "Texas", "Oregon"])

df1
df2

# Add two DataFrames
df1 + df2

#S14
# Arithmetic methods with fill values
df1 = pd.DataFrame(np.arange(12.).reshape((3, 4)), columns=list("abcd"))
df2 = pd.DataFrame(np.arange(20.).reshape((4, 5)), columns=list("abcde"))

df2.loc[1, "b"] = np.nan # add a missing value

df1 + df2

# Fill missing values with 0
df1.add(df2, fill_value=0)

#S15
# Function application and mapping
frame = pd.DataFrame(np.random.standard_normal((4, 3)),
   columns=list("bde"),
   index=["Utah", "Ohio", "Texas", "Oregon"])

frame

np.abs(frame) # apply a function to each column

def f1(x):
   return x.max() - x.min() # define a function

frame.apply(f1) # apply the function to each column
frame.apply(f1, axis="columns") # apply the function to each row

def f2(x):
   return pd.Series([x.min(), x.max()], index=["min", "max"]) # define a function

frame.apply(f2)

#S16
# Sorting and ranking
frame = pd.DataFrame(np.arange(8).reshape((2, 4)),
   index=["three", "one"],
   columns=["d", "a", "b", "c"])
frame

frame.sort_index() # sort by row index
frame.sort_index(axis="columns") # sort by columns
frame.sort_index(axis="columns", ascending=False) # sort by columns in descending order

#S17
# Ranking
frame = pd.DataFrame({"b": [4.3, 7, -3, 2], "a": [0, 1, 0, 1],
   "c": [-2, 5, 8, -2.5]})
frame

frame.rank() # rank by row
frame.rank(axis="columns") # rank by column

#S18
# Summarizing and computing descriptive statistics
df = pd.DataFrame([[1.4, np.nan], [7.1, -4.5],
   [np.nan, np.nan], [0.75, -1.3]],
   index=["a", "b", "c", "d"],
   columns=["one", "two"])
df

df.sum() # sum by column
df.sum(axis="columns") # sum by row
df.mean(axis="columns", skipna=False) # mean by row, including missing values
df.idxmax() # get the index of the maximum value in each column
df.cumsum() # cumulative sum by column
df.describe() # get summary statistics



