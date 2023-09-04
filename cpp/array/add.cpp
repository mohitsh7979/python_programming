#include<iostream>

using namespace std;

int main(){


    int n;
    cout<<"Enter Your array size :";
    cin>>n;

    int arr[n],sum = 0;


   for(int i=0 ; i<n ; i++){

       cin>>arr[i];
   }


    int max=INT32_MIN;
    for(int i=0 ; i<n ; i++){
    
        if(arr[i]>max)
        {
            max=arr[i];
        }
    
    }
    cout<<max;

    
}