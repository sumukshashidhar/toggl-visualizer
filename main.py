import src.datareader as datareader
import src.visualize as vs


data = datareader.Reader(filepath='data/1.csv')
data.clean()
data.export_cleaned()


data2 = datareader.Reader(filepath='data/1--clean.csv')
a = vs.Plot(data2.get_full_dataframe())
a.pie_plot()
