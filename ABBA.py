s=input()
d=input()
def canObtain(st,d):
  if(len(st)==len(d)):
    if(st==d):
      return 1
    else:
      return 0
  t=canObtain(st+"A",d)
  if(t!=1):
   t=canObtain(st[::-1]+"B",d)
  return t
if(canObtain(s,d)==1):
  print("Possible")
else:
  print("Not possible")

  
