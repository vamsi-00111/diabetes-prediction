import os
import pandas as pd
from dataclasses import dataclass
from src.exception import customException
from src.logger import logging
from sklearn.preprocessing import StandardScaler
from sklearn.compose import ColumnTransformer
import numpy as np
from utils import save_pickle


@dataclass
class DataTransformFilePaths:
    data_preprocessor_file_Path=os.path.join("artifacts","preprocessed.pkl")
    
class DataTransformation:
    def __init__(self):
        
        self.filepath=DataTransformFilePaths()
        
    def data_transformation_obj(self):
        try:
            logging.info("transformation started")
            columns=['Glucose',
                    'BloodPressure',
                    'SkinThickness',
                    'Insulin',
                    'BMI',
                    'Age',
                    'Pregnancies',
                    'DiabetesPedigreeFunction']
            scaler=StandardScaler()
            ct=ColumnTransformer(
                [
                    ("scaler",scaler,columns)
                ]
            )
            logging.info("transformation is finished")
            
            return ct
        
        except Exception as e:
            raise customException(e)
            
        
    def initiate_data_transformation(self,x_train,x_test):
        try:
            
            df_xtrain=pd.read_csv(x_train)
            df_xtest=pd.read_csv(x_test)
            
            logging.info("initiating splitting data")

            target_column="Outcome"
            x_train=df_xtrain.drop(target_column,axis=1)
            y_train=df_xtrain[target_column]
           
            
            x_test=df_xtest.drop(target_column,axis=1)
            y_test=df_xtest[target_column]
            logging.info("scaling train and test data")
            
            std=self.data_transformation_obj()
            
            x_train_scaler=std.fit_transform(x_train)
            x_test_scaler=std.transform(x_test)
            logging.info("finished scaling ")
            
            x_train_arr=np.c_[x_train_scaler,np.array(y_train)]
            x_test_arr=np.c_[x_test_scaler,np.array(y_test)]
            
            save_pickle(std,self.filepath.data_preprocessor_file_Path)
            
            
            return x_train_arr,x_test_arr,self.filepath.data_preprocessor_file_Path
            
            
            
            
        except  Exception as e:
            raise customException(e)
            
