# include<iostream>

using namespace std ;

# define N 5

int queue[N];

int front = -1;

int rare = -1;


void enqueue(){

    int x;

    cin>>x;

    if (rare == N-1){

        cout<<"Overflow"<<endl;
    }

    else if(front ==-1 && rare == -1){

        front = rare = 0;

        queue[rare] = x;
    }

    else{

        rare++;

        queue[rare] = x;
    }


}



void dequeue(){


   
    if(front ==-1 && rare == -1){

         cout<<"Underflow"<<endl;
    }

    else if (front == rare){

        front = rare = -1;
    }

    else{

        cout<<queue[front]<<endl;
        front++;
    }


}


void display(){


   
    if(front ==-1 && rare == -1){

         cout<<"Underflow"<<endl;
    }

    else{

        for (int  i = front; i <= rare; i++)
        {
            cout<<queue[i]<<endl;
        }
        
    }


}


void peek(){

    if(front ==-1 && rare == -1){

         cout<<"Underflow"<<endl;
    }

    else{

        cout<<queue[front]<<endl;
    }


    
}


int main(){


    int n;

    while (n!=0)
    {

        cout<<"Enter your choice : 1 insert : 2 delete 3 : display : 4 peek and 0 exit program : ";
        cin>>n;

        switch (n)
        {
        case 1:
            
            enqueue();
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
            
            cout<<"Invalid choice"<<endl;
            break;
        }
    }
    


}