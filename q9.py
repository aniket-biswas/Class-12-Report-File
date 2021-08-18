# Q9}Write a program to read a text file line by line and display each word 
#    separated by "#".
f1 = open("a1.txt",'r')
for  line in f1:
     word= line .split()
     for w in word:
          print(w + '#',end ='')
     print()
f1.close()