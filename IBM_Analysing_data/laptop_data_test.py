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
df.head(50)
df.info()

df[["Screen_Size_cm", "CPU_frequency", "Weight_kg"]] = df[
    ["Screen_Size_cm", "CPU_frequency", "Weight_kg"]
].astype("float")
df[["Category", "Price", "GPU", "OS", "CPU_core", "Storage_GB_SSD", "RAM_GB"]] = df[
    ["Category", "Price", "GPU", "OS", "CPU_core", "Storage_GB_SSD", "RAM_GB"]
].astype("int")


df["Screen_Size_cm"] = np.round(df["Screen_Size_cm"], 2)

df["Screen"].unique()
df["Storage_GB_SSD"].unique()


missing_data = df.isnull()
# missing_data.head(50)


for column in missing_data.columns.values.tolist():
    print(column)
    print(missing_data[column].value_counts())
    print("")

    # Screen_Size_cm
    # Screen_Size_cm
    # False    234
    # True       4
    # Name: count, dtype: int64

    # Weight_kg
    # Weight_kg
    # False    233
    # True       5
    # Name: count, dtype: int64

screen_avg_size = df["Screen_Size_cm"].astype("float").mean(axis=0)
df["Screen_Size_cm"] = np.round(
    df["Screen_Size_cm"].replace(np.nan, screen_avg_size), 2
)

avg_wt = df["Weight_kg"].astype("float").mean(axis=0)
df["Weight_kg"] = np.round(df["Weight_kg"].replace(np.nan, avg_wt), 2)

df.to_csv("./clean_csv_laptop_pricing_dataset.csv")
