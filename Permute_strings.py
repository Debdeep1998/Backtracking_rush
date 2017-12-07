import math
a=input()
b=list(a)
def permute(d,i):
  if(len(d)==2):
    print(''.join(b))
    d[0],d[1]=d[1],d[0]
    b[i],b[i+1]=d[0],d[1]
    print(''.join(b))
  else:
    m=list(d)
    k=0
    t=0
    while(k<math.factorial(len(d))):
      j=i
      while(j<len(b)):
       if(b[j]==m[t]):
         break
       j+=1
      b[j]=b[i]
      b[i]=m[t]
      c=list(b[i+1: ])
      permute(c,i+1)
      b[i+1],b[i+2]=b[i+2],b[i+1]
      t+=1  
      k+=math.factorial(len(c))
permute(b,0)


      
