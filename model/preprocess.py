
from re import S
import numpy as np
import pandas as pd
import os
import argparse

import tensorflow as tf
from sklearn.model_selection import train_test_split
from tflite_model_maker import model_spec

parser = argparse.ArgumentParser(description=' ################ MySafetyNet: Preprocessing data ################', usage='%(prog)s')
parser.add_argument('-in', '--input', type=str, required=True, help='Input csv file containing the data', dest='input')
parser.add_argument('-out', '--output', type=str, required=True, help='Output path for saving the data', dest='output')

args = parser.parse_args()
data = args.input
out_path = args.output

def main():
    '''
    Applies preprocessing to the data 
    and handles imbalance problem
    '''
    if data[-3:]=='zip':
        df = pd.read_csv(data,
                    compression='zip',low_memory=False)
    elif data[-3:]=='csv':
        df = pd.read_csv(data,
                    low_memory=False)
    else:
        print('Error: Input file type is not supported')

    print(df)
    print(df.keys())
    df_count = df.groupby(['label']).size().reset_index(name='count')
    print(df_count)

    count_labels = []
    
    for index, row in df_count.iterrows():
        print(row['label'], row['count'])
        count_labels.append(row['count'])
    print(count_labels)
    sorted_count_labels = sorted(count_labels)
    print(sorted_count_labels, len(sorted_count_labels))

    imbalanced = False
    th = 2 # %20 of data
    for i in range(len(sorted_count_labels)-1):
        ratio = sorted_count_labels[i+1] / sorted_count_labels[i]
        if ratio>th:
            imbalance = True
            print('Imbalanced data. Ratio of: ', ratio)
        
    df.label.plot(kind='hist', title='labels distribution')

    if imbalance == True:
        train_df, rest = train_test_split(df, random_state=42, train_size=0.80, stratify=df.label.values) # 80% train
        valid_df, test_df = train_test_split(rest, random_state=42, train_size=0.50, stratify=rest.label.values)

        train_path = out_path + 'train_strat.csv'
        valid_path = out_path + 'valid_strat.csv'
        test_path = out_path + 'test_strat.csv'

    else:
        train_df, rest = train_test_split(df, random_state=42, train_size=0.80 ) # 80% train
        valid_df, test_df = train_test_split(rest, random_state=42, train_size=0.50)

        train_path = out_path + 'train.csv'
        valid_path = out_path + 'valid.csv'
        test_path = out_path + 'testt.csv'

    print('Train: ', train_df.shape)
    print('Valid: ',valid_df.shape)
    print('Test: ', test_df.shape)

    train_df.to_csv (train_path, index = False, header=True)
    valid_df.to_csv (valid_path, index = False, header=True)
    test_df.to_csv (test_path, index = False, header=True)


if __name__ == "__main__":
    main()