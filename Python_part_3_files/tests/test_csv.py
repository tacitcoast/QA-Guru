import csv
import os.path
from .conftest import path_res


def test_csv():
    with open(os.path.join(path_res, 'username.csv'), 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(os.path.join(path_res, 'username.csv')) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)
    assert len(row) == 3
