# 导入第三方库
import requests                 #用于爬取网页
from bs4 import BeautifulSoup   #用于解析网页
import pandas as pd             #用于处理数据

# 格式化日期
def format_date(year,month):
    year_str=str(year)                          #将年份数据转化为字符串
    month_str=str(month)                        #将月份数据转化为字符串
    if month <=9:
        return str(year_str+'0'+month_str)      #若月份为个位数则在前面补0
    else:
        return str(year_str+month_str)

# print(format_date(2011,1))                    #函数测试，输出2011年1月的格式化日期

# 输出要分析的日期
def all_date(years): 
    temp_data = []                              #使用列表保存临时数据
    for year in years:
        for month in range(1,13):               #遍历每天的天气数据
            temp_data.append(format_date(year,month))
    return temp_data

# print(all_date(list(range(2011,2021))))       #函数测试：输出2011-2020年的所有月份

# 保存所有日期所在网页的超链接
def all_html(years):
    url_base="https://lishi.tianqi.com/xian/"   #访问西安天气所在的网页
    url=[]                                      #建立列表来保存所有超链接
    date=all_date(years)                        #输入要爬取的年份，输出年份下所有的月份
    for each_month in date: 
        url.append(url_base+each_month)         #将每个年月信息转化为对应的超链接，即可通过该超链接来访问每个年下每个月的天气信息
    return url

# print(all_html(range(2011,2021)))             #函数测试：输出2011-2020年所有网页的超链接

# 爬取网页
def get_html(url):
    try:                                        #检测try语句块中的错误，从而让except语句捕获异常信息并处理      
        headers={                               #设置请求头
		'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/34.0.1847.137 Safari/537.36 LBBROWSER'
		}
        r = requests.get(url, timeout = 10,headers=headers)     #使用requests爬取网页信息，并作超时处理
        r.raise_for_status()                                    #如果响应状态码不是200就主动产生异常时停止程序
        # print("status code:","{:3d}".format(r.status_code))   #获得响应状态码
        r.encoding = r.apparent_encoding                        #获取网页的编码方式  
        return r.text
    except:
        return 'program exception!'             #try语句块中出现错误则输出程序异常

# print(get_html('https://lishi.tianqi.com/xian/202002.html'))    #函数测试：请问网页是否成功

# 解析所有网页
def get_data(years):
    date_set=all_date(years)                        #获得所有日期
    url_set=all_html(years)                         #获得所有超链接
    amount=len(date_set)                            #获得全部日期的个数
    final_data = []                                 #使用列表保存最终数据       
    for i in range(amount):                         #对每个日期即每个月进行遍历
        date=date_set[i]                            #获得当前日期
        html=get_html(url_set[i])                   #获得当前日期天气信息所在的超链接
        soup = BeautifulSoup(html,'html.parser')    #使用BeautifulSoup解析网页

        #使用selector来定位和保存要爬取的天气信息，分别为平均高温，平均低温，平均空气质量指数
        temperature_highest_average=soup.select("body > div.main.clearfix > div.main_left.inleft > div.inleft_tian > ul > li:nth-child(1) > div:nth-child(1) > div.tian_twoa")[0].string
        temperature_lowest_average=soup.select("body > div.main.clearfix > div.main_left.inleft > div.inleft_tian > ul > li:nth-child(1) > div:nth-child(2) > div.tian_twoa")[0].string
        AQI_average=soup.select("body > div.main.clearfix > div.main_left.inleft > div.inleft_tian > ul > li:nth-child(4) > div.tian_twoa")[0].string
        
        temp_data=[date,temperature_highest_average,temperature_lowest_average,AQI_average]     #使用temp_data列表临时保存天气信息
        final_data.append(temp_data)                    #将temp_datafinal_data列表添加到final_data列表中
        print("analyzing:{0}/{1}".format(i+1,amount))   #打印当前进度

    print('done!')  #爬取结束

    return final_data

#用main()主函数将各个模块连接
def main():
    years=range(2011,2021)          #爬取2011年~2020年的天气数据
    final_data = get_data(years)    #解析并保存这十年的天气数据
    df=pd.DataFrame(final_data)     #将final_data列表转化为df数据框
    df.columns = ["日期","平均高温","平均低温","平均空气质量指数"]  #设置列标题
    df.to_csv('./result_data/data_monthly.csv')   #将数据保存到result_data文件夹下的.csv文件

if __name__ == '__main__':
    main()