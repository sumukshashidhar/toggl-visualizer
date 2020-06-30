import src.datareader as datareader

data = datareader.Reader(filepath='data/1.csv')


print(data.get_full_dataframe())

data.clean()
data.export_cleaned()