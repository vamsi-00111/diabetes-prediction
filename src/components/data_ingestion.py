from src.exception import customException
from src.logger import logging
from src.components.data_transformation import DataTransformation
import pandas as pd
import os
from dataclasses import dataclass
from sklearn.model_selection import train_test_split
from src.components.model import TrainModel


@dataclass
class configFilePaths:
    train_data_path: str = os.path.join("artifacts", "train.csv")
    test_data_path: str = os.path.join("artifacts", "test.csv")
    raw_data_path: str = os.path.join("artifacts", "data.csv")

class dataIngestion:
    def __init__(self):
        self.config=configFilePaths()
        
    def initiate_data_splitting(self):
        logging.info("data ingestion started")
        try:
             df=pd.read_csv("data/imputed diabetes.csv")
             
             os.makedirs("artifacts",exist_ok=True)
             
             df.to_csv(self.config.raw_data_path,index=False)
          
             
             
             logging.info("initiating data splitting")
          
             train,test=train_test_split(df,random_state=42,test_size=.2)
             
             logging.info("saving train and test data")
             
             train.to_csv(self.config.train_data_path,index=False)
             test.to_csv(self.config.test_data_path,index=False)
             
             return self.config.train_data_path,self.config.test_data_path
                 
             
        except Exception as e:
            raise customException(e)
             
if __name__=="__main__":
    
    splitting=dataIngestion()
    train_data,test_data=splitting.initiate_data_splitting()
    
    tranform=DataTransformation()
    x_train,x_test,_=tranform.initiate_data_transformation(x_train=train_data,x_test=test_data)
    
    model=TrainModel()
    
    r2_xtrain,r2_xtest,_=model.train_model(x_train,x_test)
    print((r2_xtrain,r2_xtest))
             
             
             
             
             
             
             
             
             
             
             
        