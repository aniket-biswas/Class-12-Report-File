# Q14}Consider the following CSV file(emp.csv):
#             1,Peter,3500
#             2,Scott,4000
#             3,Harry,5000
#             4,Michael,2500
#             5,Sam,4200
#     Write a Python function DISEMP () to read the contents of the file 
#     emp.csv and count how many employees are earning less than 5000.
import csv
def DISPEMP():
    with open("emp.csv") as csvfile:
        myreader=csv.reader(csvfile,delimiter=",")
        print("%10s"%"EMPNO","%20s"%"EMPNAME","%10s"%"SALARY")
        print("=============================================")
        for row in myreader:
            if int(row[2])>4000:
                print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2])
DISPEMP()