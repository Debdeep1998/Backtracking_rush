#Turn-wise 2 player pickup game in which player 1 always gets to start and can pickup either 1 or 4 balls from a jar containing "n" number of balls.Given that player 1 and player 2 take turns and both play optimally. 
Output "Yes" or "No" for wins and losses of Player 1.
#include<stdio.h>
	
	int p;
	int best(int n,int turn)
	{	
	  if(n==0 && turn==1)
	  {
	  	return -10;
	  }
	  if(n==0 && turn==0)
	  {
	  	return 10;
	  }
	  if(turn==1)
	  {
	     p=best(n-1,0);
	    if(n-4>=0 && p!=10)
	    {
	    	p=best(n-4,0);
	    }
	    return p;
	  }
	  if(turn==0)
	  {
	    p=best(n-1,1);
	    if(n-4>=0 && p!=-10)
	    {
	      p=best(n-4,1);
	    }
	    return p;
	  }
	}
	void sumit(int k)
	{
	   
	      p=best(k-1,1);
	    if(k-4>=0 && p!=-10)
	    {
	      p=best(k-4,1);
	    }
	    if(p==-10)
	    {
	      printf("Yes\n");
	    }
	    else
	    {
	      printf("No\n");
	    }
	}
	void main()
	{
	  int t,c,i;
	  int n[100];
	  i=0;
	  printf("Enter number of test cases");
	  scanf("%d",&t);
	  
	  c=t;
	  
	  while (t-- >0)
	  {
	  printf ("Enter a number");
	  scanf("%d",&n[i]);
	  i++;
	  }
	  t=0;
	  while(t<=c)
	  {
	    sumit(n[t++]);
	    
	  }
	  
	  
	}


