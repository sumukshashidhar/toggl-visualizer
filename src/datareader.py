import pandas as pd





filepath = './samples/sample.csv'




class Reader:

    def __init__(self, filepath='./sample/sample.csv'):
        self.df = pd.read_csv(filepath)
    

    def get_full_dataframe(self):
        return self.df
    