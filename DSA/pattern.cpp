#include <iostream>

using namespace std;

int main()
{
 
    
    int n = 10;
    
    for(int i=0 ; i<n ; i++){
        
        for(int j=0 ; j<(n-i)/2 ; j++){
            
            cout<<" ";
        }
        
        for(int k=0 ; k<=i ; k++){
            
            cout<<"*";
        }
        
        cout<<"\n";
        
        
        
    }

    return 0;
}