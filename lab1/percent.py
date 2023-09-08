from exception import *
import numpy as np
class PercentileCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_percentiles(self, column_number):
        try:
            column_data = [float(row[column_number]) for row in self.data]
            percentiles = [np.percentile(column_data, p) for p in range(0, 101, 5)]
            return percentiles
        except (IndexError, ValueError):
            raise MyException("Invalid column number or data format.")