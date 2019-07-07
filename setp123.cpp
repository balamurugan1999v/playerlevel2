#include <iostream>
#include<string.h>
using namespace std;

int main()
{
    int co=0,ci=0,l,i,j,n,a[100],temp=0;
    cin>>n;
    for(i=2;i<=n;i++)
    {
        if((n%i)==0)
        {
            a[ci]=i;
            ci++;
        }
    }
    for (i=0;i<=ci;i++)
        {
            co=0;
            for(j=1;j<=a[i];j++)
            {
            if ((a[i]%j)==0)
            {
                co+=1;
            }
            }
    if (co==2)
        cout<<a[i]<<" ";
        }    
    return 0;
}
