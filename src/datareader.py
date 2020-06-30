import pandas as pd





filepath = './samples/sample.csv'




class Reader:

    def __init__(self, filepath='./samples/sample.csv'):
        self.df = pd.read_csv(filepath)
        self.filepath = filepath

    def get_full_dataframe(self):
        return self.df


    def clean(self):
        self.df.drop(columns=['User', 'Email', 'Client', 'Billable', 'Tags', 'Amount ()'], inplace=True)

    
    def export_cleaned(self):
        self.df.to_csv(self.filepath[:-4]+'--clean.csv')