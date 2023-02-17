from sensor.entity.config_entity import TrainingPipelineConfig,DataIngestionConfig
#from sensor.pipeline.training_pipeline import TrainPipeline
from sensor.configuration.mongo_db_connection import MongoDBClient
from sensor.exception import SensorException
from sensor.pipeline.training_pipeline import TrainPipeline
import os,sys
from sensor.logger import logging
from datetime import datetime




#def test_exception():
    #try:
  #      x=1/0
    #except Exception as e:
     #   raise SensorException(e,sys)




if __name__=='__main__':
  

  #training_pipeline_config=TrainingPipelineConfig()
 # data_ingestion_config=DataIngestionConfig(training_pipeline_config=training_pipeline_config)
  #print(data_ingestion_config.__dict__)
  #print(dataingestion.__dict__)
  #train_pipeline=TrainPipeline()
  #train_pipeline.run_pipeline()
  training_pipeline=TrainPipeline()
  training_pipeline.run_pipeline()
  
