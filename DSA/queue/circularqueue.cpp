#include<iostream>

using namespace std;

# define N 5

int queue[N];

int front = -1;
int rare = -1;

void enqueue(int x){

    if(front ==-1 && rare ==-1){

        front = rare = 0;

        queue[rare] = x;
    }

    else if((rare+1)%N==front){

        cout<<"Overflow"<<endl;
    }

    else{

        rare = (rare+1)%N;
        queue[rare] = x;
    }
}


void dequeue(){

    if(front ==-1 && rare == -1){

        cout<<"underflow"<<endl;
    }

    else if(front == rare){

        front = rare -1;
    }

    else{

        cout<<queue[front]<<endl;

        front = (front+1)%N;
    }
}


void display(){

    int i = front;

    if(front == -1 && rare == -1){

        cout<<"Queue is empty"<<endl;
    }

    else{

        while (i!=rare)
        {
            cout<<queue[i]<<endl;
            i = (i+1)%N;
        }
        cout<<queue[rare]<<endl;
        
    }
}

void peek(){

    if(front == -1 && rare == -1){

        cout<<"Queue is empty"<<endl;
    }

    else{

        cout<<queue[front]<<endl;
    }
}


int main(){

    int n;

    while (n!=0)
    {

        cout<<"Choise 1 : enqueue , 2 : dequeue , 3 : display : , 4 : peek , 0 : exit :";
        cin>>n;

        switch (n)
        {
        case 1:
            
            int a;
            cin>>a;
            enqueue(a);
            break;

        case 2:
           
           dequeue();
           break;

        
        case 3:

          display();
          break;

        
        case 4:

          peek();
          break;

        
        default:
            break;
        }
    }
    
}