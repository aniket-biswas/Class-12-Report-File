# Q5}Write a program using function that prints out the first n rows 
#    of Pascal's triangle.

n = int(input("Enter No of rows required:"))

for i in range(n):
    print(' '*(n-i), end='')
    print(' '.join(map(str, str(11**i))))