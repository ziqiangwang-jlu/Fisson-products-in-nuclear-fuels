#! /public/home/ziqiangw/anaconda3/bin/python

from irradiation_GB_Cu import *

data = []
with open ('mean_error.txt', 'r') as file:
    x=[]
    y=[]
    e=[]
    for i in range(5):
        line = file.readline()
        ls = line.split()
        x.append(int(ls[0].split('_')[0]))
        y.append(float(ls[1]))
        e.append(float(ls[-1]))
    data.append((x,y,e))
    x=[]
    y=[]
    e=[]
    for i in range(5):
        line = file.readline()
        ls = line.split()
        x.append(int(ls[0].split('_')[0]))
        y.append(float(ls[1]))
        e.append(float(ls[-1]))
    data.append((x,y,e))
    x=[]
    y=[]
    e=[]
    for i in range(5):
        line = file.readline()
        ls = line.split()
        x.append(int(ls[0].split('_')[0]))
        y.append(float(ls[1]))
        e.append(float(ls[-1]))
    data.append((x,y,e))
MultipleTwoVariableErrorBar(data, saveto='Kr_bubbles',legend=['Empty voids','Half-filled Kr bubbles','Full-filled Kr bubbles'],labels=['Cluster size(number of atoms)','Thermal conductivity(W/m/K)'])
