# %%
import pandas as pd   # In particular, Pandas is used for pre processing
#from sklearn.impute import SimpleImputer # It has a impute module which has simple imputer. Simple imputer is a class that basically performs imputation. For example, if I want to replace particular missing value in a column with, for example, the mean value of the remaining values in the column, those operations we can do. 
import numpy as np

# %%
# CREATE a simple datafraome(it is structure in a tabluar format) with some missing values
df=pd.DataFrame({
    'A' : [1, 2, np.nan, 4, 5],
    'B' : [np.nan, 2, 3, 4, 5],
    'C' : [1, 2, 3, np.nan, np.nan]
})

# %%
df

# %%
pip install scikit-learn


# %%
conda env list
echo $CONDA_DEFAULT_ENV


# %%
conda activate python
pip install scikit-learn

# %%
pip show scikit-learn


# %%


from sklearn.impute import SimpleImputer # type: ignore

# Now in above column 'A' we can take avg of available values...
# Create an instance of SimpleImputer with mean strategy
imputer = SimpleImputer(missing_values=np.nan, strategy='mean')

# %%
#Perform the imputation on the dataframe
df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)

df_imputed

#Here we have replaced Nan values with mean values from the cloumn values.


