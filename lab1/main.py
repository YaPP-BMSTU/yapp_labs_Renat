from dataCSV import *
from statistic import *
from percent import *

def get_valid_filename():
    while True:
        filename = input("Enter file path: ")
        try:
            open(filename, 'r').close()
            return filename
        except FileNotFoundError:
            print("File not found. Please enter a valid file path.")

def get_valid_region(data_analyzer):
    while True:
        region = input("Enter region to filter: ")
        filtered_data = data_analyzer.filter_by_region(region)
        if filtered_data:
            return region
        else:
            print("Invalid region. Please enter a valid region.")

def get_valid_column_number(data_analyzer):
    while True:
        try:
            column_number = int(input("Enter the column number for statistics: "))
            if 0 <= column_number < len(data_analyzer.headers) and column_number != 1:
                return column_number
            else:
                print("Invalid column number. Please enter a valid column number.")
        except ValueError:
            print("Invalid column number format. Please enter a valid column number.")


def main():
    filename = get_valid_filename()
    try:
        analyzer = DataAnalyzer(filename)
    except MyException as e:
        print(e.message)
        return

    print("Data:")
    analyzer.display_table(analyzer.data)

    region = get_valid_region(analyzer)
    filtered_data = analyzer.filter_by_region(region)

    print("\nFiltered Data for Region '{}':".format(region))
    analyzer.display_table(filtered_data)

    column_number = get_valid_column_number(analyzer)
    stats_calculator = StatisticsCalculator(filtered_data)
    max_val, min_val, median, mean = stats_calculator.calculate_statistics(column_number)
    print("\nStatistics for column {}:".format(column_number))
    print("Max Value:", max_val)
    print("Min Value:", min_val)
    print("Median:", median)
    print("Mean:", mean)

    percentile_calculator = PercentileCalculator(filtered_data)
    percentiles = percentile_calculator.calculate_percentiles(column_number)
    print("\nPercentiles:")
    for p, percentile_value in enumerate(percentiles):
        print("Percentile {}%: {}".format(p * 5, percentile_value))

if __name__ == '__main__':
    main()