import turtle
import math

t0=turtle.Turtle()
t1=turtle.Turtle()
t2=turtle.Turtle()
t3=turtle.Turtle()
t4=turtle.Turtle()
t5=turtle.Turtle()
t6=turtle.Turtle()

for i in (t0,t1,t2,t3,t4,t5,t6):
    i.shape('circle')
x=0
colors=['red','yellow', 'blue', 'green', 'orange','purple','brown']
for i in (t0,t1,t2,t3,t4,t5,t6):
    i.color(colors[x%7])
    i.up()
    i.goto(50+50*x,0)
    i.down()
    x=x+1

def b(a,c):
    b = (a ** 2 - c**2) ** 0.5
    return b
def r(d):
    r = d * math.pi / 180
    return r

while True:
    for i in range(360):
        c=50
        a=100
        t1.goto(a * math.cos(10*r(i)),b(a,c) * math.sin(10*r(i)))
        a=150
        t2.goto(a * math.cos(8*r(i)),b(a,c) * math.sin(8*r(i)))
        a=200
        t3.goto(a * math.cos(6*r(i)),b(a,c) * math.sin(6*r(i)))
        a=250
        t4.goto(a * math.cos(4*r(i)),b(a,c) * math.sin(4*r(i)))
        a=300
        t5.goto(a * math.cos(2*r(i)),b(a,c) * math.sin(2*r(i)))
        a=350
        t6.goto(a * math.cos(r(i)),b(a,c) * math.sin(r(i)))
                
