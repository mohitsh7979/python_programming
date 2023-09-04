#include <iostream>

using namespace std;

int partation(int a[], int lb, int ub)
{

    int pivot = a[lb];
    int start = lb;
    int end = ub;

    while (start < end)
    {
        while (a[start] <= pivot)
        {
            start++;
        }

        while (a[end] > pivot)
        {
            end--;
        }

        if (start < end)
        {

            swap(a[start], a[end]);
        }
    }

    swap(a[lb], a[end]);

    return end;
}

void quicksort(int a[], int lb, int ub)
{

    if (lb < ub)
    {
        int loc = partation(a, lb, ub);
        quicksort(a, lb, loc - 1);
        quicksort(a, loc + 1, ub);
    }
}

int main()
{

    int n;
    cout << "Enter your array size :";
    cin >> n;

    int a[n];

    for (int i = 0; i < n; i++)
    {
        cout << "Enter your array element" << i + 1 << ":";
        cin >> a[i];
    }

    quicksort(a, 0, n - 1);

    for (int i = 0; i < n; i++)
    {
        cout << a[i] << " ";
    }
}