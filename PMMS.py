import pandas as pd


col_names = ['week', '30yr FRM', '30 yr p&f', '15yr FRM', '15yr p&f', '5/1 ARM', '5/1 ARM p&f', '5/1 ARM margin',  '1yr ARM', '1yr ARM p&f', '1yr ARM margin', '30yr FRM 1yr ARM spread']
rates = pd.read_csv('PMMS2015.csv', names=col_names, header=0)

rates['30yr FRM'].plot()
