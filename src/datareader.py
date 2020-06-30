import pandas as pd

filepath = './../samples/sample.csv'


df = pd.read_csv(filepath)

print(df.head())