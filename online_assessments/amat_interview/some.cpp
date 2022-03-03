#include <stdio.h>

#define FLAG 0

void pascal(int level) {
// initialize two arrays of size (level * 2) + 1
// initialize first of these arrays with values 1 1
// in a for loop from 1 to level
// use the values in the first array to come up with the second
// switch the second to first
//
// 1 1
//  level - 1
//  j: 1 -> level, i: 0 -> level - 1
//
//  second_arr[j] = first_arr[i - 1] + first_arr[i]
//  
// 1 j
}

int main(void) {
    pascal(4);
}
