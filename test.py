from sensor.Data_access.sensor_data import SensorData

# create an instance of the SensorData class
sensor_data = SensorData()

# set the name of the collection you want to export
collection_name = "sensor"

# call the export_collection_as_dataframe method with the appropriate arguments
df = sensor_data.export_collection_as_dataframe(collection_name)

# print the value of database_name and collection_name
print("Database Name:", sensor_data.mongo_client.database_name)
print("Collection Name:", collection_name)

