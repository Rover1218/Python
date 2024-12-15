import pandas as pd
df = pd.read_csv('data.csv')
print("\nOriginal Data:")
print(df)
df = df.drop(1)
df.loc[0, 'column_name'] = 'new_value'
df = df.reset_index(drop=True)
print("\nAfter deletion and update:")
print(df)
df.to_csv('data.csv', index=False)