from sklearn import preprocessing
import numpy as np
from numpy import genfromtxt
import pandas as pd





#my_data = genfromtxt('Training_Data_2016/training_data_2016.csv', delimiter=',')
#Data = np.asarray(my_data)
#unique=np.unique(column(Data,2))
#print(unique)

Data = pd.read_csv('Training_Data_2016/training_data_2016.csv',low_memory = False)
Data = Data.drop('Vehicle_Annual_Miles', 1)
Data = Data.drop('Vehicle_Comprehensive_Coverage_Limit', 1)
replacements = {
   'Policy_Zip_Code_Garaging_Location': {
      r'Unknown': '00000',}
    'Vehicle_Miles_To_Work': {
      r'-1': np.nan,}
    'Policy_Zip_Code_Garaging_Location': {
      r'Unknown': '00000',}
    'Vehicle_Passive_Restraint': {
      r'Unknown': 'Y',}
    'Vehicle_Med_Pay_Limit': {
      r'Unknown': np.nan,}
    'Policy_Zip_Code_Garaging_Location': {
      r'Unknown': '00000',}






}

Data.replace(replacements, regex=True, inplace=True)
#Data['Policy_Zip_Code_Garaging_Location'] = Data['Policy_Zip_Code_Garaging_Location'].replace('Unknown', '00000')
for col in Data[1:]:
    print Data[col].unique()
    #print Data[col].columns
#print Data[1].unique()
#print list(Data.columns.values)
#print(Data.head())

