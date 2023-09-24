import pandas as pd


class LoadDataSet:
    def load(self, file: str, delimiter: str = ","):
        if len(delimiter) != 0:
            df = pd.read_csv(file, delimiter=delimiter, low_memory=False)
            return df
        else:
            df = pd.read_csv(file)
            return df
