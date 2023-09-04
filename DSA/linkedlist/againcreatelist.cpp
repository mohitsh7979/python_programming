#include <iostream>

using namespace std;


struct Node
{

    int data;

    struct Node *ptr;
};


int main()
{

    int n;

    struct Node *newnode, *head, *temp;
    head = 0;

 

    while (n != 0)
    {
        cout << "Enter Your choise 1 : create new 2: insert biggning 3: insert ending 4: insert after value : 0 Exit :";
        cin >> n;


        switch (n)
        {
        case 1:
                                 
            newnode = (struct Node *)malloc(sizeof(struct Node));
            cout << "Enter Your Data : ";
            cin >> newnode->data;
            newnode->ptr = 0;

            if (head == 0)
            {

                head = temp = newnode;
            }

            else
            {

                temp->ptr = newnode;
                temp = newnode;
            }

            temp = head;

            while (temp != 0)
            {
                cout << temp->data << endl;
                temp = temp->ptr;
            }
            break;

        case 2:

            temp = head;

            while (temp != 0)
            {
                cout << temp->data << endl;
                temp = temp->ptr;
            }

        default:
            break;
        }
    }
}