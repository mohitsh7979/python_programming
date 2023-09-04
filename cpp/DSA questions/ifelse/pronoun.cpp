#include <iostream>
using namespace std;

int main()
{
    // your code goes here

    int t;
    cin >> t;

    for (int i = 0; i < t; i++)
    {

        int n;
        cin >> n;

        int arr1[n];
        int arr2[n];
        int counter = 0;

        for (int i = 0; i < n; i++)
        {

            cin >> arr1[i];
            cin >> arr2[i];
        }



        for (int i = 0; i < n; i++)
        {

            cout << arr1[i];
        }



        for (int j = 0; j < n; j++)
        {

          
            cout << arr2[j];
        }

        for (int i = 0; i < n; i++)
        {

            if (arr1[i] > arr2[i] && (arr1[i] / 2) <= arr2[i])
            {

                counter++;
                cout << "entery third";
            }

           

            else if (arr2[i] > arr1[i] && (arr2[i] / 2) <= arr1[i])
            {

                cout<<arr2[i]/2;

                counter++;
                cout << "enter second";
            }

            else if (arr1[i] == arr2[i])
            {

                counter++;
                cout << "enter last";
            }
        }

        cout << counter << endl;
    }

    return 0;
}
