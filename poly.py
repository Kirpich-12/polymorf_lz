#Deros.All rights reserved
#=======================

import pandas as pd 

class Bank:
    def __init__(self, csv):
        self.csv = csv
        self.df = pd.read_csv(self.csv)

    def __neg__(self):
         return self.df.drop_duplicates()
    
    def razd(self):
        df = Bank('var4.csv')
        df = -df
        df1 = df[df['Вид расчета'] == 'наличный']    # строки, удовлетворяющие условию
        df2 = df[df['Вид расчета'] == 'безналичный']    # строки, не удовлетворяющие условию
        print(f'nal:{df1}, anal:{df2}, kol-vo:{100000 - (len(df1) + len(df2))}')

    def __del__():
        print('This xren has been deleted')
    

b = Bank('var4.csv')
b.razd()