e=int(input())//number input
n=int(input())//expoenent input
c=0
def natural(i,k,s):
    global c
    
    while(i<=int(e**(1/k))):
       s=s+(i**k)
       if(s==e):
          c+=1
       if(s>e):
         return
       natural(i+1,k,s)
       s=s-(i**k)
       i+=1   
natural(1,n,0)
print (c)
      
        
         
        
      
      

       
      
       


