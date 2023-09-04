#include <bits/stdc++.h>

using namespace std;

void insertationsort(int arr[], int n)
{

    for (int i = 1; i < n; i++)
    {

        int temp = arr[i];

        int j = i - 1;

        while (j >= 0 && arr[j] > temp)
        {
            arr[j + 1] = arr[j];
            j--;
        }

        arr[j + 1] = temp;
    }

    for (int i = 0; i < n; i++)
    {
        cout << arr[i] << " ";
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

    insertationsort(arr, n);
}