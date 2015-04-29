## Sales by store calculation on Hadoop (Cloudera CDH)

#### From MOOC - Intro to Hadoop and MapReduce : Udacity

- Sample input data format

    - 2012-01-01	09:00	San Jose	Men's Clothing	214.05	Amex
    - 2012-01-01	09:00	Fort Worth	Women's Clothing	153.57	Visa
    - 2012-01-01	09:00	San Diego	Music	66.08	Cash
    - 2012-01-01	09:00	Pittsburgh	Pet Supplies	493.51	Discover

### Find Sales per Store
- mapper.py : read store and sales data from input file
- reducer.py : calculate sales per store

### Find Sales per Category
- mapper2.py : read ite and sales data from input file
- reducer2.py : calculate sales per item

### Find the monetary value for the highest individual sale for each separate store
- mapper3.py
- reducer3.py

### Find the total sales value across all the stores, and the total number of sales. Assume there is only one reducer.
- mapper4.py
- reducer4.py
