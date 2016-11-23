from sklearn import preprocessing
import numpy as np
from numpy import genfromtxt
import pandas as pd





Data = pd.read_csv('Training_Data_2016/training_data_2016.csv',low_memory = False)

# Drop unneccessary columns #

Data = Data.drop('Vehicle_Annual_Miles', 1)
Data = Data.drop('Vehicle_Comprehensive_Coverage_Limit', 1)
Data = Data.drop('Driver_Minimum_Age', 1)
Data = Data.drop('Driver_Maximum_Age', 1)
Data = Data.drop('EEA_PolicyYear', 1)
Data = Data.drop('Vehicle_New_Cost_Amount', 1)

# Clearing unneccessary rows #

Data = Data[Data.EEA_Policy_Tenure != -1]
Data = Data[Data.Vehicle_Symbol != -1]
Data = Data[Data.Vehicle_Days_Per_Week_Driven != -1]
Data = Data[Data.Vehicle_Anti_Theft_Device != 'Unknown']

# Replace missing Data #

Data['Policy_Zip_Code_Garaging_Location'] = Data['Policy_Zip_Code_Garaging_Location'].replace('Unknown', '00000')
Data['Vehicle_Miles_To_Work'] = Data['Vehicle_Miles_To_Work'].replace('-1', np.nan)
Data['Vehicle_Passive_Restraint'] = Data['Vehicle_Passive_Restraint'].replace('Unknown', 'Y')
Data['EEA_Policy_Zip_Code_3'] = Data['EEA_Policy_Zip_Code_3'].replace('Unknown', '000')
Data['Vehicle_Med_Pay_Limit'] = Data['Vehicle_Med_Pay_Limit'].replace('-1', np.nan)
Data['Vehicle_Physical_Damage_Limit'] = Data['Vehicle_Physical_Damage_Limit'].replace('-1', np.nan)
Data['Vehicle_Collision_Coverage_Deductible'] = Data['Vehicle_Collision_Coverage_Deductible'].replace('-1', np.nan)

# Fill nan data #

Data['Vehicle_Miles_To_Work'].fillna((Data['Vehicle_Miles_To_Work'].mean()), inplace=True)
Data['Vehicle_Med_Pay_Limit'].fillna((Data['Vehicle_Med_Pay_Limit'].mean()), inplace=True)

# Print unique values in each column #

for col in Data[1:]:
    print Data[col].unique()

# Save modified data to new csv file #

Data.to_csv('new_data.csv', sep=',', encoding='utf-8')
