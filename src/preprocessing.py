import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
class DataPreProcessor:
    
    def __init__(self):
        self.scaler = StandardScaler()
    
    def clean_data(self,df):
        df = df.copy()
        df = df.dropna().reset_index(drop = True)
        return df
    
    def split_features_target(self,df):
        df = df.copy()
        X = df.drop(columns = ["Date" , "Asset", "Target_Volatility_20"] )
        y = df["Target_Volatility_20"]
        return X,y
    
    def train_test_split(self,X,y,train_size = 0.8):
        split = int(len(X) * train_size)
        X_train = X.iloc[:split]
        X_test = X.iloc[split:]
        y_train = y.iloc[:split]
        y_test = y.iloc[split:]
        return X_train, X_test, y_train, y_test
    
    def scale_features(self,X_train,X_test):
        X_train_scaled = self.scaler.fit_transform(X_train)
        X_test_scaled = self.scaler.transform(X_test)
        return X_train_scaled, X_test_scaled
    
