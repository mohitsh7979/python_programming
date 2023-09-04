#include <iostream>

using namespace std;

struct node
{

    int data;
    struct node *next;
};

int main()
{

    struct node *newnode, *head, *temp;
    int count = 0;
    head = 0;
    int n;

    while (n != 0)
    {
        cout << "Enter Your choice 1 for insert and 2 for display and 3 for insert beggning and 4 for insert ending and 5 for insert value in mid and 0 exit :";
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
                count++;
            }
            cout << "Count :" << count << endl;

            break;

        case 3:

            newnode = (struct node *)malloc(sizeof(struct node));
            cout << "Enter Your data which you want store in begnning :";
            cin >> newnode->data;
            newnode->next = head;
            head = newnode;

            break;

        case 4:

            newnode = (struct node *)malloc(sizeof(struct node));
            cout << "Enter Your data which you want store at end :";
            cin >> newnode->data;
            newnode->next = 0;

            temp = head;

            if (temp->next != 0)
            {

                temp = temp->next;
            }

            temp->next = newnode;

            break;

        case 5:

            int pos, i = 1;
            cout << "Enter your postion where you want to insert new value :";
            cin >> pos;
            if (pos > count)
            {

                cout << "Invalid postion";
            }

            else
            {

                temp = head;
                while (i < pos)
                {
                    temp = temp->next;
                    i++;
                }
            }
            newnode = (struct node *)malloc(sizeof(struct node));
            cout << "Enter Your data which you want store at position :";
            cin >> newnode->data;
            newnode->next = temp->next;
            temp->next = newnode;

            break;

    

        }
    }
}