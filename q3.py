# Q3}Write a Program to enter the numbers in a list and to show the 
#    greatest element using loop in the entered list.
a=[]
n=int(input("Enter number of elements:"))
for i in range(1,n+1):
    b=int(input("Enter element:"))
    a.append(b)
a.sort()
print("Largest element is:",a[n-1])