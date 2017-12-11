n=int(input())
l=[]
w=[]
for i in range(n):
  l.append(int(input()))
for i in range(n):
  w.append(float(input()))
print(l)
print(w)
c=float(input())
b=0
def subset(t,k,m):
    global b
    if(m>c):
      return 1
    elif(t==n):
      return k
    while(t<n):
       k=k+l[t]
       m=m+w[t]
       f=subset(t+1,k,m)
       if(f==1):
         b1=k-l[t]
         b=max(b,b1)
       b=max(b,f)
       k=k-l[t]
       m=m-w[t]
       t+=1
    return b
def knapsack(n):
  p=0
  for i in range(n):
      p=max(p,subset(i+1,l[i],w[i]))
      b=0
  print (p) 
knapsack(n)
