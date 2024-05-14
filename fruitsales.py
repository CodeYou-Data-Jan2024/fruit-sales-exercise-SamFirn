import pandas as pd


fruit_sales_by_year = pd.DataFrame({'Apples': [35,41], 'Bananas': [21,34]}, index = ['2017 Sales', '2018 Sales'])
fruit_sales_by_year.to_csv('fruit.csv')
print(fruit_sales_by_year)
