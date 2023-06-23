import csv
import os.path


def test_csv():
    with open(os.path.abspath('../resources/username.csv'), 'w') as csvfile:
        csvwriter = csv.writer(csvfile, delimiter=',')
        csvwriter.writerow(['Anna', 'Pavel', 'Peter'])
        csvwriter.writerow(['Alex', 'Serj', 'Yana'])

    with open(os.path.abspath('../resources/username.csv')) as csvfile:
        csvreader = csv.reader(csvfile)
        for row in csvreader:
            print(row)
    assert len(row) == 3