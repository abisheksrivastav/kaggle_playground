from json.tool import main
from os import listdir
from os.path import isfile, join
import random
import pandas as pd
import numpy as np
import sys
from sklearn import model_selection



#if __name__ == "__main__":

    #df = pd.read_csv('C:\\Users\\user\\kaggle_playground\\data\\train.csv')
    #df['kfold'] = -1
    #df = df.sample(frac=1).reset_index(drop=True)
    # groupkfold
  
    #y = df.num_sold.values
    #groups = df.date.dt.year
   # kf = model_selection.GroupKFold(n_splits=5)
   # for fold, (trn_, val_) in enumerate(kf.split(X=df, y=y, groups=groups)):
        #print(len(trn_), len(val_))
        #df.loc[val_, 'kfold'] = fold

    #df.to_csv('train_folds.csv', index=False) 


#  create_folds.py with groupkfold 

if __name__ == "__main__":
    df = pd.read_csv('C:\\Users\\user\\kaggle_playground\\data\\train.csv')
    df['kfold'] = -1
    df = df.sample(frac=1).reset_index(drop=True)
    # groupkfold
    #y = df.num_sold.values
    df['date'] = pd.to_datetime(df['date'])
    groups = df['date'].dt.year
    kf = model_selection.GroupKFold(n_splits=4)
    for fold, (trn_, val_) in enumerate(kf.split(X=df,  groups=groups)):
        print(len(trn_), len(val_))
        df.loc[val_, 'kfold'] = fold

    df.to_csv('train_folds.csv', index=False)