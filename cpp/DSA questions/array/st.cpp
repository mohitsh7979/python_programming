#include<iostream>

using namespace std;


struct student{

    string name;
    int age;
    int height;


    student( string name , int age , int height){

        this->name = name;
        this->age = age;
        this->height = height;

    }

    void pri(){

        cout<<"Hello World";
    }

    void input(){

        cin>>name>>age>>height;
    }

    void output(){

        cout<<name<<age<<height;
    }

};

int main(){

    student s1;
    // s1.name = "mohit";
    // s1.age = 19;
    // s1.height = 56;

    // cout<<s1.name<<endl;
    // cout<<s1.age<<endl;
    // s1.pri();

    s1.input();
    s1.output();




}