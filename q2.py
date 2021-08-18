# Q2}Write a Program to display frequencies of all the elements of 
#    a list.
arr=[]
nofele=int(input("Enter no of elements:"))
for i in range(0,nofele):
  b=int(input("Enter Elements:"))
  arr.append(b)
print("Elements:",arr)
     
#Array fr will store frequencies of element    
fr = [None] * len(arr);    
visited = -1;    
      
for i in range(0, len(arr)):    
    count = 1;    
    for j in range(i+1, len(arr)):    
        if(arr[i] == arr[j]):    
            count = count + 1;    
            #To avoid counting same element again    
            fr[j] = visited;    
                
    if(fr[i] != visited):    
        fr[i] = count;    
      
#Displays the frequency of each element present in array    
print("---------------------");    
print(" Element | Frequency");    
print("---------------------");    
for i in range(0, len(fr)):    
    if(fr[i] != visited):    
        print("    " + str(arr[i]) + "    |    " + str(fr[i]));    
print("---------------------");