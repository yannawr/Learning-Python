# first machine learning study
# this code is a reproduction of this one https://www.youtube.com/watch?v=i_LwzRVP7bg
# I reproduced it only for a first study

import numpy as np
import pandas as pd

import matplotlib.pyplot as plt
import os

# get the absolute path of the current script
script_path = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_path, "magic04.csv")

# add header
cols = ["fLength", "fWidth", "fSize", "fConc", "fConc1", "fAsym", "fM3Long", "fM3Trans", "fAlpha", "fDist", "class"]

df = pd.read_csv(file_path, names=cols)
df["class"] = (df["class"] == "g").astype(int)
print(df.head())

for label in cols[:-1]:
    plt.hist(df[df["class"] == 1][label], color = 'blue', label='gamma', alpha=0.7, density=True)
    plt.hist(df[df["class"] == 0][label], color = 'red', label='hadron', alpha=0.7, density=True)
    plt.title(label)
    plt.ylabel("Probability")
    plt.xlabel(label)
    plt.legend()
    plt.show()
    
# train, validation and test datasets
train, valid, test = np.split(df.sample(frac=1), [int(0.6*len(df)), int(0.8*len(df))])

# to complete...
