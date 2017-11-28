#include<stdio.h>
int a[100];
void initialise(int n)
{
  
    int i;
    for(i=0;i<n;i++)
    {
        a[i]=0;
        
    }
}
int sum(int *a,int n)
{
    int i,sum;
    sum=0;
    
    for(i=0;i<n;i++)
    {
        sum=sum+a[i];
    }
    return sum;
    
}
    
void climb(int n,int k,int d)
{
    if(sum(a,n)==n)
    {
        int i;
        for(i=0;i<n;i++)
        {
            if(a[i]!=0)
            printf("%d,",a[i]);
        }
        printf("\n");
    }
    else if(sum(a,n)>n)
    {
        return;
    }
    else
    {
       int c=1;
        while(c<=k)
        {
            a[d]=a[d]+c;
            climb(n,k,d+1);
            a[d]=0;
            c++;
            
        }
    }
}   
void main() {
    initialise(4);
    climb(7,3,0);
    

}
