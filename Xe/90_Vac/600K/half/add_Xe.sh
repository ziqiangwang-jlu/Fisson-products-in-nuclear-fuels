#! /bin/bash


random_position.py
sed '/Velocities/,$d' Xe_relaxed.dat > perfect.dat
new_num=$1

awk -v num=$new_num 'NR==3 {$1=num} {print}' perfect.dat > add_Xe.dat
Xe_1=$(awk -F' ' 'NR==1 {print $1, $2, $3}' Xe_position.dat)
Xe_2=$(awk -F' ' 'NR==2 {print $0}' Xe_position.dat)
Xe_3=$(awk -F' ' 'NR==3 {print $0}' Xe_position.dat)
Xe_4=$(awk -F' ' 'NR==4 {print $0}' Xe_position.dat)

num_3=$(($new_num-1))
num_2=$(($new_num-2))
num_1=$(($new_num-3))

sed -i "17 a $num_1 0 3 0.0 $Xe_1 0 0 0" add_Xe.dat
sed -i "17 a $num_2 0 3 0.0 $Xe_2 0 0 0" add_Xe.dat
sed -i "17 a $num_3 0 3 0.0 $Xe_3 0 0 0" add_Xe.dat
sed -i "17 a $new_num 0 3 0.0 $Xe_4 0 0 0" add_Xe.dat 
