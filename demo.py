import csv
import yaml
import pandas as pd
csv_file = r'C:\Users\Rakesh\Desktop\Industry_Ready_Project\sensor-fault-detection\artifact\02_17_2023_15_48_09\data_ingestion\feature_store\sensor.csv'
#df = pd.read_csv(csv_file = r'C:\Users\Rakesh\Desktop\Industry_Ready_Project\sensor-fault-detection\artifact\02_17_2023_15_48_09\data_ingestion\feature_store\sensor.csv')
schema = []

# read the first row of the CSV file to get column names
with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    headers = next(reader)

# create a dictionary for each column and add it to the schema list
for header in headers:
    column_schema = {}
    column_schema['name'] = header.strip()
    if header == 'class':
        column_schema['class'] = 'category'
    else:
        column_schema['class'] = 'int'
    schema.append(column_schema)

# write the schema to a YAML file
with open('schema.yaml', 'w') as f:
    yaml.dump(schema, f)

