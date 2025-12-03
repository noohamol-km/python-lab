import csv

csv_col = ['Roll no', 'Name', 'Department']
dict_data = [
    {'Roll no': 1, 'Name': 'Alex', 'Department': 'Mca'},
    {'Roll no': 2, 'Name': 'Aleena', 'Department': 'Mca'},
    {'Roll no': 3, 'Name': 'Minu', 'Department': 'Mca'},
    {'Roll no': 4, 'Name': 'Ebin', 'Department': 'Mca'},
    {'Roll no': 5, 'Name': 'Jimmy', 'Department': 'Mca'}
]

csv_file = "student.csv"

try:
    with open(csv_file, 'w', newline='') as file1:
        writer = csv.DictWriter(file1, fieldnames=csv_col)
        writer.writeheader()
        for data1 in dict_data:
            writer.writerow(data1)

except IOError:
    print("I/O error")

# Reading the CSV file back as a dictionary
print("CSV file as a dictionary:\n")
with open(csv_file) as f:
    data1 = csv.DictReader(f)
    for row in data1:
        print(row)
