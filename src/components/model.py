import pandas as pd
from dataclasses import dataclass
from src.exception import customException
from src.logger import logging
import os
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
from src.components.utils import save_pickle


@dataclass
class ModelPath:
    file_path=os.path.join("artifacts","model.pkl")
    
class TrainModel:
    def __init__(self):
        self.model_path=ModelPath()
        
    def train_model(self,train_arr,test_arr):
        x_train=train_arr[:,:-1]
        y_train=train_arr[:,-1]
        x_test=test_arr[:,:-1]
        y_test=test_arr[:,-1]
        
        model=LogisticRegression()
        logging.info("initiating fitting data")
    
        
        model.fit(x_train,y_train)
        
        
        y_train_pred=model.predict(x_train)
        y_test_pred=model.predict(x_test)
        logging.info("testing accuracy of score")
        
        y_train_score=accuracy_score(y_train,y_train_pred)
        y_test_score=accuracy_score(y_test,y_test_pred)
        logging.info("saving model.pkl file")
        
        save_pickle(model,self.model_path.file_path)
        
        
        return y_train_score,y_test_score,self.model_path.file_path
        
        
        
        
        
        