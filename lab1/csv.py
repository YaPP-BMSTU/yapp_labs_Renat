class CSVparse:
    def __init__(self, filename):
        self.filename = filename

    def readfile(self):
        try:
            with open(self.filename) as f:
                data = f.read()
                return data

        except FileNotFoundError:
            print("File not found.")

    def parsefile(self):
        csv_string = self.readfile()
        if csv_string:
            lines = csv_string.split('\n')
            headers = lines[0].split(',')
            data = [line.split(',') for line in lines[1:]]

            return headers, data

        else:
            print("No data to parse.")
            return None
