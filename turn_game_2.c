#include<stdio.h>
#define N 5
int a[N]={2,1,0,0,0};
 
int movesleft()
{
  int i;
  for(i=0;i<(N/2)-1;i++)
  {
    if(a[i]!=0)
    return 1;
  }
  return 0;
}
int determine(int turn,int *b)
{
  int i;
  if(movesleft()==0)
  {
    if(turn=2)
    {
      return 10;
    }
    else
    return -10;
  }
  else
  {
    if(turn==1)
    {
      int c;
       for(i=0;i<(N/2)-1;i++)
       {
          if(a[i]!=0)
          {
          a[i]=a[i]-1;
          }
          c=determine(2,b);
           a[i]=a[i]+1;
          if(c==10)
          { 
            
            break;
            
          }
         
       }
       return c;
    }
    else
    {
      int c;
       for(i=0;i<(N/2)-1;i++)
       {
          if(a[i]!=0)
          {
          a[i]=a[i]-1;
          }
          c=determine(1,b);
           a[i]=a[i]+1;
          if(c==-10)
          { 
            break;
            
          }
         
       }
       return c;
      
    }
  }
    
  }
  
void player()
{
  int i,c;
  for(i=0;i<(N/2)-1;i++)
  {
    if(a[i]!=0)
    {
      a[i]=a[i]-1;
    
    c=determine(2,a);
    a[i]=a[i]+1;
    if(c==10)
    { 
      break;
    }
  }
  }
  if(c==10)
  {
    printf("A");
  }
  else
    printf("B");
}
void main()
{
  
  player();
  
}
