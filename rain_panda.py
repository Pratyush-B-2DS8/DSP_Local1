import pandas as pd
import numpy as np

file ="ds_practice/all-india-monthly-rainfall.csv"

x = pd.read_csv(file, index_col=0)
print (x)
xcols = x.columns
print(x.columns)
#print(xcols[7])
#print(x[xcols[7]])

Jul_mean = x["Jul"].mean()
Jul_std  = x["Jul"].std()
print(Jul_mean, Jul_std)

print(x.index)
print(x.iloc[78,2])
print(x.loc[1984, "Jul"])

#Experiment with slicing
