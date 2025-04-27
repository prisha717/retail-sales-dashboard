import pandas as pd

df = pd.read_csv('superstore.csv')

print(df.head())
print(df.info())

columns_to_drop = ['Country', 'State', 'City', 'Customer Name', 'Segment']
df.drop(columns=columns_to_drop, inplace=True, errors='ignore')

df.dropna(inplace=True)

df['Order Date'] = pd.to_datetime(df['Order Date'])
df['Ship Date'] = pd.to_datetime(df['Ship Date'])

df.to_csv('superstore.csv', index=False)

print("Data cleaned and saved.")