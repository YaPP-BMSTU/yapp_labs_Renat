import os

class validation:
    max_file_size = None
    def get_valid_filename():
        while True:
            filename = input("Enter file path: ")
            if not filename.endswith('.csv'):
                print("Invalid file format. Please provide a CSV file.")
                continue

            try:
                max_file_size = 8 * 1024 * 500
                file_size = os.path.getsize(filename)
                if file_size > max_file_size:
                    print("File is too large")
                    continue
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

