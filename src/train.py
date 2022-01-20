import os
import pandas as pd
from sklearn import ensemble
from sklearn import preprocessing
from sklearn import metrics
import joblib

TRAINING_DATA = "C:\\Users\\user\\kaggle_playground\\data\\train.csv"
TEST_DATA =  "C:\\Users\\user\\kaggle_playground\\data\\test.csv"
#FOLD = int(os.environ.get("FOLD"))
#ODEL = os.environ.get("MODEL")

if __name__ == "__main__":
    df_train = pd.read_csv(TRAINING_DATA)
    df_test = pd.read_csv(TEST_DATA)
    print(df_train.shape)
   

