#include <bits/stdc++.h>


using namespace std;

void selectionsort(int arr[] , int n)
{
    for (int  i = 0; i < n-1; i++)
    {
        int min = i;

        for(int j = i+1 ; j<n ; j++){
             
             if(arr[j]<arr[min]){

                min = j;
             }
        }

        if(min!=i){

            swap(arr[i],arr[min]);
        }
    }

    for (int i = 0; i < n; i++)
    {
        cout<<arr[i]<<" ";
    }
    
    
    
}

int main()
{

    int n;

    cout << "Enter Your array size :";
    cin >> n;

    int arr[n];

    for (int i = 0; i < n; i++)
    {

        cout << "Enter Your array element :";
        cin >> arr[i];
    }

    selectionsort(arr, n);
}