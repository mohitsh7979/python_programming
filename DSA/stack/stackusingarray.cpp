#include <bits/stdc++.h>
using namespace std;

# define N 5 

int stak[N];
int top = -1;

void push()
{

    int x;
    cout << "Enter your data : ";
    cin >> x;

    if (top == N-1)
    {

        cout << "Overflow" << endl;
    }

    else
    {

        top++;
        stak[top] = x;
    }
}

void pop()
{

    int item;

    if (top == -1)
    {

        cout << "Underflow" << endl;
    }

    else
    {

        item = stak[top];

        top--;

        cout << item << endl;
    }
}

void peek()
{

    if (top == -1)
    {

        cout << "Stack is empty" << endl;
    }

    else
    {

        cout << stak[top] <<endl;
    }
}

void display()
{

    for (int i = top; i >= 0; i--)
    {

        cout << stak[i] <<endl;
    }
}

int main()
{

    int ch;

    do
    {
        cout << "Enter choice : 1:push , 2:pop , 3:peek , 4:display : ";
        cin >> ch;
        /* code */

        switch (ch)
        {

        case 1:

            push();
            break;

        case 2:

            pop();
            break;

        case 3:

            peek();
            break;

        case 4:

            display();
            break;

        default:

            cout << "Invalid choicse"<<endl;
            break;
        }
    } while (ch != 0);


    return 0;
 
    
}


