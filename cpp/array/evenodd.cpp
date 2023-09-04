#include<bits/stdc++.h>
using namespace std;


int max_no(int a[] , int n){

    int max=INT_MIN,d;
    for(int i=0;i<n;i++)
    {
        if(a[i]>max)
        {
            max=a[i];
            d=i;
        }

    }
 

    return d;
}

int main()
{
    int n;
    cout<<"enter the size of element=";
    cin>>n;
    int a[n];
    for(int i=0;i<n;i++)
    {
        cin>>a[i];
    }
    int d = max_no(a,n);
    cout<<"indexing :"<<d<<endl;
    for(int i=d;i<n;i++)
    {
        a[i]=a[i+1];
    }
    
    cout<<"Deleted array :"<<"\n";
    for (int i = 0; i < n-1; i++)
    {
       cout<<a[i]<<endl;
    }

    int m = max_no(a,n-1);
    cout<<"Indexing :"<<m;

    return 0;
}