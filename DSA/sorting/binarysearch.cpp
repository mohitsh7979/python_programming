#include <iostream>

using namespace std;

int binarysearch(int a[], int data, int n)
{

    int l = 0, r = n - 1;

    while (l <= r)
    {
        int mid = (l + r) / 2;
        if (data == a[mid])
        {

            return mid;
        }

        else if (data < a[mid])
        {

            r = mid - 1;
        }

        else
        {

            l = mid + 1;
        }
    }

    return -1;
}

int main()
{

    int n;
    cout << "Enter Your array size : ";
    cin >> n;

    int a[n];

    for (int i = 0; i < n; i++)
    {
        cout << "Enter Your Element " << i + 1 << " : ";
        cin >> a[i];
    }

    int data;

    cout << "Enter your value which you want to search : ";
    cin >> data;

    int value = binarysearch(a, data, n);

    if (value == -1)
    {

        cout << "Your data item is not in array !!!!"<<endl;
    }

    else
    {

        cout << "Your value " << a[value] << " is findout at index " << value + 1<<endl;
    }

    int m;

    while (m != 0)
    {

        cout << "Continue for 1 and 0 for exit :";
        cin >> m;

        switch (m)
        {
        case 1:

            int data;

            cout << "Enter your value which you want to search : ";
            cin >> data;

            int value = binarysearch(a, data, n);

            if (value == -1)
            {

                cout << "Your data item is not in array !!!!"<<endl;
            }

            else
            {

                cout << "Your value " << a[value] << " is findout at index " << value + 1<<endl;
            }

            break;
        }
    }
}