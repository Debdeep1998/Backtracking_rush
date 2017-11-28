import math
l=[]
q=int(input())
c=0
while(c!=q):
   
    l.append(int(input()))
    c+=1

def count(c,n):
    if (c>n):
        return 0
    else:
        return int(math.pow(3,c)+(math.pow(3,c)/3)+count(c+1,n))
c=0
while(c!=len(l)):
    print ((count(1,l[c])+1)%(int(math.pow(10,9)+7)))
    c+=1
    

