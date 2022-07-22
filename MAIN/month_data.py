# 导入第三方库
import pandas as pd

df = pd.read_csv('./result_data/data_monthly.csv')                #加载原始的天气数据

# 读入原始数据
date=df['日期'].to_list()                       
AQI=df['平均空气质量指数'].to_list()
temperature_highest=df['平均高温'].to_list()
temperature_lowest=df['平均低温'].to_list()
name=['月平均高温','月平均低温','月平均空气质量指数']

# 去取缺失值
AQI=AQI[84:]

# 格式化数据
date_amount=len(date)
for i in range(date_amount):
    temperature_highest[i]=temperature_highest[i].replace("℃",'')   #替换摄氏度
    temperature_lowest[i]=temperature_lowest[i].replace("℃",'')

# 字符串转整型
temperature_highest=list(map(int,temperature_highest))  #将原来通过字符串保存的天气数据转化为整型
temperature_lowest=list(map(int,temperature_lowest))
AQI=list(map(int, AQI))

# 提取每列下某一个月的数据
def select_month(item,month):
    temp=[]
    amount=len(item)
    month = month-1
    while month<amount:
        temp.append(item[month])
        month=month+12
    return temp

# 提取每年11月份的数据
November_temperature_highest=select_month(temperature_highest,11)
November_temperature_lowest=select_month(temperature_lowest,11)