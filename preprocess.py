from sklearn import preprocessing
import numpy as np
from numpy import genfromtxt
import pandas as pd





Data = pd.read_csv('training_data_2016.csv',low_memory = False)

# Drop unneccessary columns #

Data = Data.drop('Vehicle_Annual_Miles', 1)
Data = Data.drop('Vehicle_Comprehensive_Coverage_Limit', 1)
Data = Data.drop('Driver_Minimum_Age', 1)
Data = Data.drop('Driver_Maximum_Age', 1)
Data = Data.drop('EEA_PolicyYear', 1)
Data = Data.drop('Vehicle_New_Cost_Amount', 1)
Data = Data.drop('vehicle_make_description', 1)

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

# Classify driver_Age into 3 categories Cizhen #

Data['Driver_Age_Under_25'] = pd.Series(Data.Driver_Total_Teenager_Age_15_19 + Data.Driver_Total_College_Ages_20_23, index=Data.index)
Data['Driver_Age_25_To_64'] = pd.Series(Data.Driver_Total_Young_Adult_Ages_24_29 + Data.Driver_Total_Low_Middle_Adult_Ages_30_39 + Data.Driver_Total_Middle_Adult_Ages_40_49 + Data.Driver_Total_Adult_Ages_50_64, index=Data.index)
Data['Driver_Age_Above_64'] = pd.Series(Data.Driver_Total_Senior_Ages_65_69 + Data.Driver_Total_Upper_Senior_Ages_70_plus, index=Data.index)

# Drop the unclassified Driver_Ages_xxx columns Cizhen #

Data = Data.drop('Driver_Total_Teenager_Age_15_19', 1)
Data = Data.drop('Driver_Total_College_Ages_20_23', 1)
Data = Data.drop('Driver_Total_Young_Adult_Ages_24_29', 1)
Data = Data.drop('Driver_Total_Low_Middle_Adult_Ages_30_39', 1)
Data = Data.drop('Driver_Total_Middle_Adult_Ages_40_49', 1)
Data = Data.drop('Driver_Total_Adult_Ages_50_64', 1)
Data = Data.drop('Driver_Total_Senior_Ages_65_69', 1)
Data = Data.drop('Driver_Total_Upper_Senior_Ages_70_plus', 1)


#Categorizing continuous data #

Data['Vehicle_Miles_To_Work']=pd.cut(Data['Vehicle_Miles_To_Work'], bins=[0, 20,40,60,80,100], include_lowest=True, labels=['lowest', 'low', 'mid', 'high', 'highest'])

Data['Annual_Premium'] = pd.cut(Data['Annual_Premium'],9 , labels= ['highest', 'very high', 'moderately high', 'higher', 'medium', 'lower', 'moderately low', 'very low', 'lowest'])


# Print unique values in each column #

# for col in Data[1:]:
#     print Data[col].unique()

# Save modified data to new csv file #

Data.to_csv('new_data.csv', sep=',', encoding='utf-8')
print 'done'
