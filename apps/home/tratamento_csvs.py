#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Apr 13 00:13:54 2021

@author: rogerbage
"""

import pandas as pd
import glob
#import graficos as gra

path = r'csvs/feitos/' # use your path
all_files = glob.glob(path + "/*.csv")

matches = ["petroleo", "petróleo"]

contador = {}
x = []
y = []

def conta_matches(df):
    cont = 0
    for f in df.itertuples():
        if any(z in f.inteiro_teor.lower() for z in matches):
            cont += 1
    return cont

for filename in all_files:
    df = pd.read_csv(filename, sep=';')
    contador[str(df.ano[0])] = conta_matches(df)
    
 
for i in sorted(contador.keys()):
    x.append(i)
    y.append(contador[i])

print (x, y)
#gra.GeraBar(x, y)

