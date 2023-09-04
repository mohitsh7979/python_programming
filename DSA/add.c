// Online C compiler to run C program online
#include <stdio.h>

int main()
{
    // Write C code here
    // printf("Hello world");

    int arr[100];
    int i;
    int a;
    int j;
    int index;
    int newvalue;

    printf("How much item you want store in your list :");
    scanf("%d", &a);

    for (j = 0; j < a; j++)
    {
        scanf("%d", &arr[j]);
    }

    // printf("index :");
    // scanf("%d", &index);
    // printf("value :");
    // scanf("%d", &newvalue);

    // for (i = 4; i >= index; i--)
    // {

    //     arr[i + 1] = arr[i];
    //     arr[i] = newvalue;
        
    // }
    // printf("\n");

    for (j = 0; j <=a; j++)
    {
        printf("%d\t", arr[j]);
    }
    
    index=sizeof(arr)/sizeof(arr[0]);
    printf("%d",index);

    return 0;

    // int arr[5]={10,20,30,40,50};

    // int a=sizeof(arr)/sizeof(arr[0]);
    // printf("%d",a);

    
}