#! /public/home/ziqiangw/anaconda3/bin/python


import numpy as np
import statistics
import os

size_list = [36,45,60,90,120]
for i in size_list:
    therm_condu_list = []
    os.chdir(str(i)+'_Vac/600K/one/thermal_condu')
    cwd = os.getcwd()
    print(cwd)
    with open ('thermal_conductivity.txt', 'r') as file:
        while True:
            line = file.readline()
            if len(line.split()) == 0:
                break
            else:
                therm_condu_list.append(float(line.split()[2]))
    standard_deviation = statistics.stdev(therm_condu_list)
    mean = np.mean(therm_condu_list)
    os.chdir('../../../../')
    with open ('mean_error.txt', 'a') as f:
        f.write(str(i)+'_Vac: '+str(mean)+' '+str(standard_deviation)+'\n')

     


