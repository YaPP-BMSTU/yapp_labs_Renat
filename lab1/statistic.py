import numpy as np
from exception import *
class StatisticsCalculator:
    def __init__(self, data):
        self.data = data

    def calculate_statistics(self, column_number):
        try:
            column_data = [float(row[column_number]) for row in self.data]
            max_value = max(column_data)
            min_value = min(column_data)
            median = np.median(column_data)
            mean = np.mean(column_data)
            return max_value, min_value, median, mean
        except (IndexError, ValueError):
            raise MyException("Invalid column number or data format.")