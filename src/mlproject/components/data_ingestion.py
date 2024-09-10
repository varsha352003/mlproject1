##MySQL--->Train test split--->dataset
import os
import sys ##for custom exception
from mlproject.exception import CustomException
from mlproject.logger import logging
import pandas as pd
from mlproject.utils import read_sql_data
from sklearn.model_selection import train_test_split
from dataclasses import dataclass ##to initialize input parameter

@dataclass
class DataIngestionConfig:
    train_data_path:str=os.path.join('artifacts','train.csv')
    test_data_path:str=os.path.join('artifacts','test.csv')
    raw_data_path:str=os.path.join('artifacts','raw.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        try:
            ##reading the data from mysql
            df=pd.read_csv(os.path.join('notebook/data','raw.csv'))
            logging.info("Reading completed from mysql database")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)
            ##this is to create artifacts folder
            ##all these train_data_path,test_data_path are in self.ingestion_config we can take any path train,test or raw data path
            ##self.ingestion_config pecifies the path where the training data file will be saved
            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True) ##index false so that it does not take index
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)
            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)

            logging.info("Data ingestion is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e,sys) ##error parameters