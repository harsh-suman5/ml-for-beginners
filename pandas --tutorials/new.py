import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

#creating a series by passing a list of values

data = pd.Series([1,3,5,np.nan, 6, 8]) # pd.series is used for 1-d array data structures
print(data)

#creating a dataframe by passing a numpy array with
#a determined idex using date_range

dates= pd.date_range("20250501", periods=7)
print(dates)
df = pd.DataFrame(np.random.randn(7,4), index=dates, columns=list("ABCD"))
print(df)
#dataframe is used for 2d array data structures

df2  =  pd.DataFrame({
    "A":1.0,
    "B":pd.Timestamp("20250501"),
    "C":pd.Series(1, index=list(range(4)), dtype="float32"),
    "D":np.array([3] * 4, dtype = "int32"),
    "E":pd.Categorical(["test", "train", "test", "train"]),
    "F":"foo",

})
print(df2)  
print(df2.dtypes)

# viewing data
data = df.head()
print(data) 
print(df.tail())

#display the dataframe.index or dataframe.column
print(df.index)
print(df.columns)

print(df.to_numpy())
print(df.to_csv)

print(df.describe())

print(df.T) #transposing our data

print(df.sort_index(axis=1, ascending=False)) #sort by an axis
print(df.sort_values(by="C")) # sort by value

#dataframe.at(), dataframe.iat, datafrrame.loc() and dataframe.iloc() are used in production codes


print(df.mean(axis=1))




