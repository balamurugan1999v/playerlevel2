import java.util.*;
public class setp124 {
  public static void main(String[] args) {
    int a,b,i,j,n,ans=1,y=0,co;
    Scanner s=new Scanner(System.in);
    n=s.nextInt();
    int ar[]=new int[n];
    for (i=0;i<n;i++)
    {
      ar[i]=s.nextInt();
      ans=ans*ar[i];
      if (y<ar[i])
      {
        y=ar[i];
      }
    }
    for (i=y;i<=ans;i++)
    {
      co=0;
      for (j=0;j<n;j++)
      {
        if((i%ar[j])==0)
        co+=1;
      }
      if (co==n)
      break;
    }
    System.out.println(i);
  }
}
