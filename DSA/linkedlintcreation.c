#include<stdio.h>
// #include<stdlib.h>

// struct Node
// {
//     /* data */
//     int data;
//     struct Node *next;
// };


// void linkedListTraversal(struct Node *ptr)
// {   
//     while (ptr !=NULL){

//      printf("Element: %d\n",ptr->data);
//      ptr=ptr->next;
//     }
// }

// int main(){

//     struct Node *head;
//     struct Node *second;
//     struct Node *third;


//     //Allocate memory for nodes in the linked list in heap
//     head=(struct Node *)malloc(sizeof(struct Node));
//     second=(struct Node *)malloc(sizeof(struct Node));
//     third=(struct Node *)malloc(sizeof(struct Node));

//     //link first and seconds nodes
//     head->data=7;
//     head->next=second;

//     //link second and third nodes
//     second->data=11;
//     second->next=third;

//     //Terminate the list at the third node
//     third->data=66;
//     third->next=NULL;


//     linkedListTraversal(head);

//     return 0;

// }

#include<stdio.h>
#include<stdlib.h>

struct Node{

    int data;
    struct Node *next;
};


void linkedlistTraversal(struct Node *ptr){
    
    while (ptr!=NULL)
    {
        /* code */
    printf("%d\n",ptr->data);
    ptr=ptr->next;
    }


    printf("Hello world ");
}




int main(){

    struct Node *head;
    struct Node *second;
    struct Node *third;


    head=(struct Node *) malloc(sizeof(struct Node));
    second=(struct Node *)malloc(sizeof(struct Node));
    third=(struct Node *)malloc(sizeof(struct Node));

    head->data=7;
    head->next=second;

    second->data=8;
    second->next=third;

    third->data=9;
    third->next=NULL;


    linkedlistTraversal(head);



    

}




























