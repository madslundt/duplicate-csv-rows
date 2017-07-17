import csv
import os
import sys
from math import fabs

def loadCSV(file_path, delimiter):
    f = open(file_path, 'r')
    reader = csv.DictReader(f, delimiter=delimiter)
    return reader.fieldnames, list(reader)

def duplicateCSVRows(csv_path, column_name, output_path, separator):
    columns, rows = loadCSV(csv_path, separator)

    print columns

    with open(output_path, 'w+') as f:
        csvWriter = csv.DictWriter(f, fieldnames=columns, delimiter=separator)
        csvWriter.writeheader()
        for row in rows:
            number = 0
            try:
                number = int(row[column_name])
            except ValueError:
                csvWriter.writerow(dict(row))
                continue

            row[column_name] = 1

            if (number < 0):
                row[column_name] = -1


            number = int(fabs(number))

            for i in xrange(1, number + 1):
                csvWriter.writerow(dict(row))


def main():
    csv_path = raw_input('Enter path to the CSV: ')
    column_name = raw_input('Enter the name of the column to look for in the CSV: ')

    output_path = raw_input('Where to output the duplicated CSV file? ')

    separator = raw_input('How do you separate CSV files [;]? ') or ';'

    duplicateCSVRows(csv_path, column_name, output_path, separator)


if __name__ == "__main__":
    main()
