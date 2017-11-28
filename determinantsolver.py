import math
n = int(input()) 
a = []
for p in range(n):
    row = input().split()
    for p in range(len(row)):
        row[p] = int(row[p])
    a.append(row)

  
print (a)
def reduce(b,f):
  m=0
  k=0
  l = []
  for z in range(len(b)-1):
    l.append([0] * (len(b)-1))
  for c in range(1,len(b)):
    for d in range(len(b)):
      if (d!=f):
        l[m][k]=b[c][d]
        k+=1
    m+=1
    k=0
  return l
def determinant(v,b):
  if(b==2):
    return (v[0][0]*v[1][1])-(v[0][1]*v[1][0])
  else:
    s=0
    for i in range(0,b):
      p1=reduce(v,i)
      t=int(math.pow(-1,i))*determinant(p1,len(p1))*v[0][i]
      s=s+t
  return s

print (determinant(a,n))
  
