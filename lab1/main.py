from csv import *
from tabulate import tabulate
from regiondata import *

filename = input("Enter file path: ")
csv = CSVparse(filename)
analyzer = DataAnalyzer(filename)
result = csv.parsefile()

if result:
    headers, data = result
    print("Headers:", headers)
    print("Data:")
    try:
        print(tabulate(data, headers=headers, tablefmt="pipe", stralign="center"))
    except TypeError:
        print("Invalid data format.")

    region = input("Enter region to filter: ")
    filtered_data = analyzer.filter_by_region(region)
    if filtered_data:
        print("Filtered Data:")
        analyzer.display_table(filtered_data)
    else:
        print("No data available for the specified region.")
else:
    print("Unable to parse the file.")
