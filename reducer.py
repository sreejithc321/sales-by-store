#!/usr/bin/python

import sys

tot_sales = 0
prev_store = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    curnt_store, sales = data_mapped

    if prev_store and prev_store != curnt_store:
        print prev_store, "\t", tot_sales
        prev_store = curnt_store;
        tot_sales = 0

    prev_store = curnt_store
    tot_sales += float(sales)

if prev_store != None:
    print prev_store, "\t", tot_sales

