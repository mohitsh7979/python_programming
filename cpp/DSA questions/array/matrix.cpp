#include <stdio.h>

int main() {
    int n = 10; 


    for (int i = 0; i < n; i++) {
      
        for (int j = 0; j < n; j++) {
            int value;

            if (i % 2 == 0) {
            
                value = i + j * n + 1;
            } else {
              
                value = (i + 1) * n - j;
            }

            printf("%2d ", value);
        }

        printf("\n");
    }

    return 0;
}