#!/bin/bash

cd
cd VLSI_Design/assignment_1


echo "Running ngspice..........."
ngspice part_1.cir &
pid1=&!
sleep 13
kill $pid1

echo "Running python script.........."
python3 plot.py
pid2=&!
sleep 2
kill $pid2
