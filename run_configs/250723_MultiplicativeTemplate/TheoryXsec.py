import pandas as pd

class TheoryXsec:
    def __init__(self, csv_basedir):
        self.csv_basedir = csv_basedir
    def GetXsec(self, var):
        csv_filepath = f'{self.csv_basedir}/xsec_{var}.csv'
        df = pd.read_csv(csv_filepath)
        return df['x_center'].to_numpy(), df['x_err'].to_numpy(), df['xsec'].to_numpy()