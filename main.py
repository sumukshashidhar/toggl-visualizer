import src.datareader as datareader
import src.visualize as vs
data = datareader.Reader(filepath='data/1.csv')


print(data.get_full_dataframe())

data.clean()
data.export_cleaned()


data2 = datareader.Reader(filepath='data/1--clean.csv')
print(data2.get_full_dataframe())


a = vs.Plot(data2)
a.pie_plot()