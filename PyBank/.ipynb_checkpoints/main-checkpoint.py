import os
import csv

PyBank_csv = os.path.join("Resources","budget_data.csv")

with open(PyBank_csv) as csvfile:
    csv_reader = csv.reader(csvfile, delimiter=",")