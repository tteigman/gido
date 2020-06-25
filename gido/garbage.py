import pandas as pd


class Garbage(object):
    column_processors = {}

    def __init__(self, df):
        self.df = df

    def add_column_processor(self, processor):
        self.column_processors[processor.__class__.__name__] = processor

    def compute_columns(self):
        names = [p.evaluate(self.df) for p in self.column_processors.values()]
        return names
