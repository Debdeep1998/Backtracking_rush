a = []
a = [[0, 0, 0, 5, 0, 0, 0, 0, 0],
     [0, 2, 0, 0, 0, 0, 0, 0, 0],
     [0, 8, 7, 0, 0, 0, 0, 0, 1],
     [0, 0, 3, 0, 1, 0, 0, 0, 0],
     [0, 0, 0, 8, 6, 3, 0, 0, 0],
     [0, 5, 0, 0, 9, 0, 6, 0, 0],
     [1, 3, 0, 0, 0, 0, 2, 5, 0],
     [0, 0, 0, 6, 0, 0, 0, 0, 0],
     [0, 0, 0, 0, 0, 0, 3, 0, 0]];

for i in range(9):
  print(a[i])
print()
def valid(i,k,l):
  
  for j in range(3):
    if(k<(3*(j+1))):
      m1=(3*(j+1))
      m=(3*(j+1))-3
      break
  for j in range(3):
    if(l<(3*(j+1))):
      n1=(3*(j+1))
      n=(3*(j+1))-3
      break
  n0=n
  for j in range(9):
    if(j!=l)and(a[k][j]==i):
      return 0
  for j in range(9):
    if(j!=k)and(a[j][l]==i):
      return 0
  while(m<m1):
    while(n<n1):
      if(m!=k)and(n!=l)and(a[m][n]==i):
        return 0
      n+=1
    m+=1
    n=n0
f=0  
def min_sudo(k,l):
  global f
  if(k==9):
    for j in range(9):
      print(a[j])
    f+=1
    return
  else:
    if(a[k][l]==0):
      d=1
      while(d<=9):
        if(valid(d,k,l)==0):
          d+=1
          continue
        a[k][l]=d
        if(l==8):
          min_sudo(k+1,0)
        else:
          min_sudo(k,l+1)
        if(f==1):
          return
        d+=1
      a[k][l]=0  
    else:
      if(l==8):
        min_sudo(k+1,0)
      else:
        min_sudo(k,l+1)
      if(f==1):
        return
min_sudo(0,0)  
if(f==0):
  print("No solution exists")

      
  
