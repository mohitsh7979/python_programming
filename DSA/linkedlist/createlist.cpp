#include <iostream>

using namespace std;

struct Node
{
    int data;
    struct Node *next;
};



int main(){

    // cout<<sizeof(struct Node);

    struct Node *head , *newnode , *temp;
    head = 0;
    int choice;

    while (choice)
    {
       newnode = (struct Node *)malloc(sizeof(struct Node));
    //    cout<<"Newnode:>>>"<<newnode;

       cout<<"Enter data : ";
       cin>>newnode->data;
       newnode->next=0;

       if(head == 0){

        head = temp = newnode;

       }

       else{

        temp->next = newnode;
        temp = newnode;
       }

       cout<<"Do you want to continue (0,1) : ";
       cin>>choice;



    }

    temp = head;

    while (temp!=0)
    {
        cout<<temp->data<<endl;
        temp = temp->next;
    }
    
    
}
