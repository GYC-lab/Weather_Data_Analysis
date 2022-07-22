# 导入第三方库
import pandas as pd

df = pd.read_csv('./result_data/AQI_daily.csv')                #加载原始的天气数据

# 读入原始数据
title=df.columns.tolist()[1:]
AQI=df['AQI'].to_list()                       
AQI_rank=df['AQI_rank'].to_list()
PM25=df['PM2.5'].to_list()
PM10=df['PM10'].to_list()
SO2=df['SO2'].to_list()
NO2=df['NO2'].to_list()
CO=df['CO'].to_list()
O3=df['O3'].to_list()
air_quality=[AQI,AQI_rank,PM25,PM10,SO2,NO2,CO,O3]

#获得数据集大小
date_amount=len(AQI)