#include <iostream>

using namespace std;

int main()
{

    int n;
    cout<<"Enter Your array size : ";
    cin >> n;

    int arr[n];

    for (int i = 0; i < n; i++)
    {
        cout<<"Enter your array element "<<i+1<<":";
        cin >> arr[i];
    }

    for (int i = 0; i < n - 1; i++)
    {

        int temp = 0;
        int flag  = 0;

        // first method

        // for (int j = 0; j < n - 1; j++)
        // {

        //     if (arr[j] > arr[j + 1])
        //     {

        //         temp = arr[j];
        //         arr[j] = arr[j + 1];
        //         arr[j + 1] = temp;
        //     }
        // }

        // second method


        for (int j = 0; j < n - 1 - i; j++)
        {

            if (arr[j] > arr[j + 1])
            {

                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;

                flag = 1;
            }
        }

        if(flag==0){

            break;
        }


    }

    for (int i = 0; i < n; i++)
    {

        cout << arr[i] << " ";
    }
}