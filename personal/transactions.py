import pandas as pd

df = pd.read_csv(
    'C:/Users/devg2/OneDrive - Daniel Vargas/transactions_download/transactions.csv')

df = df[['ID', 'OData__x0075_pb1', 'Description', 'Amount',
         'GST', 'QST', 'Category', 'Month', 'Total_x0020_Amount']]

df.columns = ['ID', 'Date', 'Description', 'Amount',
              'GST', 'QST', 'Category', 'Month', 'Total_Amount']

df1 = df['Category'].str.split(',', expand=True)
df2 = df1[2].str.split(':', expand=True)
df2[1] = df2[1].str.replace('"', '')
df2[1] = df2[1].str.replace('}', '')

df['Category'] = df2[1]

print(type(df['Category']))
print(df['Category'])

df.to_excel(
    'C:/Users/devg2/OneDrive - Daniel Vargas/transactions_download/transactions.xlsx')
