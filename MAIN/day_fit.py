import day_data # 导入处理过的数据
import numpy as np
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn import linear_model
from matplotlib import pyplot  as plt,rcParams

rcParams['font.family']='FangSong'  #设置字体形式（防止中文乱码）
rcParams['axes.unicode_minus']=False    #设置正常显示字符（显示负号）

# 计算标准误差（均方根误差）
def stdError_func(y_test, weather):
    return np.sqrt(np.mean((y_test-weather)**2))

# 计算R方
def R2_func(y_test, weather):   
    return 1-((y_test-weather)**2).sum() / ((weather.mean() - weather)**2).sum()

# 导入数据
def load_data(amount,variate):
    X = np.array(range(1,amount+1))
    # X=X[:,np.newaxis]
    Y = np.array(variate)
    return X,Y  

# 拟合天气数据
def daily_weather_fit(amount,weather,weather_name,i):
    
    print('以下是对{}的多项式拟合:'.format(weather_name))

    # 绘制20天天气数据的散点图
    plt.figure(i)
    plt.scatter(amount, weather, s=30, color='red',marker='x',alpha=0.8)

    degrees = list(range(2,14)) #多项式最高次数从2变化到13
    
    strError_set=[]
    for degree in degrees:
        clf = Pipeline([('poly', PolynomialFeatures(degree=degree)), ('linear', linear_model.LinearRegression(fit_intercept=False))])   #采用多项式拟合
        clf.fit(amount[:, np.newaxis],  weather)               #自变量需要二维数组
        predict_y =  clf.predict(amount[:, np.newaxis])  #计算预测值
        strError = stdError_func(predict_y, weather)      #计算标准误差
        R2 = R2_func(predict_y, weather)                  #计算R方
        score = clf.score(amount[:, np.newaxis], weather)      #采用sklearn中自带的模型评估，即R方
        strError_set.append(strError)
        print ('degree={}: strError={:.2f}, R2={:.2f}, clf.score={:.2f}'.format(degree, strError,R2,score)) #输出结果

    #查找标准误差最小值对应的多项式最高次数
    min_error=min(strError_set)
    min_error_index=strError_set.index(min_error)
    degree_optim=degrees[min_error_index]
    print('拟合最优结果:{}次多项式拟合\n'.format(degree_optim))

    clf = Pipeline([('poly', PolynomialFeatures(degree=degree_optim)), ('linear', linear_model.LinearRegression(fit_intercept=False))])   #采用多项式拟合
    clf.fit(amount[:, np.newaxis],  weather)                        #自变量需要二维数组
    predict_y =  clf.predict(amount[:, np.newaxis])                 #计算预测值
    plt.plot(amount, predict_y, linewidth=2, label=degree_optim)    #实际值和预测值可视化
    plt.legend()
    plt.title('2021年11月1日-11月20日西安市{}拟合结果'.format(weather_name))                                    #设置图标题
    # plt.show()
    plt.rcParams['savefig.dpi'] = 600                                                                         #设置图片像素
    plt.savefig('./result_figure/daily/fit/2021年11月1日-11月20日西安市{}拟合结果.png'.format(weather_name))    #保存图片

# 载入天气数据
amount,temperature_highest = load_data(day_data.date_amount,day_data.temperature_highest)
amount,temperature_lowest = load_data(day_data.date_amount,day_data.temperature_lowest)
amount,wind_power = load_data(day_data.date_amount,day_data.wind_power)
amount,AQI = load_data(day_data.date_amount,day_data.AQI)

# 拟合天气数据
daily_weather_fit(amount,temperature_highest,day_data.weather_name[0],1)    #拟合最高温
daily_weather_fit(amount,temperature_lowest,day_data.weather_name[1],2)     #拟合最低温
daily_weather_fit(amount,wind_power,day_data.weather_name[2],3)             #拟合风力等级
daily_weather_fit(amount,AQI,day_data.weather_name[3],4)                    #拟合空气质量指数