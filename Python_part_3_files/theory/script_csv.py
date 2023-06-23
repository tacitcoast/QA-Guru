import csv

# with open('resources/username.csv', 'r') as csvfile:
#     csvfile = csv.reader(csvfile)
#     for row in csvfile:
#         print(row)

with open('resources/eggs.csv', 'w') as csvfile:
    csfile = csv.writer(csvfile, delimiter=',')
    csfile.writerow(['Jane', 'Jade'])
    csfile.writerow(['John', 'Jhoan'])