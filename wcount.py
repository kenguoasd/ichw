#!/usr/bin/env python3

"""wcount.py: count words from an Internet file.

__author__ = "Wenxiang Guo"
__pkuid__  = "1800011767"
__email__  = "1800011767@pku.edu.cn"
"""
import urllib
import operator
import string
import sys
from urllib.request import urlopen

def removePunctuation(text):
    """定义函数removePunctuation，将text中的标点符号去掉
    """
    b = ''.join(c for c in text if c not in string.punctuation)   
    return b

def wcount(lines, topn=10):
    """统计网址中的单词个数，之后根据单词个数的多少从高到低排列， 
    输出前topn个单词以及对应的个数。
    其中lines为网址，topn为数字，代表前n个最多的单词
    """
    doc = urlopen(lines)                     #打开网址
    docstr0 = doc.read()                     #阅读
    docstr00 = docstr0.decode('utf-8')       #把字节流转化成字符串
    docstr1 = docstr00.lower()               #把字符串中的大写换成小写
    docstr = removePunctuation(docstr1)      #把字符串中的标点去掉
    list1 = docstr.split()                   #根据空格分割字符串成列表

    list0 = set(list1)                       
    list2 = list(list0)                      #获得所有单词的种类
    dir1 = {}                                #创建一个新字典
 
    for x in range(len(list2)):              
        dir1[list2[x]] = 0                   #字典值初始为0
        for y in range(len(list1)):
            if list2[x] == list1[y]:         #遍历list1所有单词，与list2种类相同的个数加1
                dir1[list2[x]] += 1          #用字典统计单词出现个数
    c = sorted(dir1,key=dir1.__getitem__,reverse=True)      #按键值从大到小排列
    if int(topn) > len(c):                  
        for i in range(len(c)):
            print (c[i],dir1[c[i]])          #如果输入topn大于字典长度，输出所有单词及其个数
    else:
        for i in range(int(topn)):
            print (c[i],dir1[c[i]])          #如果输入topn小于等于字典长度，输出前topn个单词及对应个数

if __name__ == '__main__':                   #运行主函数

    if  len(sys.argv) == 1:
        print('Usage: {} url [topn]'.format(sys.argv[0]))
        print('  url: URL of the txt file to analyze ')
        print('  topn: how many (words count) to output. If not given, will output top 10 words')
        sys.exit(1)                           #如果输入的sys.argv长度等于1，进行提示并退出
    else:
        if len(sys.argv) >2:
            topn = sys.argv[2]
            wcount(sys.argv[1],topn)          #如果输入的sys.argv长度大于2，可以带入第三个topn的值
        else:
            topn = 10
            wcount(sys.argv[1],topn)          #如果输入的sys.argv长度等于2，默认topn等于10
    try:                                      #运行错误进行检查
        web_file = urlopen(sys.argv[1])
        lines_byte = web_file.read()
        web_file.close()
        lines = bytes.decode(lines_byte)
        wcount(lines, topn)
    except urllib.request.URLError:
        sys.stdout.write('Web path unexist or denied request!')
    except ValueError:
        sys.stdout.write('Unsupported url format "{}" !'.format(sys.argv[1]))
    except Exception:
        sys.stdout.write('Other unpredictable error, please ensure the url starts with "http://" and check your spelling')
