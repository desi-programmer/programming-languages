#include<stdio.h>

int main(){
    int choice = 1;
    char choose = 'a';

    // switch 
    // switch(expression){
    //     case constant-expression:
    //         expressions ;
    // }

    // switch(choice + 1){ // supported
    switch(choice){
        case 1:
            printf("Choice is 1");
            break;
        case 2:
            printf("Choice is 2");
            break;
        default:
            printf("Default !!!");
    }

    printf("\n");

    switch(choose){
        case 'a':
            printf("A");
            break;
        case 'b':
            printf("B");
            break;
        default:
            printf("Oops Default !");
    }

    return 0;
}