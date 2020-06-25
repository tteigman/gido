import pandas as pd


class StatsBase(object):
    def _compute(self, df, val_df):
        self.val_df = val_df
        column_stats = pd.DataFrame()
        column_stats["count"] = df.notna().sum()
        column_stats["min_len"] = val_df.min()
        column_stats["max_len"] = val_df.max()

        column_stats["min_count"] = (val_df == column_stats["min_len"]).sum()
        column_stats["max_count"] = (val_df == column_stats["max_len"]).sum()

        min_max_count = column_stats[["min_count", "max_count"]]
        row_count = column_stats["count"].max()
        column_stats["rows_less_min_max"] = row_count - min_max_count.sum(axis=1)

        most_freq = column_stats["rows_less_min_max"].value_counts().idxmax()
        column_stats["likely_header"] = column_stats["rows_less_min_max"] == most_freq

        min_or_max = column_stats[["min_count", "max_count"]].idxmin(axis=1)
        column_stats.loc[min_or_max == "min_count", "likely_header_len"] = column_stats[
            "min_len"
        ]
        column_stats.loc[min_or_max == "max_count", "likely_header_len"] = column_stats[
            "max_len"
        ]
        column_matrix = (val_df == column_stats["likely_header_len"]) & column_stats[
            "likely_header"
        ]
        self.column_stats = column_stats
        self.column_matrix = column_matrix
        return self.__class__.__name__


class FreqCount(StatsBase):
    """
    Uses the frequency count on the column axis as a method of 
    """

    def evaluate(self, df):
        """
        Uses frequency count of a string in the column
        """

        def get_freq(s):
            return s.map(s.value_counts())

        val_df = df.apply(get_freq)
        return self._compute(df, val_df)


class StringMethod(StatsBase):
    def __init__(self, method, char=True):
        self.method = method
        self.char = char

    def evaluate(self, df):
        """
        Uses frequency count as a feature.
        """

        def count_instances(string):
            return sum(map(self.method, string))

        if self.char:
            val_df = df.fillna("").astype(str).applymap(count_instances)
        else:
            val_df = df.fillna("").astype(str).applymap(self.method)
        return self._compute(df, val_df)


class StrLength(StatsBase):
    """
    TODO inherit from String Method
    """

    def evaluate(self, df):
        """
        String length as a feature.
        """
        val_df = df.fillna("").astype(str).applymap(len)
        return self._compute(df, val_df)
