import pandas as pd
import numpy as np

filepath = "https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMDeveloperSkillsNetwork-DA0101EN-Coursera/laptop_pricing_dataset_mod1.csv"
df = pd.read_csv(filepath, header=None)

# setting first row as header
df.columns = df.iloc[0]
# dropping 1st row
df = df[1:].reset_index(drop=True)
df = df.drop(df.columns[0], axis=True)

df.tail(50)
df.info()

df[["Screen_Size_cm", "CPU_frequency", "Weight_kg"]] = df[["bore", "stroke"]].astype(
    "float"
)
df[["Category", "Price", "GPU", "OS", "CPU_core", "Storage_GB_SSD", "RAM_GB"]] = df[
    ["normalized-losses"]
].astype("int")
df[["price"]] = df[["price"]].astype("float")
df[["peak-rpm"]] = df[["peak-rpm"]].astype("float")

df[["Screen_Size_cm"]] = np.round(df["Screen_Size_cm"], 2)
