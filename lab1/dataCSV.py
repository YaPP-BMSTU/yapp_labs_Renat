from tabulate import tabulate
from exception import *
class DataAnalyzer:
    def __init__(self, filename):
        self.filename = filename
        self.headers, self.data = self.parse_csv()

    def parse_csv(self):
        try:
            with open(self.filename, 'r') as file:
                lines = file.readlines()
                headers = lines[0].strip().split(',')
                data = [line.strip().split(',') for line in lines[1:]]
                for row in data:
                    if len(row) != 7:
                        raise MyException("Error. line word break")
                    if all(cell.strip() == '' for cell in row):
                        raise MyException("Error. Empty line found")
                return headers, data
        except FileNotFoundError:
            raise MyException("File not found.")
        except IndexError:
            raise MyException("No data to parse.")

    def filter_by_region(self, region):
        filtered_data = [row for row in self.data if row[1] == region]
        return filtered_data

    def display_table(self, data):
        print(tabulate(data, stralign="center"))
