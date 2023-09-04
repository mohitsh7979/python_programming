#include <iostream>

using namespace std;

struct node
{

    int data;
    struct node *next;
};

int main()
{

    struct node *head, *newnode, *temp;
    head = 0;

    int n;

    while (n != 0)
    {

        cout << "1 insert 2 display 3 delete first 4 delete end 5 delete mid 0 exit  :";
        cin >> n;
        switch (n)
        {
        case 1:

            newnode = (struct node *)malloc(sizeof(struct node));

            cout << "Enter Your data :";
            cin >> newnode->data;

            newnode->next = 0;

            if (head == 0)
            {

                head = temp = newnode;
            }

            else
            {

                temp->next = newnode;
                temp = newnode;
            }
            break;

        case 2:

            temp = head;

            while (temp != 0)
            {
                cout << temp->data << endl;
                temp = temp->next;
            }

            break;

        case 3:

            if (head != 0)
            {
                temp = head;
                head = head->next;
                free(temp);
            }

            else
            {

                cout << "Empty !!" << endl;
            }

        case 4:

            struct node *prevnode;

            temp = head;

            while (temp->next != 0)
            {
                prevnode = temp;
                temp = temp->next;
            }

            if (temp == head)
            {

                head = 0;
            }

            else
            {

                prevnode->next = 0;
            }

            free(temp);

        case 5:

          struct node *nextnode;
          int pos , i = -1;
          temp = head;

          cout<<"Enter postion :";
          cin>>pos;

          while (i<pos-1)
          {
            temp = temp->next;
            i++;
          }

          nextnode = temp->next;
          temp->next = newnode->next;
          free(nextnode);
          
        }

    }
}