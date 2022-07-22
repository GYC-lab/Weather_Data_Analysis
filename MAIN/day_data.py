# 导入第三方库
import pandas as pd 
import re

# 读取数据
df = pd.read_csv('./result_data/data_daily.csv')

# 原始数据
date=df['日期'].to_list()
temperature_highest=df['最高温'].to_list()
temperature_lowest=df['最低温'].to_list()
wind_power=df['风力风向'].to_list()
AQI=df['空气质量指数 '].to_list()

# 格式化数据
date_amount=len(date)
wind_power_temp=[]
AQI_temp=[]
for i in range(date_amount):
    temperature_highest[i]=temperature_highest[i].replace("°",'')
    temperature_lowest[i]=temperature_lowest[i].replace("°",'')
    wind_power[i]=re.findall(r"\d+\.?\d*",wind_power[i])
    wind_power_temp.append(wind_power[i][0])
    AQI[i]=re.findall(r"\d+\.?\d*",AQI[i])
    AQI_temp.append(AQI[i][0])

# 字符串转整型
temperature_highest=list(map(int,temperature_highest))
temperature_lowest=list(map(int,temperature_lowest))
wind_power=list(map(int,wind_power_temp))
AQI=list(map(int,AQI_temp))

# 天气数据对应的名称
weather_name=['最高温','最低温','风力','空气质量指数']