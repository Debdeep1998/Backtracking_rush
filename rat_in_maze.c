n = int(input()) 
a = [[int(j) for j in input().split()] for i in range(n)]
b=[[0] * n for i in range(n)]
for i in range(n):
  print(a[i])
print()
f=0
def path(i,j):
  global f
  if(a[i][j]==0):
    return 
  if(i==n-1)and(j==n-1):
    if(a[i][j]==1):
      b[i][j]=1
      for i in range(n):
        print(b[i])
    f=1
    return
  elif(i<=n-1):
    while(j<n and f!=1):
      b[i][j]=1
      if(i<n-1):
        path(i+1,j)
        
      if(f!=1):
        j+=1
        path(i,j)
        j-=1
path(0,0)    
  
