import plotly.express as px


class Plot:

    def __init__(self, dataframe):
        self.df = dataframe
    

    def pie_plot(self):
        fig = px.pie(self.df, values='Duration', names='Description')
        fig.show()