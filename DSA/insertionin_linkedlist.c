#include <stdio.h>
#include <stdlib.h>

struct Node
{

    int data;
    struct Node *next;
};

void linkedtraverse(struct Node *ptr)
{

    while (ptr != NULL)
    {
        printf("%d\n", ptr->data);
        ptr = ptr->next;
    }
}

struct Node * insertinstarting(struct Node *head, int data)
{

    struct Node *ptr = (struct Node *)malloc(sizeof(struct Node));
    
    ptr->next=head;
    ptr->data=data;

    return ptr;
}

struct Node * insertinbetween(struct Node *second ,int data){

    struct Node *new=(struct Node *)malloc(sizeof(struct Node));
    
    new->next=second;
    new->data=data;

    return new;
}

int main()
{

    struct Node *head;
    struct Node *second;
    struct Node *third;

    head = (struct Node *)malloc(sizeof(struct Node));
    second = (struct Node *)malloc(sizeof(struct Node));
    third = (struct Node *)malloc(sizeof(struct Node));

    head->data = 10;
    head->next = head;

    second->data = 20;
    second->next = third;

    third->data = 30;
    third->next = NULL;

    // linkedtraverse(head);
    head=insertinstarting(head,100);
    linkedtraverse(head);

    head=insertinbetween(head,500);
    insertinbetween(second,500);

}