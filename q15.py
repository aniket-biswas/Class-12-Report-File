# Q15}Write a Python function CSVCOPY ( ) to take sourcefile, targetfile 
#     as parameter and create a targetfile and copy the contents of the 
#     sourcefile to targetfile.
import csv 
def CSVCOPY(sourcefile,targetfile): 
  with open(sourcefile) as csvfile: 
    f2 = open(targetfile,'w') 
    mywriter=csv.writer(f2,delimiter=',') 
    myreader = csv.reader(csvfile,delimiter=',') 
    for row in myreader: 
      mywriter.writerow([row[0],row[1],row[2]]) 
  f2.close()
CSVCOPY()