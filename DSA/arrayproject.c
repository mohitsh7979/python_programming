#include <stdio.h>

int main()
{

    int arr[100];
    int i;
    int a;

    printf("Press 1 for createing a list\n");
    printf("Press 2 for displayin list\n");
    printf("Press 3 for add new item in a list\n");
    printf("Press 4 for deleting item in  a list\n");

    for (i = 0; i <= 4; i++)
    {

        int input;
        printf("Select your No : ");
        scanf("%d", &input);

        if (input == 1)
        {

            int j;
            printf("How much item you want store in your list :");
            scanf("%d", &a);

            for (j = 0; j < a; j++)
            {
                scanf("%d", &arr[j]);
            }
        }

        else if (input == 2)
        {

            int j;
            printf("your list item is :");

        
            for (j = 0; j <=a; j++)
            {

                printf("%d\t", arr[j]);
            }
           
        }

        else if (input == 3)
        {
            printf("Welcome in add itme list list \n");
            int index;
            int newvalue;
            int j;
            printf("Selcte your index where you want to store your new value :");
            scanf("%d",&index);
            printf("Enter Your new Value :");
            scanf("%d",&newvalue);
            for (j =a-1; j >= index; j--)
            {

                arr[j + 1] = arr[j];
                arr[j] = newvalue;
            }
        }

        else if (input == 4)
        {
            printf("Welcome in deleting  list");
        }

        printf("\n");
    }
}