import numpy as np
from  matplotlib import pyplot as  plt,rcParams
from sklearn.metrics import mean_absolute_error, median_absolute_error  
# 决策树回归
from sklearn import tree
DecisionTreeRegressor = tree.DecisionTreeRegressor()
# 线性回归
from sklearn import linear_model
LinearRegression = linear_model.LinearRegression()
# SVM回归
from sklearn import svm
SVR = svm.SVR()
# KNN回归
from sklearn import neighbors
KNeighborsRegressor = neighbors.KNeighborsRegressor()
# 随机森林回归
from sklearn import ensemble
RandomForestRegressor = ensemble.RandomForestRegressor(n_estimators=20)#这里使用20个决策树
# Adaboost回归
from sklearn import ensemble
AdaBoostRegressor = ensemble.AdaBoostRegressor(n_estimators=50)#这里使用50个决策树
# GBRT回归
from sklearn import ensemble
GradientBoostingRegressor = ensemble.GradientBoostingRegressor(n_estimators=100)#这里使用100个决策树
# Bagging回归
from sklearn.ensemble import BaggingRegressor
BaggingRegressor = BaggingRegressor()
# ExtraTree极端随机树回归
from sklearn.tree import ExtraTreeRegressor
ExtraTreeRegressor = ExtraTreeRegressor()

rcParams['font.family']='FangSong'  #设置字体形式（防止中文乱码）
rcParams['axes.unicode_minus']=False    #设置正常显示字符（显示负号）

model_name_set=['决策树回归','线性回归','SVM回归','KNN回归','随机森林回归','Adaboost回归','GBRT回归','Bagging回归','极端随机树回归']
model_set=[DecisionTreeRegressor,LinearRegression,SVR,KNeighborsRegressor,RandomForestRegressor,AdaBoostRegressor,GradientBoostingRegressor,BaggingRegressor,ExtraTreeRegressor]

# 计算回归模型的结果
def regression_model_compute(model,X_train,X_test,y_train,y_test):
    #将训练集代入到各个回归模型中
    clf=model.fit(X_train,y_train)              #对训练集进行回归
    prediction = clf.predict(X_test)            #对测试集计算预测值
    score = clf.score(X_test, y_test)           #对测试集计算R方
    Mean_Absolute_Error=mean_absolute_error(y_test, prediction)     #计算平均绝对误差
    Median_Absolute_Error=median_absolute_error(y_test, prediction) #计算中值绝对误差
    evalution=[score,Mean_Absolute_Error,Median_Absolute_Error]     #将3种模型性能评估指标
    return evalution,prediction

# 实现第i个回归模型的可视化
def regression_model_plot(i,prediction,score,y_test):
    plt.subplot(3,3,i)
    plt.plot(np.arange(len(prediction)), y_test,'go-',markersize=2,linewidth =1.0,label='实际值')
    plt.plot(np.arange(len(prediction)),prediction,'ro-',markersize=2,linewidth =1.0,label='预测值')
    plt.title('{}-score: {}'.format(model_name_set[i-1],score),fontsize=6)  
    plt.xticks(fontsize=4)
    plt.yticks(fontsize=4)
    plt.subplots_adjust(wspace=0.3,hspace=0.3)

# 比较9种回归模型
def regression_model_compare(X_train,X_test,y_train,y_test):
    score_set=[]
    Mean_Absolute_Error_set=[]
    Median_Absolute_Error_set=[]
    plt.figure()
    for i in range(1,len(model_set)+1):
        model=model_set[i-1]
        evaluation,prediction=regression_model_compute(model,X_train,X_test,y_train,y_test)
        score_set.append(evaluation[0])
        Mean_Absolute_Error_set.append(evaluation[1])
        Median_Absolute_Error_set.append(evaluation[2])
        regression_model_plot(i,prediction,evaluation[0],y_test)
        
    return score_set,Mean_Absolute_Error_set,Median_Absolute_Error_set