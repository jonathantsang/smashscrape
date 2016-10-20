import csv

arrayofdata=[[1,2,4,5,'something','spam',2.334],
             [3,1,6,3,'anything','spam',0]]
             
with open('mydata.csv', 'w') as mycsvfile:
    thedatawriter = csv.writer(mycsvfile, dialect='excel')
    for row in arrayofdata:
        thedatawriter.writerow(row)