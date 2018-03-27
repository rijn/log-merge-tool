import csv
from os import listdir
from os.path import isfile, join

path = './logs/'

files = [f for f in listdir(path) if isfile(join(path, f))]

data = []

for file in files:
  with open(path + file, newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=',')
    for row in reader:
      data.append(row[1:])

base = data[0][3]
for row in data:
  row[3] = int(row[3]) - int(base)

data = sorted(data, key=lambda row: row[3])

with open('line_log.csv', 'w', newline='') as csvfile:
  writer = csv.writer(csvfile, delimiter=',')
  writer.writerow(['Client', 'Request', 'Key', 'Timestamp', 'Action', 'Value'])
  for row in data:
    writer.writerow(row);
