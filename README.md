## Sales by store calculation on Hadoop (Cloudera CDH)

- Sample input data format

    - 2012-01-01	09:00	San Jose	Men's Clothing	214.05	Amex
    - 2012-01-01	09:00	Fort Worth	Women's Clothing	153.57	Visa
    - 2012-01-01	09:00	San Diego	Music	66.08	Cash
    - 2012-01-01	09:00	Pittsburgh	Pet Supplies	493.51	Discover


- mapper.py : read store and sales data from input file

- reducer.py : calculate sales per store
