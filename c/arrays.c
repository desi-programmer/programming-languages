#include<stdio.h>

int main(){
    int choice = 0;
    printf("Arrays in C \nChoose Option > ");
    scanf("%d", &choice);
    switch(choice)
        case 1:
	    printf("Option 1");
	default:
	    printf("Welcome");
    printf("%d", choice);
    return 0;
}
