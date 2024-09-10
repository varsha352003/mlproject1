#take the train test raw data that we formed and apply feature engineering using pipeline to it and the pickle file of feature engg will be our output
import sys
from dataclasses import dataclass
import numpy as np
import pandas as pd
from sklearn.preprocessing import OneHotEncoder,StandardScaler
from sklearn.compose import ColumnTransformer
#to handle categorical values and missing data
from sklearn.impute import SimpleImputer
from sklearn.pipeline import Pipeline

from mlproject.utils import save_object

from mlproject.exception import CustomException
from mlproject.logger import logging

#as we will need pickle file

import os

#input will be the feature engg pickle file path
class DataTransformationConfig:
    preprocessor_obj_file_path=os.path.join('artifacts','preprocessor.pk1') #preprocessor.pk1 is pickel file

class DataTransformation:
    def __init__(self):
        self.data_transformation_config=DataTransformationConfig()


    def get_data_transformer_object(self):
        #this function will perform feature engg

        try:
            numerical_columns = ["writing_score", "reading_score"]
            categorical_columns = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]
            num_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy='median')), #imputer used to fill the missing values with median
                ('scalar',StandardScaler())
            ])
            cat_pipeline=Pipeline(steps=[
                ("imputer",SimpleImputer(strategy='most_frequent')),
                ("one hot encoder",OneHotEncoder()),
                ("Scalar",StandardScaler(with_mean=False))#removing the mean and scaling to unit variance.
                
            ])
            logging.info(f"Categorical Columns:{categorical_columns}")
            logging.info(f"Numerical Columns:{numerical_columns}")

            #now to combine both numerical and categorical column we will use column transfoermer


            preprocesor=ColumnTransformer(
                [
                    ("num_pipeline",num_pipeline,numerical_columns),
                    ("cat_pipeline",cat_pipeline,categorical_columns)
                ]
            )
            return preprocesor

        except Exception as e:
            raise CustomException(e,sys)
        #we have given traain and test path for data transformation
    def initiate_data_transformation(self,train_path,test_path):
        try:
            train_df=pd.read_csv(train_path)
            test_df=pd.read_csv(test_path)

            logging.info("REading the train and test file")
            #this object will be calling feature engg function
            preprocessing_obj=self.get_data_transformer_object()

            target_column_name="math_score"
            numerical_columns=["writing_score","reading_score"]

        #divide the train dataset into independent and dependent feature
            input_features_train_df=train_df.drop(columns=[target_column_name],axis=1)
            target_feature_train_df=train_df[target_column_name]


        #divide the test dataset into independent and dependent feature
            input_features_test_df=test_df.drop(columns=[target_column_name],axis=1)
            target_feature_test_df=test_df[target_column_name]

            logging.info("Applying Preprocessing on training and test dataframe")

            input_feature_train_arr=preprocessing_obj.fit_transform(input_features_train_df)
            input_feature_test_arr=preprocessing_obj.transform(input_features_test_df)
            #here we are only doing transform bcz of data leakage concept

            #creating array for input and target vales
            train_arr = np.c_[
                input_feature_train_arr, np.array(target_feature_train_df)
            ]
            test_arr = np.c_[input_feature_test_arr, np.array(target_feature_test_df)]

            logging.info(f"Saved preprocessing object")

            #now go to util.py import pickle and create function save_object to create pickle file
        #next import save object function from utils here



            save_object(

                file_path=self.data_transformation_config.preprocessor_obj_file_path, #pickle file path 
                obj=preprocessing_obj
            )

            return(
                train_arr,
                test_arr,
                self.data_transformation_config.preprocessor_obj_file_path
                
            )
        
        except Exception as e:
            raise CustomException(sys,e)
        
        #now to run data transformstion goto app.py