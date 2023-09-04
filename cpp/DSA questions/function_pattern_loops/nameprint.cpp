#include<iostream>
// (j == a && i <= a / 2)
using namespace std;

int main()
{
    int a = 10;

    for (int i = 0; i <= a; i++)
    {

        for (int j = 0; j <= a; j++)
        {

            if (i == 0 || j == 0 || i == a / 2 || (j==a && i<=a/2))
            {

                cout << "*"; // R
            }

            else
            {

                cout << " ";
            }
        }

        cout << "\n";
    }

    cout <<"\n";
    cout <<"\n";

    for (int i = 0; i <= a + 2; i++)
    {

        for (int j = 0; j <= a; j++)
        {

            if (i == 0 || j == 0 || i == a / 2 || (j == a && i <= a / 2) || i - j == a / 2)
            {

                cout << "*"; // R
            }

            else
            {

                cout << " ";
            }
        }

        cout << "\n";
    }

    
    cout <<"\n";
    cout <<"\n";


    for (int i = 0; i <= a; i++)
    {

        for (int j = 0; j <= a; j++)
        {

            if (i + j == a / 2 || (abs(i - j) == a / 2 && i <= a / 2) || (i == a / 4 && (j >= a*30 / 100) && j <= (a * 75 / 100)))
            {

                cout << "*"; // R
            }

            else
            {

                cout << " ";
            }
        }

        cout << "\n";
    }

    
    cout <<"\n";
    cout <<"\n";


    for (int i = 0; i <= a; i++)
    {

        for (int j = 0; j <= a; j++)
        {

            if (i == 0 || j == 0 || (i == a && j <= a / 2) || (j == a / 2 && i >= a / 2) || (j == a && i >= a / 2) || (i == a / 2 && j >= a / 2))
            {

                cout << "*";
            }

            else
            {

                cout << " ";
            }
        }

        cout << "\n";
    }

    
    cout <<"\n";
    cout <<"\n";


    for (int i = 0; i <= a; i++)
    {

        for (int j = 0; j <= a; j++)
        {

            if (i + j == a || (i - j == 0 && j <= a / 2))
            {

                cout << "*"; // R
            }

            else
            {

                cout << " ";
            }
        }

        cout << "\n";
    }

    
    cout <<"\n";
    cout <<"\n";


    for (int i = 0; i <= a; i++)
    {

        for (int j = 0; j <= a; j++)
        {

            if (i + j == a / 2 || (abs(i - j) == a / 2 && i <= a / 2) || (i == a / 4 && j >= (a*30 /100) && j <= (a * 75 / 100)))
            {

                cout << "*"; // R
            }

            else
            {

                cout << " ";
            }
        }

        cout << "\n";
    }

    return 0;
}
