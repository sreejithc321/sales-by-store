#!/usr/bin/python

import sys

tot_sales = 0
tot_trans = 0.0

for line in sys.stdin:
    tot_sales = tot_sales + 1 
    tot_trans = tot_trans + float(line)
print tot_trans, "\t", tot_sales

