import numpy as np
import pandas as pd
class TargetEngineer():

    def __init__(self):
        pass
    
    def add_target_features(self, df, horizon=20):
        df = df.copy()
        df[f"Target_Volatility_{horizon}"] = (
            df["Daily_Return"]
            .rolling(window=horizon)
            .std()
            .shift(-horizon)
            * np.sqrt(252)
        )
        return df