#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on: 2019
Author: @daniel
"""
import os
import time
import pandas as pd
import numpy as np

path = 'C:/Users/devg2/Desktop/Sample TEXT'
os.chdir(path)

''' ---------------------------- DATA ETL FUNCTIONS ------------------------'''


def load_amadeus(directory):
    '''Scans all files directory and returns AMADEUS as dataframe'''
    amadeus_list = []
    amadeus_files = []
    amadeus = []
    for root, dirs, files in os.walk(os.path.abspath('../Sample TEXT/AMADEUS')):
        for file in files:
            amadeus_files.append(file)
            amadeus_list.append(os.path.join(root, file))
    for file in amadeus_list:
        text = open(file, 'r')
        amadeus.append(text.readlines())
    length = len(sorted(amadeus, key=len, reverse=True)[0])
    amadeus = pd.DataFrame(
        np.array([xi + [None]*(length - len(xi)) for xi in amadeus]))
    amadeus.insert(loc=0, column='File', value=amadeus_files)

    return amadeus


def load_galileo(directory):
    '''Scans all files directory and returns GALILEO as dataframe'''
    galileo_list = []
    galileo_files = []
    galileo = []
    for root, dirs, files in os.walk(os.path.abspath('../Sample TEXT/GALILEO')):
        for file in files:
            galileo_files.append(file)
            galileo_list.append(os.path.join(root, file))
    for file in galileo_list:
        text = open(file, 'r')
        galileo.append(text.readlines())
    length = len(sorted(galileo, key=len, reverse=True)[0])
    galileo = pd.DataFrame(
        np.array([xi + [None]*(length - len(xi)) for xi in galileo]))
    galileo.insert(loc=0, column='File', value=galileo_files)

    return galileo


def load_sabre(directory):
    '''Scans all files directory and returns SABRE as dataframe'''
    sabre_list = []
    sabre_files = []
    sabre = []
    for root, dirs, files in os.walk(os.path.abspath('../Sample TEXT/SABRE')):
        for file in files:
            sabre_files.append(file)
            sabre_list.append(os.path.join(root, file))
    for file in sabre_list:
        text = open(file, 'r')
        sabre.append(text.readlines())
    length = len(sorted(sabre, key=len, reverse=True)[0])
    sabre = pd.DataFrame(
        np.array([xi + [None]*(length - len(xi)) for xi in sabre]))
    sabre.insert(loc=0, column='File', value=sabre_files)

    return sabre


# Data ETL to dataframes
start = time.time()
amadeus = load_amadeus(path)
galileo = load_galileo(path)
sabre = load_sabre(path)

# Test dataframes to csv
amadeus.to_csv('amadeus.csv', sep='\t', encoding='utf-8')
galileo.to_csv('galileo.csv', sep='\t', encoding='utf-8')
sabre.to_csv('sabre.csv', sep='\t', encoding='utf-8')
end = time.time()

#total_files = f'Total Amadeus files: {len(amadeus_files)}, Total Galileo files: {len(galileo_files)}, Total Sabre files: {len(sabre_files)}'
#total_time = f'Total code running time: {end - start}, for {len(amadeus_files) + len(galileo_files) + len(sabre_files)} total files'
