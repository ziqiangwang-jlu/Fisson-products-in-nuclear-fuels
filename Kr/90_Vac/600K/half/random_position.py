#! /public/home/ziqiangw/anaconda3/bin/python


import random
from math import *

x_1 = 13.67+random.uniform(-4.0, 4.0)
y_1 = 52.3817+random.uniform(-4.0, 4.0)
z_1 = 13.67+random.uniform(-4.0, 4.0)
while not sqrt(pow((x_1-13.67),2)+pow((y_1-52.3817),2)+pow((z_1-13.67),2))<=4.0:
    x_1 = 13.67+random.uniform(-4.0, 4.0)
    y_1 = 52.3817+random.uniform(-4.0, 4.0)
    z_1 = 13.67+random.uniform(-4.0, 4.0)

x_2 = 13.67+random.uniform(-4.0,4.0)
y_2 = 119.377+random.uniform(-4.0,4.0)
z_2 = 13.67+random.uniform(-4.0,4.0)
while not sqrt(pow((x_2-13.67),2)+pow((y_2-119.377),2)+pow((z_2-13.67),2))<=4.0:
    x_2 = 13.67+random.uniform(-4.0,4.0)
    y_2 = 119.377+random.uniform(-4.0,4.0)
    z_2 = 13.67+random.uniform(-4.0,4.0)

x_3 = 13.67+random.uniform(-4.0,4.0)
y_3 = 214.286+random.uniform(-4.0,4.0)
z_3 = 13.67+random.uniform(-4.0,4.0)
while not sqrt(pow((x_3-13.67),2)+pow((y_3-214.286),2)+pow((z_3-13.67),2))<=4.0:
    x_3 = 13.67+random.uniform(-4.0,4.0)
    y_3 = 214.286+random.uniform(-4.0,4.0)
    z_3 = 13.67+random.uniform(-4.0,4.0)

x_4 = 13.67+random.uniform(-4.0,4.0)
y_4 = 275.698+random.uniform(-4.0,4.0)
z_4 = 13.67+random.uniform(-4.0,4.0)
while not sqrt(pow((x_4-13.67),2)+pow((y_4-275.698),2)+pow((z_4-13.67),2))<=4.0:
    x_4 = 13.67+random.uniform(-4.0,4.0)
    y_4 = 275.698+random.uniform(-4.0,4.0)
    z_4 = 13.67+random.uniform(-4.0,4.0)

with open ('Xe_position.dat', 'w') as file:    
    file.write(str(x_1)+' '+str(y_1)+' '+str(z_1)+'\n')
    file.write(str(x_2)+' '+str(y_2)+' '+str(z_2)+'\n')
    file.write(str(x_3)+' '+str(y_3)+' '+str(z_3)+'\n')
    file.write(str(x_4)+' '+str(y_4)+' '+str(z_4)+'\n')
    

