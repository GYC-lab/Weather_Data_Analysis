import AQI_data # 导入处理过的数据
from matplotlib import pyplot as plt, rcParams
import numpy as np

rcParams['font.family']='FangSong'  #设置字体形式（防止中文乱码）
rcParams['axes.unicode_minus']=False    #设置正常显示字符（显示负号

# 数据可视化
def plot_item(item,name):
    plt.figure()
    x=list(np.arange(1,AQI_data.date_amount+1).astype(dtype=np.str_))
    plt.plot(x,item,label='{}'.format(name),linewidth=0.5)
    # plt.scatter(x,item,s=20,color='blue',marker='o',linewidth=2,alpha=0.8)
    plt.xlabel('天数')    #设置x轴标签
    plt.ylabel('{}'.format(name))    #设置x轴标签
    plt.xticks(range(0,AQI_data.date_amount,500),fontsize=12)
    plt.yticks(fontsize=12) #调整y轴刻度标签大小
    plt.title('2016年-2020年西安市每日{}变化走势图'.format(name))
    plt.legend()
    # plt.show()            #显示图片
    plt.rcParams['savefig.dpi'] = 600              #设置图片像素
    plt.savefig('./result_figure/AQI/plot/2016年-2020年西安市每日{}变化走势图.png'.format(name))         #保存图片

for i in range(len(AQI_data.title)):
    plot_item(AQI_data.air_quality[i],AQI_data.title[i])