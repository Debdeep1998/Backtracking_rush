m=[[1,1,1,1,1,1,1,1,1,1],
   [1,1,0,1,1,0,1,1,0,1],
   [1,1,1,0,1,1,1,1,1,1]]
a=[]
x=int(input("Enter destination x:"))
y=int(input("Enter destination y:"))
for i in range(len(m)):
  a.append([])
  for j in range(len(m[0])):
    a[i].append(1 if(m[i][j]!=1)else(0))
def check(m,n):
  if(a[m][n]==1):
    return 0
  return 1
def path(m,n):
  l=0
  if(m==x)and(n==y):
    return 1
  a[m][n]=1
  if(n+1<len(a[0])):
    if(check(m,n+1)==1):
      l=max(l,path(m,n+1))
  if(m+1<len(a)):
    if(check(m+1,n)==1):
      l=max(l,path(m+1,n))
  if(n-1>=0):
    if(check(m,n-1)==1):
      l=max(l,path(m,n-1))
  if(m-1>=0):
    if(check(m-1,n)==1):
      l=max(l,path(m-1,n))
  a[m][n]=0
  if(l>0):
   return l+1
  else:
    return 0
print(path(int(input("Enter source x:")),int(input("Enter source y:")))-1)

    
    
  
  
