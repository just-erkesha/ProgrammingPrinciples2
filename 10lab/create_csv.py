import csv

with open('data.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['Arman', '87777777777'])
    writer.writerow(['Aiman', '87717777171'])
    writer.writerow(['Bagdat', '87007007070'])