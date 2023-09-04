#include<bits/stdc++.h>
using namespace std;
int main()
{
    int n;
    cout<<"enter the size of array=";
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    for(int i=0;i<n;i++)
    {
        cout<<"a["<<i<<"]="<<a[i]<<"  ";
    }
    cout<<endl;
    int k=0,l=0;
    int a1[5];
    int a2[5];
    for(int i=0;i<n;i++)
    {
        if(a[i]%2==0)
        {
            a1[k]=a[i];
            k++;
        }
        else
        {
            a2[l]=a[i];
            l++;
        }
    }
    for(int n=0;n<k;n++)
    {
        cout<<a1[n]<<" ";
    }
    cout<<endl;
    for(int m=0;m<l;m++)
    {
        cout<<a2[m]<<" ";
    }
    return 0;
        
}
