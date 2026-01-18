# Parameterizing your pipeline
import sys
import pandas as pd

# print('Arguments:', sys.argv)
month = int(sys.argv[1])

df = pd.DataFrame({"A": [1, 2], "B": [3, 4]})
df['month'] = month
print(df.head())

df.to_parquet(f'pipeline_{month}.parquet')

print(f'Hello pipeline, month = {month}')