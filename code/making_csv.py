import csv


filename = 'testing.csv'

with open(filename, 'w', newline = '') as csvfile:
    fieldnames = ["a", "b"]
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
    
    writer.writeheader()
    writer.writerow({'a': 'Baked', 'b': 'Beans'})

with open(filename, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    
    for row in reader:
        print(row['a'], row['b'])
       