#---------------------------------------
#
# This script is used to calculate the thermal conuctivity of UO2 using Muller-Plathe method
# By Ziqiang Wang on 03/18/2022 on Jilin university
# 
#---------------------------------------

variable     Nevery    equal   50
variable     T         equal   600

clear
units          metal
boundary       p p p
atom_style     full

read_data vac_0.02_relaxed.dat

set           type     1    charge     -1.1104
set           type     2    charge      2.2208
set           type     3    charge      0.0

kspace_style                pppm     1.0e-05
pair_style                  hybrid/overlay  coul/long   11.0  eam/alloy  table  linear  1000  pppm
pair_coeff                  * * coul/long
pair_coeff                  * * eam/alloy CeThUNpPuAmCmO.eam.alloy O Th NULL
pair_coeff                  3 3 table CRG_gas_potentials.lmptab Xe-Xe 11
pair_coeff                  1 3 table CRG_gas_potentials.lmptab Xe-O 11
pair_coeff                  2 3 table CRG_gas_potentials.lmptab Xe-Th 11
neighbor                    2.0  bin
neigh_modify                every  1  delay  0  check  yes

#The first equilation
velocity        all create $T 10004 mom yes rot yes dist gaussian
fix             nvt  all  nvt  temp  $T $T  0.1

run             100000
unfix           nvt
reset_timestep  0

# the second run
fix             1 all nve

group           oxygen type 1
fix             2 oxygen thermal/conductivity ${Nevery} y 20

compute         ke all ke/atom
variable        temp atom c_ke/1.5
compute         layers all chunk/atom bin/1d y lower 0.05 units reduced
fix             3      all ave/chunk  2000 50 100000 layers v_temp file profile_${T}K.mp

variable        Tdiff    equal     f_3[11][3]-f_3[1][3]
variable        deltaT   equal     v_Tdiff*1.5/0.0001292

timestep        0.001
thermo_style    custom step f_2 temp v_Tdiff v_deltaT
thermo          100000

run             1000000

