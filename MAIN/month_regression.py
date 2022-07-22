 # 导入第三方库
import month_data # 导入处理过的数据
import regression_model as rm #调用回归模型及函数
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd                 
from sklearn import model_selection #用于数据划分

# 导入数据
def load_data(amount,variate):
    X = np.array(range(1,amount+1))
    X=X[:,np.newaxis]
    Y = np.array(variate)
    return X,Y  

# 回归天气数据
def regression_weather(date,weather,name):
    
    print('以下是对{}的回归：'.format(name))

    X,Y = load_data(date,weather)

    # 划分数据
    X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.25, random_state=0)
    
    # 查看训练集和测试集的大小
    print('训练集大小:',X_train.shape[0])
    print('测试集大小:',X_test.shape[0])

    # 比较9种回归模型
    score_set,Mean_Absolute_Error_set,Median_Absolute_Error_set=rm.regression_model_compare(X_train,X_test,y_train,y_test)
    
    # 输出各个回归模型的R方值：
    model_evaluation=[]
    for i in range(9):
        model_evaluation.append([rm.model_name_set[i],score_set[i],Mean_Absolute_Error_set[i],Median_Absolute_Error_set[i]])
    df = pd.DataFrame(model_evaluation, columns=['model', 'score','Mean Absolute Error','Median Absolute Error']) 
    
    # 输出结果
    pd.set_option('display.unicode.ambiguous_as_wide', True)
    pd.set_option('display.unicode.east_asian_width', True)
    print(df)
    score_max=max(score_set)
    score_max_index=score_set.index(score_max)
    print('回归模型性能最好的是:[{}]{}\n'.format(score_max_index,rm.model_name_set[score_max_index]))
    
    # 绘图并保存
    plt.legend(loc=2, bbox_to_anchor=(1.05,1.0),borderaxespad = 0.,fontsize=5)  
    plt.rcParams['savefig.dpi'] = 600 #图片像素
    plt.savefig('./result_figure/monthly/regression/9种回归模型对比_{}.png'.format(name))

    return df,score_max,score_max_index #返回结果

regression_weather(month_data.date_amount,month_data.temperature_highest,month_data.name[0])    #回归120个月的月平均高温
regression_weather(month_data.date_amount,month_data.temperature_lowest,month_data.name[1])     #回归120个月的月平均低温    