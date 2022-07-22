 # 导入第三方库
import AQI_data # 导入处理过的数据
import numpy as np
from matplotlib import pyplot as plt, rcParams              
from sklearn import model_selection #用于数据划分
from sklearn import ensemble # 随机森林回归

from sklearn.metrics import mean_absolute_error, median_absolute_error

rcParams['font.family']='FangSong'  #设置字体形式（防止中文乱码）
rcParams['axes.unicode_minus']=False    #设置正常显示字符（显示负号

Y = np.array(AQI_data.AQI)
X = np.array([AQI_data.PM25,AQI_data.PM10,AQI_data.SO2,AQI_data.NO2,AQI_data.CO,AQI_data.O3]).transpose()

# 划分数据
X_train, X_test, y_train, y_test = model_selection.train_test_split(X, Y, test_size=0.2, random_state=0)

# 查看训练集和测试集的大小
print('训练集大小:',X_train.shape[0])
print('测试集大小:',X_test.shape[0])

# 采用随机森林根据6种污染物对AQI进行回归
RandomForestRegressor = ensemble.RandomForestRegressor(n_estimators=120)#这里使用100个决策树
clf=RandomForestRegressor.fit(X_train,y_train)                                    #对训练集进行回归
prediction = clf.predict(X_test)                                #对测试集计算预测值
score = clf.score(X_test, y_test)                               #对测试集计算R方
Mean_Absolute_Error=mean_absolute_error(y_test, prediction)     #计算平均绝对误差
Median_Absolute_Error=median_absolute_error(y_test, prediction) #计算中值绝对误差

# 输出回归模型的R方值、平均绝对误差、中值绝对误差：
model_evaluation=[score,Mean_Absolute_Error,Median_Absolute_Error]

# 输出结果
print('R方：{:.4f}\t平均绝对误差：{:.4f}\t中值绝对误差：{:.4f}'.format(model_evaluation[0],model_evaluation[1],model_evaluation[2]))

# 绘图并保存
plt.plot(np.arange(len(prediction)), y_test,'go-',markersize=2,linewidth =0.5,label='实际值')
plt.plot(np.arange(len(prediction)),prediction,'ro-',markersize=2,linewidth =0.5,label='预测值')
plt.title('随机森林回归-score: {}'.format(score),fontsize=10.5)  
plt.xticks(fontsize=10.5)
plt.yticks(fontsize=10.5)
plt.subplots_adjust(wspace=0.3,hspace=0.3)
plt.legend(fontsize=10.5)  
plt.rcParams['savefig.dpi'] = 600 #图片像素
plt.savefig('./result_figure/AQI/regression/随机森林回归结果.png')

# 对2021年11月23日和24日两天的AQI进行预测
print('模型应用：')
new_pollute1=np.array(['61','146','12','52','0','12'])[:,np.newaxis].transpose()
new_pollute2=np.array(['57','193','9','47','0','5'])[:,np.newaxis].transpose()

new_prediction1=clf.predict(new_pollute1)
new_prediction2=clf.predict(new_pollute2)
print('2021年11月23日西安市的空气质量指数：{:.0f}'.format(new_prediction1[0]))     
print('2021年11月24日西安市的空气质量指数：{:.0f}'.format(new_prediction2[0]))     