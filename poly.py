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
        print(100000 - (len(df1) + len(df2)),  'строк удалено')
        df1.to_csv('df1.csv')
        df2.to_csv('df2.csv')
        

    def __del__(self):
        print('This bank has been deleted')


def main():
    b = Bank('var4.csv')
    b.razd()

if __name__ == '__main__':
    main()