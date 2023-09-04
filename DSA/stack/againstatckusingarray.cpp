#include <iostream>

using namespace std;

#define N 5

int stack[N];

int top = -1;

void push()
{

    int x;
    cin >> x;

    if (top == N - 1)
    {

        cout << "Overflow" << endl;
    }

    else
    {

        top++;
        stack[top] = x;
    }
}

void pop()
{



    if (top == -1)
    {

        cout << "Underflow" << endl;
    }

    else
    {

        int item = stack[top];

        top--;

        cout << item << endl;
    }
}

void display()
{

    for (int i = top; i>0; i--)
    {

        cout << stack[i] << endl;
    }
}

int main()
{

    int n;

    while (n != 0)
    {

        cout << "Enter choice :1 for push 2 for pop 3 for display";

        cin >> n;

        switch (n)
        {
        case 1:

            push();

            break;

        case 2:

            pop();

            break;

        case 3:

            display();

            break;

        default:
            break;
        }
    }
}