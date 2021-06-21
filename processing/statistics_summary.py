
class Statistics:
    def __init__(self, mean, median, std, mode, max, min, count, kurt, sum, unique, var, sem) -> None:
        self.mean = mean
        self.median = median
        self.std = std
        self.mode = mode
        self.max = max
        self.min = min    
        self.count = count
        self.kurt = kurt
        self.sum = sum
        self.unique = unique
        self.var = var
        self.sem = sem              


def compute_correlation(df):
    return df.corr()

def compute_column_stats(df):
    stats_columns = {}
    for column in df:
        
        if(df[column].dtype == 'float64' or df[column].dtype == 'int64'):
            stats = Statistics(df[column].mean(),
                    df[column].median(),
                    df[column].std(),
                    df[column].mode(),
                    df[column].max(),
                    df[column].min(),
                    df[column].count(),
                    df[column].kurtosis(),
                    df[column].sum(),
                    df[column].unique(),
                    df[column].var(),
                    df[column].sem())

        stats_columns.put(column, stats)
            
    return stats_columns   
        