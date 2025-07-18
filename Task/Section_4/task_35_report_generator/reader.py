import csv
def read_csv(file):
    with open(file) as f:
        return list(csv.DictReader(f))
