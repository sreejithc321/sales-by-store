## Sales by store Calculation on Hadoop (Cludera CDH)

- Sample input data format

    2012-01-01	09:00	San Jose	Men's Clothing	214.05	Amex
    2012-01-01	09:00	Fort Worth	Women's Clothing	153.57	Visa
    2012-01-01	09:00	San Diego	Music	66.08	Cash
    2012-01-01	09:00	Pittsburgh	Pet Supplies	493.51	Discover


- mapper.py : Read store and sales data from input file

- reducer.py : Calculate sales per store
