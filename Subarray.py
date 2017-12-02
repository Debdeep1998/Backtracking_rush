n=int(input())//Enter size of array
l=[]
for i in range(n)://Enter array items
    a=int(input())
    l.append(a)
k=[0]*n
def subset(i,t):
    if(i==n):
        return
    while(t<n):
       k[i]=l[t]
       
       print(k[:i+1])  
       subset(i+1,t+1)
       t+=1
       k[i]=0
        
subset(0,0)



    
  
