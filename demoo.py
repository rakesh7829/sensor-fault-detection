import pandas as pd
from pandas.api.types import CategoricalDtype
import yaml

# read in your dataset
df = pd.read_csv(r'C:\Users\Rakesh\Desktop\Industry_Ready_Project\sensor-fault-detection\artifact\02_17_2023_15_48_09\data_ingestion\feature_store\sensor.csv')

# create an empty dictionary to store the schema
schema = {}

# loop through each column in the dataset
for column in df.columns:

    # get the dtype of the column
    dtype = df[column].dtype

    # create a dictionary to store the details of the column
    column_schema = {}

    # check the dtype of the column and update the column_schema dictionary accordingly
    if dtype == 'object':
        column_schema['type'] = 'string'
    elif dtype == 'int64':
        column_schema['type'] = 'integer'
    elif dtype == 'float64':
        column_schema['type'] = 'float'
    elif dtype.name == 'category':
        column_schema['type'] = 'categorical'
        column_schema['categories'] = df[column].astype(CategoricalDtype()).cat.categories.tolist()

    # add the column_schema dictionary to the schema dictionary with the column name as the key
    schema[column] = column_schema

# write the schema to a yaml file
with open('schema.yaml', 'w') as file:
    yaml.dump(schema, file)

