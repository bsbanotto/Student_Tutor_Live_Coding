#include <stdio.h>

//recursive function to print alphabet
void alphabet_recursion(char end_letter)
{
    if (end_letter != ('a' - 1))
    {
        alphabet_recursion(end_letter - 1);
        printf("%c ", end_letter);
    }
}

//iterative function to print alphabet
void alphabet_iterative(char end_letter)
{
    char letter;

    for(letter = 'a'; letter <= end_letter; letter++)
    {
        printf("%c ", letter);
    }
}
//main function - entry point to print alphabet ending at given character
void main(void)
{
    printf("Alphabet iterative:\n");
    alphabet_iterative('f');
    printf("\n");

    printf("Alphabet recursion:\n");
    alphabet_recursion('f');
    printf("\n");
}

// https://tinyurl.com/59m3pxs8