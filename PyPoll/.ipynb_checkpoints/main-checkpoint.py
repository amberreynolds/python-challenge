import os
import csv

csvpath = os.path.join("Resources/election_data.csv")

with open(csvpath, newline="") as csvfile:
    csv_reader =csv.reader(csvfile, delimiter=",")
    csv_headers = next(csv_reader)