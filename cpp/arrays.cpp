// Arrays in cpp are homogeneous collection of data.
// <data-type> varname[length] = [initial_values]
// int a[5] = {12,13,13,12,12};
// int a[5];


#include<iostream>

int main(){
    // simple array of integers of length 10 
    int marks[10] = {12,34,89,76,64,45,76,98,25,76};
    // accesing using index
    // index starts at 0
    // so total length = n, but index = 0, n-1
    std::cout << marks[0] << std::endl; // prints 12
    std::cout << marks[9] << std::endl; // prints 76
    std::cout << marks[11] << std::endl; // prints random garbage value


    // Welcome to every C/C++ programmer's bestest friend: Undefined Behavior.
    // [Learn more] : https://stackoverflow.com/questions/1239938/accessing-an-array-out-of-bounds-gives-no-error-why

    return 0;
}