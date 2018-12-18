#!/usr/bin/env python3
"""tile.py:用来模拟铺砖问题的程序
__author__ = "Wenxiang.Guo"
__pkuid__  = "1800011767"
__email__  = "1450527589@qq.com"
"""

import turtle     #引入turtle模块

m = int(input())    #输入的m为地板的一个边
n = int(input())    #输入的n为地板的另一个边
a = int(input())    #输入的a为砖块的一个边
b = int(input())    #输入的b为砖块的另一个边

qiang = [[0]*m for _ in range(n)]       #在二维的列表中表示墙
ans = []                                #ans为空列表，这里用来放每种方法地板的坐标
rem = []                                #rem为空列表，这里用来记录种类，即记录ans的列表
def puzhuan(ans):                       #定义puzhuan函数
    """定义铺砖函数为所执行的函数，这里的变量为一个空列表
    通过迭代方法，得出所需列表，并且每次得到预期结果均被输出
    未铺砖的地板设为0，铺上的地板设为1，铺满后再拆，进行迭代"""
    if sum(qiang[i][j] for i in range(n) for j in range(m)) == m*n:         #假设所有地板对应数之和为m*n，可以认为全部铺满
        rem.append(ans.copy())                                              
        print(ans)
        return                               #若全部铺满，rem会记录下这个结果，输出该方案，并返回
    for i in range(n):                       
        for j in range(m):
            if qiang[i][j]==1:
                continue                     #对每一个qiang[i][j]遍历，如果显示铺上砖，则继续
            if j+a<=m and i+b<=n:            #如果这个点所在位置可以向后放下一块砖
                if sum([qiang[x][y]for y in range(j,j+a) for x in range(i,i+b)])==0:       #该点开始砖覆盖的位置全部都是0，说明可以放
                    temp = []
                    for x in range(i,i+b):
                        for y in range(j,j+a):
                            qiang[x][y] = 1            #令砖覆盖的点全部变成1
                            temp.append(x*m+y)         #temp中加入该点编号
                    ans.append(tuple(temp))            #ans中加入砖覆盖的点的编号
                    puzhuan(ans)                       #递归重复进行
                    for x in range(i,i+b):
                        for y in range(j,j+a):
                            qiang[x][y] = 0
                    ans.pop()                         #把砖块拆下来，使其覆盖点均变成0
            if j+b<=m and i+a<=n:                     #如果横排放不下，变成纵排
                if sum([qiang[x][y]for y in range(j,j+b) for x in range(i,i+a)])==0:
                    temp = []
                    for x in range(i,i+a):
                        for y in range(j,j+b):
                            qiang[x][y] = 1
                            temp.append(x*m+y)
                    ans.append(tuple(temp))           #纵排可以放下时就放砖并记录
                    puzhuan(ans)                      #继续递归
                    for x in range(i,i+a):
                        for y in range(j,j+b):
                            qiang[x][y] = 0
                    ans.pop()                         #拆砖
            return                                    #返回

if __name__ == "__main__":                            #执行主函数。即puzhuan函数
    puzhuan(ans)

bian = 600/max(m,n)             #定义边为600/m，n中最大值，保证图不会出界

len = len(rem)                  #定义len为方案个数
turtle.Screen()               #显示画屏
num = int (turtle .numinput("Input","Please print number 0~"+str(len-1)))         #在turtle中引入对话框
pick = rem[num]               #定义pick为所选的方案
t = turtle.Turtle()
p1 = turtle.Turtle()
p2 = turtle.Turtle()
p3 = turtle.Turtle()            #引入多个乌龟，t用来画方案，p1和p2用来画格，p3用来写编号


t.speed(7)                   #t的速度设为7
p1.speed(0)                  #p1速度设为最快
p2.speed(0)                  #p2速度设为最快
p3.speed(0)                  #p3速度设为最快


for i in range(m*n):                                       #遍历，根据编号移动p3位置，并写编号
    p3.up()
    p3.goto((i%m+0.35)*bian-300,(i//m+0.35)*bian-300)      #p3移动到该坐标
    p3.down()
    p3.write(i,font=("Times",18,"bold"))                   #p3写编号


for i in range(m+1):                                       #遍历，根据i先画竖线
    p1.up()
    p1.goto(i*bian-300,bian*n-300)                         #p1移动到边的一点
    p1.down()
    p1.goto(i*bian-300,-300)                               #p1画竖线
    
for i in range(n+1):                                      #遍历，根据i先画横线
    p2.up()      
    p2.goto(-300,i*bian-300)                              #p2移动到边一点
    p2.down()
    p2.goto(bian*m-300,i*bian-300)                        #p2画横线

for i in pick:                        #根据pick中的元素，找到每个砖块中最大和最小编号，并根据编号确定移动位置的坐标
    s = min(i)                          #每次遍历都进行调整
    l = max(i)
    x1 = (s%m)*bian-300
    y1 = (s//m)*bian-300
    x2 = (l%m+1)*bian-300
    y2 = (l//m+1)*bian-300              #根据每个i确定坐标，(x1,y1)最左下方点(x2,y2)最右上方点
    t.up()
    t.pensize(9)                      #改变t宽度，表示铺砖
    t.goto(x1,y1)
    t.down()
    t.goto(x1,y2)
    t.goto(x2,y2)
    t.goto(x2,y1)
    t.goto(x1,y1)                     #t围绕四个点画方形，即铺砖
