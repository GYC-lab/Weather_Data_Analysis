# 导入第三方库
import requests
from bs4 import BeautifulSoup
import pandas as pd 

# 爬取网页
def get_html(url):
    try:                                        #检测try语句块中的错误，从而让except语句捕获异常信息并处理      
        r = requests.get(url, timeout = 10)     #使用requests爬取网页信息，并作超时处理
        r.raise_for_status()                    #如果响应状态码不是200就主动产生异常时停止程序
        status=r.status_code                    #获得响应状态码   
        print('status code:',status)  
        r.encoding = r.apparent_encoding        #获取网页的编码方式  
        return r.text
    except:
        return 'program exception!'             #try语句块中出现错误则输出程序异常
    
# 解析网页
def get_data(html):
    soup = BeautifulSoup(html,'html.parser')    #使用BeautifulSoup解析网页
    body  = soup.body                           #获取html网页主体部分
    data = body.find('table',class_="history-table")        #检索body中的div元素拿到class为c7d的内容
    table=data.find_all("tr")

    final_data=[]

    # 保存标题
    title=table[0].text
    title=title.split("\n")
    location=title.index('')
    del(title[location])
    final_data.append(title)

    # 保存数据
    for i in range(1,len(table)):
        data=table[i].text
        data=data.split("\n")
        location=data.index('')
        del(data[location])
        final_data.append(data)

    return final_data
    
#用format()将结果打印输出
def print_data(final_data,num):
    print("{:^10}\t{:^8}\t{:^8}\t{:^8}\t{:^8}".format('日期','天气','最高温度','最低温度','风级'))
    for i in range(num):    
        final = final_data[i]
        print("{:^8}\t{:^8}\t{:^8}\t{:^8}\t{:^8}".format(final[0],final[1],final[2],final[3],final[4]))

#用main()主函数将各个模块连接
def main():
    url = 'https://tianqi.2345.com/wea_history/57036.htm'
    html = get_html(url) # 获取网页信息
    final_data = get_data(html) # 数据
    df=pd.DataFrame(final_data[1:])
    df.columns = final_data[0]
    # print(data)
    df.to_csv('./result_data/data_daily.csv')
    print(final_data)
    print(len(final_data))

if __name__ == '__main__':
    main()