#include<stdio.h>
#include<string.h>

struct person{

    char name[20];
    int age;
    int height;




};

int main(){

    // struct person p1;

    
    // strcpy(p1.name , "mohit");
    // p1.age=20;
    // p1.height=5;

    // printf("%d",p1.age);

    // scanf("%s %d %d",&(p1.name),&(p1.age),&(p1.height));

    // printf("%s %d %d",p1.name,p1.age,p1.height);



    // structure with array

    struct person p1[3];

    for(int i = 0 ; i<3 ; i++){

        scanf("%s %d %d",&(p1[i].name),&(p1[i].age),&(p1[i].height));
    }

    for(int i = 0 ; i<3 ; i++){

        printf("%s %d %d",(p1[i].name),(p1[i].age),(p1[i].height));
    }

}