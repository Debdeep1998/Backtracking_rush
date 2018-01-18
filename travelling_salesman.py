n=int(input("Enter size of matrix:"))
l=[[0 for j in range(n)] for i in range(n)]
for i in range(n):
  a=input().split()
  for j in range(len(a)):
    l[i][j]=int(a[j])
a=[]
for i in range(1,n+1):
  a.append(i)
for i in range(n):
  print(l[i])
a.append(1)
m=9999
def tsp(b,t):
  global l
  global m
  global a
  if(t==n-1):
    s=0
    for i in range(n):
      s+=l[b[i]-1][b[i+1]-1]
    m=min(m,s)
  else:
    c=0
    i=t
    while(i<n):
      b[t],b[t+c]=b[t+c],b[t]
      tsp(b,t+1)
      b[t],b[t+c]=b[t+c],b[t]
      i+=1
      c+=1
tsp(a,1)
print(m)
      
     
      
      
      
    
        
      
      
  
  
      
      
      
    
        
      
      
  
  
