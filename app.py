import sys
import os

# Append 'src' to sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))
from mlproject.logger import logging
from mlproject.exception import CustomException
from mlproject.components.data_ingestion import DataIngestion ##data ingestion is our class
from mlproject.components.data_ingestion import DataIngestionConfig
if __name__ == "__main__":
    logging.info("The execution has started")

    try:
        #data_ingestion_config=DataIngestionConfig() we don't need this as it's already called in dataingestion
        data_ingestion=DataIngestion()
        data_ingestion.initiate_data_ingestion()

    except Exception as e:
        logging.info("Custom Exception")
        raise CustomException(e,sys)
