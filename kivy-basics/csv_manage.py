import csv

searchfile = open('pincode_output.csv', 'rb')
reader = csv.reader(searchfile, delimiter = ',')
a = input()
for a in reader:
    print(a)