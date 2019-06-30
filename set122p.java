import java.util.*;
import java.lang.*;
class Main {
  public static void main(String[] args) {
    Scanner s=new Scanner(System.in);
String a;
int i,j,k,b,a1=0;
a=s.next();
char ch[]=a.toCharArray();
k=a.length();
for (i=0;i<k;i++)
{
   if (ch[i]=='-')
   {
       j=i+1;
       while(ch[j]!='-')
       {
         b=Character.getNumericValue(ch[j]);
           //System.out.println(a1+" "+b);
           a1=a1*10+b;
           j=j+1;
       }
       break;
   }
}
switch(a1)
{
  case 1:System.out.println("January");
  break;
  case 2:System.out.println("February");
  break;
  case 3:System.out.println("March");
  break;
  case 4:System.out.println("April");
  break;
  case 5:System.out.println("May");
  break;
  case 6:System.out.println("June");
  break;
  case 7:System.out.println("July");
  break;
  case 8:System.out.println("August");
  break;
  case 9:System.out.println("Sepetember");
  break;
  case 10:System.out.println("October");
  break;
  case 11:System.out.println("November");
  break;
  case 12:System.out.println("December");
  break;
}
  }
}
