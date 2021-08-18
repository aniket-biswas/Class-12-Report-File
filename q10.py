# Q10}Write a function in python to count the number of lines in a text 
#     file which begins with an upper case character.
def UpperCase(): 
    f = open('a1.txt') 
    count = 0 
    for line in f: 
            if line[0].isupper(): 
                        count+=1 
    print("Lines starting from Capital letters: ",count)
UpperCase()