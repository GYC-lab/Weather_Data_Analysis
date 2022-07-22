# 导入第三方库
import requests                 #用于爬取网页
from bs4 import BeautifulSoup   #用于解析网页
import pandas as pd             #用于处理数据

# 格式化日期（年月）：用于实现网页翻页
def format_date_monthly(year,month):
    year_str=str(year)                          #将年份数据转化为字符串
    month_str=str(month)                        #将月份数据转化为字符串
    if month <=9:
        return str(year_str+'0'+month_str)      #若月份为个位数则在前面补0
    else:
        return str(year_str+month_str)

# print(format_date(2011,1))                    #函数测试，输出2011年1月的格式化日期

# 格式化日期（年月日）：用于结果保存
def format_date_daily(year,month,day):
    # 对个位数日期前补0
    if day<=9:
        date_daily=format_date_monthly(year,month)+str(0)+str(day)
    else:
        date_daily=format_date_monthly(year,month)+str(day)
    return date_daily

# print(format_date_daily(2011,11,1))                    #函数测试，输出2011年11月1日的格式化日期

# 输出要分析的日期（年月）：用于实现网页翻页
def all_date_monthly(years): 
    temp_data = []                              #使用列表保存临时数据
    for year in years:
        for month in range(1,13):               #遍历每天的天气数据
            temp_data.append(format_date_monthly(year,month))
    return temp_data

# print(all_date_montly(list(range(2016,2021))))       #函数测试：输出2016-2020年的所有月份

# 保存所有日期所在网页的超链接
def all_html(years):
    url_base="http://www.tianqihoubao.com/aqi/xian-"   #访问西安天气所在的网页
    url=[]                                      #建立列表来保存所有超链接
    date=all_date_monthly(years)                        #输入要爬取的年份，输出年份下所有的月份
    for each_month in date: 
        url.append(url_base+each_month+'.html')         #将每个年月信息转化为对应的超链接，即可通过该超链接来访问每个年下每个月的天气信息
    return url

# print(all_html(range(2016,2021)))             #函数测试：输出2016-2020年所有网页的超链接

# 爬取网页
def get_html(url):
    try:                                        #检测try语句块中的错误，从而让except语句捕获异常信息并处理      
        headers={                               #设置请求头
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'
		}
        r = requests.get(url, timeout = 10,headers=headers)     #使用requests爬取网页信息，并作超时处理
        r.raise_for_status()                                    #如果响应状态码不是200就主动产生异常时停止程序
        # print("status code:","{:3d}".format(r. status_code))   #获得响应状态码
        r.encoding = r.apparent_encoding                        #获取网页的编码方式  
        return r.text
    except:
        return 'program exception!'             #try语句块中出现错误则输出程序异常

# print(get_html('http://www.tianqihoubao.com/aqi/xian-201501.html'))    #函数测试：请问网页是否成功

# 解析所有网页
def get_data(years):
    date_set=all_date_monthly(years)                        #获得所有日期（年月）
    url_set=all_html(years)                         #获得所有超链接
    amount=len(date_set)                            #获得全部日期的个数

    final_data = []                                 #使用列表保存最终数据     

    for i in range(amount):                         #对每个月进行遍历
        print("analyzing {0}/{1} month".format(i+1,amount))   #打印当前进度
        date_monthly=date_set[i]                            #获得当前日期
        html=get_html(url_set[i])                   #获得当前日期天气信息所在的超链接
        soup = BeautifulSoup(html,'html.parser')    #使用BeautifulSoup解析网页
        body  = soup.body                           #获取html网页主体部分
        data = body.find('table',class_='b')        #检索body中的table元素拿到class为'b'的内容
        table = data.find_all("tr")                 #查找所有tr标签，即可得到当前月份下每天的空气质量数据
        
        # 对当前月下的每天进行遍历，获得每天的天气数据，最终得到28/29/30/31个子数据
        day_data=[]
        for j in range(1,len(table)):   
            # 对个位数日期前补0
            if j<=9:
                date_daily=date_monthly+str(0)+str(j)
            else:
                date_daily=date_monthly+str(j)
            print("\tanalyzing {0}/{1} day:{2}".format(j,len(table)-1,date_daily) )  #打印当前进度
            data=table[j].text          
            data=data.split("\n")
            data=data[5:]               #截取需要部分
            data[0]=data[0].replace("\r","")    #删除'/r'
            del(data[1])
            # PM25_location=data.index('245')
            for item in data:  #删除列表中的空字符串
                if item=='':
                    data.remove(item)
            day_data.append(data)

        final_data.extend(day_data)
        
    print('Crawl over!')
        
    return final_data

# print(get_data([2020]))           #函数测试，爬取、解析、输出2020年每月每日的空气质量数据

#用main()主函数将各个模块连接
def main():
    years=range(2016,2021)          #爬取2016年~2020年的天气数据
    final_data = get_data(years)    #解析并保存这5年的天气数据
    df=pd.DataFrame(final_data)     #将final_data列表转化为df数据框
    df.columns = ["AQI","AQI_rank","PM2.5","PM10","SO2","NO2","CO","O3"]  #设置列标题
    df.to_csv('./result_data/AQI_daily_new.csv')   #将数据保存到result_data文件夹下的.csv文件

if __name__ == '__main__':
    main()