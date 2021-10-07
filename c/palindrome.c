/*
 * https://bit.ly/3zNlNkn
 */

#include <stdio.h>
#include <string.h>
#include <stdbool.h>

char * reverse_str(char str[]) {
    static char rev_str[30];
    int str_len;
    int rev_index;
    int i;

    str_len = strlen(str);
    rev_index = str_len;

    for (i = 0 ; i < str_len ; i++)
        rev_str[i] = str[--rev_index];
    rev_str[i] = '\0';

    return rev_str; // <--- must be captured by a pointer refer the bitly link
}


bool isPalindrome(char str[]) {
    char * rev_str;
    rev_str = reverse_str(str);
    return !(strcmp(rev_str,str));
}


int main () {

    char input_str[30];

    printf("Enter a string:\n"); gets(input_str);

    isPalindrome(input_str) ? printf("Palindrome") : printf("Not Palindrome");
    printf("\n");

    return 0;
}
