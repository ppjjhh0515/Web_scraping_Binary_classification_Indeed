#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue May 11 20:27:07 2021

@author: junghopark
"""

import pandas as pd 
from joblib import load
import csv

def load_data(data_path):
    alldata_df = pd.read_csv(data_path) 
    alldata_df.columns = ['Text']
    all_X = alldata_df['Text']

    return all_X


def vectorize_data(all_X, counter_path):
    #Build a counter based on the training dataset
    counter = load(counter_path)
    #count the number of times each term appears in a document and transform each doc into a count vector
    X_vector = counter.transform(all_X)
    
    return X_vector


if __name__ == "__main__":
    # load the new data (no labels)
    all_X = load_data("test_set.csv")
    # use the existing vectorizer we fitted during training to vectorize the new data
    X_vector = vectorize_data(all_X, "fit_counter.joblib")
    
    # load the model we trained
    VT = load("trained_model.joblib")

    pred=VT.predict(X_vector)

    print("\n The predictions for the loaded data are\n", pred)
    
    output = open('new_test_set_prediction_output.csv', 'w', encoding='UTF-8')
    writer = csv.writer(output, lineterminator='\n')
    for prediction in pred:
        if prediction == 0:
            write = "data scientist"
        elif prediction == 1:
            write = "software engineer"
        writer.writerow(write)
    print("predictions saved at new_test_set_prediction_output.csv")