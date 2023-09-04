#include <iostream>

using namespace std;

int main()
{

    int n;
    cout<<"Enter Your array size :";
    cin >> n;

    int arr[n];

    for (int i = 0; i < n; i++)
    {

        cin >> arr[i];
    }

    int s;
    cout<<"Enter Your search element :";
    cin>>s;

   for (int i = 0; i < n; i++)
   {
     if (arr[i]==s)
     {
        cout<<"found at index"<<i+1<<" "<<arr[i];
     }
     
   }
   
    

}