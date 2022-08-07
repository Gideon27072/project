import csv 

with open('sample.csv') as sample_csv:
    file_reader = csv.reader(sample_csv, delimiter=',')
    
for row in file_reader:
        print(',  '.join(row))
    