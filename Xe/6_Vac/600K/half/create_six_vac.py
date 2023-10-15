#! /public/home/ziqiangw/anaconda3/bin/python

import random
from read_lmp_dat import *
from distance import *
import numpy as np

system = Read_data('perfect_relaxed.dat')
tot_num = system.get_tot_num()
def check_distance(atom_id, id_list):
    return_value = 0
    for index in id_list:
        if get_distance(system.get_position(atom_id),system.get_position(index)) >6.0:
            pass
        else:
            return_value = 1
            break
    if return_value == 1:
        return False
    else:
        return True 

selected_list = []
oxygen_id_list = []
dict = {}
Th_elem_ls = []
while len(selected_list) < 120:
    atom_id = random.randint(1,tot_num)
    while not (system.get_type(atom_id) == 2 and check_distance(atom_id, selected_list)):
        atom_id = random.randint(1, tot_num)
    selected_list.append(atom_id)
    elem_num = 0
    value_list = []
    for id in range(1,tot_num+1):
        if system.get_type(id) == 1:
            if get_distance(system.get_position(atom_id), system.get_position(id)) < 2.5:
                elem_num = elem_num + 1
                if elem_num  >= 3:
                    break
                else:
                    if id not in oxygen_id_list:
                        value_list.append(id)
                        oxygen_id_list.append(id)
                        dict[atom_id] = value_list
                    else:
                        elem_num = elem_num - 1 
            else:
                pass
        else:
            pass

# Select the second Th atom
    second_id = random.randint(1, tot_num)
    while not (system.get_type(second_id)==2 and get_distance(system.get_position(second_id),system.get_position(atom_id))<=4.0 and second_id not in selected_list):
        second_id = random.randint(1, tot_num)
    selected_list.append(second_id)
    elem_num = 0
    value_list = []
    for id in range(1,tot_num+1):
        if system.get_type(id) == 1:
            if get_distance(system.get_position(second_id),system.get_position(id)) < 2.5:
                elem_num = elem_num + 1
                if elem_num >= 3:
                    break
                else:
                    if id not in oxygen_id_list:
                        value_list.append(id)
                        oxygen_id_list.append(id)
                        dict[second_id] = value_list
                    else:
                        elem_num = elem_num - 1
            else:
                pass
        else:
            pass 

    Th_tuple = (atom_id, second_id)
    Th_elem_ls.append(Th_tuple)    

Xe_id = []
for i in Th_elem_ls:
    index = random.randint(0,1)
    Xe_id.append(i[index])

key_list = []
for key, value in dict.items():
    key_list.append(key)
Th_id_array = np.array(key_list)
Oxygen_id_array = np.array(oxygen_id_list)

print('Th array shape: ', Th_id_array.shape, Th_id_array)
print('O array shape: ', Oxygen_id_array)
print('Xe id: ', len(Xe_id), np.array(Xe_id))
