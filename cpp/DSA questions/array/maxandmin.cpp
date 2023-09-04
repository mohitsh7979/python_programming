#include <bits/stdc++.h>
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
        int arr[n];

        for (int i = 0; i < n; i++)
        {

            cin >> arr[i];
        }

        int max = INT_MIN;
        int max1 = 0;
        int a = 0;

        for (int i = 0; i < n; i++)
        {

            if (arr[i] > max)
            {
                max = arr[i];
            }

            if (max > max1)
            {
                a = max1;
                max1 = max;
            }
        }

        cout << a << endl;
    }
    return 0;
}
