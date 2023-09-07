from csv import CSVparse
from tabulate import tabulate
class DataAnalyzer:
    def __init__(self, filename):
        csv = CSVparse(filename)
        result = csv.parsefile()

        if result:
            self.headers, self.data = result
        else:
            raise ValueError("Unable to parse the file.")

    def filter_by_region(self, region):
        filtered_data = [row for row in self.data if row[1] == region]
        return filtered_data

    def display_table(self, data):
        print(tabulate(data, headers=self.headers, tablefmt="pipe", stralign="center"))