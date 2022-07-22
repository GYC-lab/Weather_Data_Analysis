import day_data # 导入处理过的数据
from matplotlib import pyplot as plt, rcParams
import numpy as np

rcParams['font.family']='FangSong'  #设置字体形式（防止中文乱码）
rcParams['axes.unicode_minus']=False    #设置正常显示字符（显示负号

# 气温数据可视化
def plot_temperature():
    plt.figure()
    x=list(np.arange(1,day_data.date_amount+1).astype(dtype=np.str_))
    plt.plot(x,day_data.temperature_highest,'r-',label='月平均高温')
    plt.plot(x,day_data.temperature_lowest,'b-',label='月平均低温')
    plt.scatter(x,day_data.temperature_highest,s=20,color='red',marker='o',linewidth=2,alpha=0.8)
    plt.scatter(x,day_data.temperature_lowest,s=20,color='blue',marker='o',linewidth=2,alpha=0.8)
    plt.xlabel('天数')    #设置x轴标签
    plt.ylabel('气温')    #设置x轴标签
    plt.yticks(fontsize=12) #调整y轴刻度标签大小
    plt.title('2021年11月西安市气温走势图')
    plt.legend()
    # plt.show()            #显示图片
    plt.rcParams['savefig.dpi'] = 600              #设置图片像素
    plt.savefig('./result_figure/daily/plot/2021年11月1日-11月20日西安市气温走势图.png')         #保存图片

# 风力等级数据可视化
def plot_wind_power():
    plt.figure()
    x=list(np.arange(1,day_data.date_amount+1).astype(dtype=np.str_))
    plt.plot(x,day_data.wind_power)
    plt.scatter(x,day_data.wind_power,s=20,color='blue',marker='o',linewidth=2,alpha=0.8)
    plt.xlabel('天数')    #设置x轴标签
    plt.ylabel('风力等级')    #设置x轴标签
    plt.yticks(fontsize=12) #调整y轴刻度标签大小
    plt.title('2021年11月1日-11月20日西安市风力等级走势图')
    # plt.show()            #显示图片
    plt.rcParams['savefig.dpi'] = 600              #设置图片像素
    plt.savefig('./result_figure/daily/plot/2021年11月1日-11月20日西安市风力等级走势图.png')         #保存图片

# 空气质量数据可视化
def plot_AQI():
    plt.figure()
    x=list(np.arange(1,day_data.date_amount+1).astype(dtype=np.str_))
    plt.plot(x,day_data.AQI,'b')
    plt.scatter(x,day_data.AQI,s=30,color='red',marker='x',linewidth=2,alpha=0.8)
    plt.grid(color='#95a5a6',linestyle='--', linewidth=1,axis='both',alpha=0.4)
    plt.xlabel('天数')    #设置x轴标签
    plt.ylabel('平均空气质量指数')    #设置x轴标签
    plt.yticks(fontsize=12) #调整y轴刻度标签大小
    plt.title('2021年11月1日-11月20日西安市空气质量走势图')
    # plt.show()
    plt.rcParams['savefig.dpi'] = 600              #设置图片像素
    plt.savefig('./result_figure/daily/plot/2021年11月1日-11月20日西安市空气质量走势图.png')         #保存图片

plot_temperature()
plot_wind_power()
plot_AQI()