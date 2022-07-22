import month_data # 导入处理过的数据
from matplotlib import pyplot as plt, rcParams

rcParams['font.family']='FangSong'  #设置字体形式（防止中文乱码）
rcParams['axes.unicode_minus']=False    #设置正常显示字符（显示负号）

# 绘制气温走势图
def plot_temperature():
    plt.figure() 
    x=list(range(1,month_data.date_amount+1))
    plt.plot(x,month_data.temperature_highest,'r-',label='月平均高温')
    plt.plot(x,month_data.temperature_lowest,label='月平均低温')
    plt.xlabel('月份')                          #设置x轴标签
    plt.ylabel('气温')                          #设置y轴标签
    plt.xticks(fontsize=12)                     #调整x轴刻度标签大小
    plt.yticks(fontsize=12)                     #调整y轴刻度标签大小
    plt.title('2011-2020年西安市月平均气温走势图')#设置图标题
    plt.legend()                                #显示图例
    # plt.show()                                #显示图片
    plt.rcParams['savefig.dpi'] = 600           #设置图片像素
    plt.savefig('./result_figure/monthly/plot/2011-2020年西安市月平均气温走势图.png')     #保存图片

# 绘制平均空气质量走势图
def plot_AQI():
    plt.figure() 
    x=list(range(1,len(month_data.AQI)+1))
    plt.plot(x,month_data.AQI)
    plt.xlabel('月份')                          #设置x轴标签
    plt.ylabel('平均空气质量指数')               #设置y轴标签
    plt.xticks(fontsize=12)                     #调整x轴刻度标签大小
    plt.yticks(fontsize=12)                     #调整y轴刻度标签大小
    plt.title('2018-2020年西安市月平均空气质量指数走势图')                  #设置图标题
    plt.rcParams['savefig.dpi'] = 600           #设置图片像素
    plt.savefig('./result_figure/monthly/plot/2018-2020年西安市月平均空气质量指数走势图.png')     #保存图片

#绘制10年间每年11月的气温走势图
def plot_November_temperature():
    plt.figure() 
    year_int=list(range(2011,2021))
    year=list(map(str,year_int))
    plt.plot(year,month_data.November_temperature_highest,'r-',label='平均高温')
    plt.plot(year,month_data.November_temperature_lowest,'b-',label='平均低温')
    plt.scatter(year,month_data.November_temperature_highest,s=20,color='red',marker='o',linewidth=2,alpha=0.8)
    plt.scatter(year,month_data.November_temperature_lowest,s=20,color='blue',marker='o',linewidth=2,alpha=0.8)
    plt.xlabel('年份')                          #设置x轴标签
    plt.ylabel('气温')               #设置y轴标签
    plt.xticks(fontsize=12)                     #调整x轴刻度标签大小
    plt.yticks(fontsize=12)                     #调整y轴刻度标签大小
    plt.legend()
    plt.title('2011-2020年西安市11月气温走势图')                  #设置图标题
    plt.rcParams['savefig.dpi'] = 600           #设置图片像素
    plt.savefig('./result_figure/monthly/plot/2011-2020年西安市11月气温走势图.png')     #保存图片

# 结果可视化
plot_temperature()  #120个月的月平均气温  
plot_AQI()          #120个月的月平均空气质量指数
plot_November_temperature() #10年每年11月的气温