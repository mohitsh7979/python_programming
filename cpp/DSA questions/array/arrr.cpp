#include<iostream>

using namespace std;

int main(){
    
    int n;
    cout<<"Enter array size :";
    cin>>n;

    int target ;
    cout<<"Enter Target value :";
    cin>>target;


    int arr[n];

    for(int i = 0 ; i<n ; i++){
 
        cin>>arr[i];
    }

    for(int i=0 ; i<n ; i++){

        for(int j = 0 ; j<n ; j++){

            if(arr[i]+arr[j]==target){

                cout<<arr[i]<<arr[j]<<endl;
                break;
            }
        }
    }

    return 0;

}