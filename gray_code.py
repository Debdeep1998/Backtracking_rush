n=int(input())
a=list()
for i in range(n):
  a.append('0')
print (a)
def gray(i):
  if(i==n-1):
    print("".join(a))
    a[i]='1' if(a[i]=='0')else('0')
    print("".join(a))
    return
  c=1
  while (c<=2):
    gray(i+1)
    if(c!=2):
      a[i]='1' if(a[i]=='0')else('0')
    c+=1
gray(0)
  
    
  
