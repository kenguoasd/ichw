#!/usr/bin/env python3
"""currency.py:用来进行货币的换算的一个函数

__author__ = "Wenxiang.Guo"
__pkuid__  = "1800011767"
__email__  = "1450527589@qq.com"
"""
from urllib.request import urlopen    #如作业说明，在Python中访问URL
a = input()    #a为输入的第一个变量
b = input()    #b为输入的第二个变量
c = input()    #c为输入的第三个变量
def exchange(currency_from, currency_to, amount_from):    #定义所需要的exchange函数，括号里为三个变量
    """Returns: amount of currency received in the given exchange.

    In this exchange, the user is changing amount_from money in 
    currency currency_from to the currency currency_to. The value 
    returned represents the amount in currency currency_to.

    The value returned has type float.

    Parameter currency_from: the currency on hand
    Precondition: currency_from is a string for a valid currency code

    Parameter currency_to: the currency to convert to
    Precondition: currency_to is a string for a valid currency code

    Parameter amount_from: amount of currency to convert
    Precondition: amount_from is a float"""


    cf = currency_from    #把第一个自变量currency_from换成简单的cf
    ct = currency_to      #把第二个自变量currency_to换成简单的ct
    af = amount_from      #把第三个自变量amount_from换成简单的af
    web = 'http://cs1110.cs.cornell.edu/2016fa/a1server.php?from='+cf+'&to='+ct+'&amt='+af    #这是把三个自变量输入到网址中得到一个字符
    doc = urlopen(web)     #如作业说明所讲访问这个网页
    docstr = doc.read()    #如作业说明
    doc.close()            #如作业说明
    jstr = docstr.decode('ascii')      #通过ascii码进行转化
    s = jstr.split(':')[2]             #将所得字符串以：分割并取第三部分
    q = eval(s)[0]                     #将所取部分换成列表格式并取第一部分
    p = q.split()[0]                   #将所得到的浮点数+空格+字母按空格分开并提取数字

    return(p)                          #得到所需数字
print(exchange(a,b,c))               #执行函数


def testa():
     """定义一个用来检查exchange函数的函数"""
     assert(str(17.13025) == exchange('USD','CNY','2.5'))    #判断前后是否相同

def testall():
    """定义一个检查所有的函数（这里就一个）"""
    testa()                         #执行函数testa()
    print('It tests passed')        #输出字符
testall()                           #执行testall()
