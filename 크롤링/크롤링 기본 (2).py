import csv

f = open('output.csv', 'w', encoding='utf-8', newline='')
wr = csv.writer(f)
wr.writerow([1, "안유진", False])
wr.writerow([2, "장원영", True])
f.close()
