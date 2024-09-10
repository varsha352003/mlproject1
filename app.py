import sys
import os

# Append 'src' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from mlproject.logger import logging
from mlproject.exception import CustomException
from mlproject.components.data_ingestion import DataIngestion ##data ingestion is our class
from mlproject.components.data_ingestion import DataIngestionConfig
from mlproject.components.data_transformation import DataTransformationConfig, DataTransformation




if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        #data_ingestion_config=DataIngestionConfig() we don't need this as it's already called in dataingestion
        data_ingestion=DataIngestion()
        train_data_path,test_data_path=data_ingestion.initiate_data_ingestion()

        #data_transfromation_config=DataTransformationConfig()
        #no need to call data trans config as data transformation will call it
        data_transformation=DataTransformation()
        data_transformation.initiate_data_transformation(train_data_path,test_data_path)   #will give train and test path in this

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
