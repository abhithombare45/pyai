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
