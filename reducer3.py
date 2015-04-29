#!/usr/bin/python

import sys

High_sales = 0
old_item = None

for line in sys.stdin:
    data_mapped = line.strip().split("\t")
    if len(data_mapped) != 2:
        continue

    curnt_item, sales = data_mapped

    if old_item and old_item != curnt_item:
        print old_item, "\t", High_sales
        old_item = curnt_item;
        High_sales = 0

    # Find Highest Value
    old_item = curnt_item
    sales =float(sales)
    if sales > High_sales:
        High_sales = float(sales)

if old_item != None:
    print old_item, "\t", High_sales

