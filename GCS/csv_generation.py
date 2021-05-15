import csv

#write to container csv file
with open('Flight_3226_C.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['testing', 'hello', 'this thing working?'])

#TODO, why aren't the other two .csv files being created????
#write to payload 1 csv file
with open('Flight_3226_SP1.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['testing', 'hello', 'this thing working?'])

#write to payload 2 csv file
with open('Flight_3226_SP2.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow(['testing', 'hello', 'this thing working?'])
