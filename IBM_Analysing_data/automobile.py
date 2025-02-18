# Internet: https://archive.ics.uci.edu/autos/imports-85.data
import pandas as pd
import numpy as np

url = "https://archive.ics.uci.edu/ml/machine-learning-databases/autos/imports-85.data"

df = pd.read_csv(url, header=None)
# or we need to put below header command aboce and run namesheaders as column name while loading data with column name in it.
# df = pd.read_csv(filename, names = headers)


headers = [
    "symboling",
    "normalized-losses",
    "make",
    "fuel-type",
    "aspiration",
    "num-of-doors",
    "body-style",
    "drive-wheels",
    "engine-location",
    "wheel-base",
    "length",
    "width",
    "height",
    "curb-weight",
    "engine-type",
    "num-of-cylinders",
    "engine-size",
    "fuel-system",
    "bore",
    "stroke",
    "compression-ratio",
    "horsepower",
    "peak-rpm",
    "city-mpg",
    "highway-mpg",
    "price",
]

df.columns = headers
df  # column test

path = "/Users/abhijeetthombare/vscode/IBM_Analysing_data/"
df.to_csv("automobile_modified.csv")

df.describe()
df.describe(include="all")
df.info()

df["symboling"]
df["symboling"].dtype

df_miss = df.replace("?", np.nan)

df.dropna(subset=["price"], axis=0).head(30)
# inplace=True
df.replace("?", np.nan, inplace=True)

missing_data = df.isnull()
missing_data.head(5)

# Count missing values in each column
for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

# "True" means the value is a missing value while "False" means the value is not a missing value.

# Based on the summary above, each column has 205 rows of data and seven of the columns containing missing data:
# <ol>
#     <li>"normalized-losses": 41 missing data</li>
#     <li>"num-of-doors": 2 missing data</li>
#     <li>"bore": 4 missing data</li>
#     <li>"stroke" : 4 missing data</li>
#     <li>"horsepower": 2 missing data</li>
#     <li>"peak-rpm": 2 missing data</li>
#     <li>"price": 4 missing data</li>
# </ol>

avg_norm_loss = df["normalized-losses"].astype("float").mean(axis=0)
print("Average of normalized-losses:", avg_norm_loss)

df["normalized-losses"].replace(np.nan, avg_norm_loss, inplace=True)

avg_bore = df["bore"].astype("float").mean(axis=0)
print("Average of bore:", avg_bore)

df["bore"].replace(np.nan, avg_bore, inplace=True)

df["stroke"].dtype
# Write your code below and press Shift+Enter to execute
mean_stroke = df["stroke"].astype("float").mean(axis=0)
print("Avg of stroke:", mean_stroke)

df["stroke"].replace(np.nan, mean_stroke)
