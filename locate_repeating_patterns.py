n=input()
print (n)
f=0
def combo(t):
  global f
  if(t==len(n)):
    return
  k=['']
  for j in range(len(n)):
    l=n[j:j+t]
    c=0
    d=j+1
    for i in range(len(n)-(j+2)):
      if (l==n[d:d+t]):
        c=c+1 
        f+=1
      d=d+1
    if(c!=0)and(l not in (k)):
      print ("%s:%d "%(l,c+1))
      k.append(l)
  combo(t+1)
combo(2)
if(f==0):
  print(0)
