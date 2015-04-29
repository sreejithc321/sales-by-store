#!/usr/bin/python

import sys

total_sales = 0
old_item = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    curnt_item, sales = data_mapped

    if old_item and old_item != curnt_item:
        print old_item, "\t", total_sales
        old_item = curnt_item;
        total_sales = 0

    old_item = curnt_item
    total_sales += float(sales)

if old_item != None:
    print old_item, "\t", total_sales

