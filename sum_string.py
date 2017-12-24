s=input()
f=0
def sumstring(i,m,k):
  global f
  if(k>=len(s)):
    f=1
    return
  if(i==0):
    c=1
    x=i+1
    while (i<=len(s)/2 and f!=1 and(len(s[i:x])<=len(s[x:]))):
      j=i+c+1
      x=i+c
      sum=0
      while ((j<(len(s)))and(sum<=int(s[j:])))and(f!=1):
        sum=int(s[i:x])+int(s[x:j])
        if(sum==int(s[j:j+len(str(sum))])):
          sumstring(x,j,j+len(str(sum)))
        j+=1
      c+=1
  else:
    sum=int(s[i:m])+int(s[m:k])
    print(sum)
    if(sum==int(s[k:k+len(str(sum))])):
      i=m
      m=k
      sumstring(i,m,m+len(str(sum)))
sumstring(0,0,0)
if(f==1):
  print("sumstring")
else:
  print("not sumstring")
