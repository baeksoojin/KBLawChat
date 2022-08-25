import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import re
import urllib.request
import time
import tensorflow_datasets as tfds
import tensorflow as tf


df_law = pd.read_csv('lawdata.csv',encoding=False)


train_data=df_law
train_data=train_data[0:-1]
train_data.head()

train_data.loc[(train_data['label']=="법인세법"),'label']=0
train_data.loc[(train_data['label']=="자본시장법"),'label']=1
train_data.loc[(train_data['label']=="소득세법"),'label']=2