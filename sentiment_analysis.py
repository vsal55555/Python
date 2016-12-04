# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:25:43 2016

@author: DJ
"""

import matplotlib.pyplot as plt   # for plotting
import pandas as pd # for getting data

twitter_data=pd.read_csv('results_olympics.csv')

print (twitter_data.corr())  #correlation analysis just apply correlation function to data
twitter_data_subjective=twitter_data[twitter_data['subjectivity']>0.5]

print (twitter_data_subjective.corr()) 

plt.scatter(twitter_data.retwc,twitter_datadata.plority)