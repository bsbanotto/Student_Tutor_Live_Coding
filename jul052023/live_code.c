#include <stddef.h>
#include <string.h>
#include <stdio.h>
#include <stdlib.h>


/* Function Prototypes */
/* These ones do the math */
int add(int a, int b);
int subtract(int a, int b);
int multiply(int a, int b);
int divide(int a, int b);
int modulo(int a, int b);

/* Returns a pointer to the correct function */
/* Takes a character, 'operator', and function pointer that gets two ints */
int (*do_math(char *s))(int, int);

/* TODO: Typedef a struct called operator_t */
typedef struct {

} operator_t;


/* Time to do some coding */
/* Implement our do_math function*/
int (*do_math(char *s))(int, int)
{
    /* TODO: Array of operator_t structs to get function pointers */
    operator_t operators[] = {
        {},
        {},
        {},
        {},
        {},
        {}
    };

    /* TODO: Work through operators array of structs to get function pointer*/

}


/*
gcc -Wall -pedantic -Werror -Wextra -std=gnu89 live_code.c -o calc
*/

/* Main function down here */
int main(int argc, char *argv[])
{
	int number1, number2;
	char *mathOperator;
	int (*func_ptr)(int, int);

	if (argc != 4)
	{
		printf("Error, incorrect usage!\n");
        printf("Proper usage: ./a.out int operator int\n");
		exit(98);
	}

	number1 = atoi(argv[1]);
	mathOperator = argv[2];
	number2 = atoi(argv[3]);

	func_ptr = do_math(mathOperator);

	if (func_ptr == NULL)
	{
		printf("Operator must be +, -, /, * or %%\n");
		printf("Proper usage: ./calc 5 + 2\n");
		exit(99);
	}

	if ((*argv[2] == '/' || *argv[2] == '%') && number2 == 0)
	{
		printf("Divide by Zero error\n");
		printf("When operator is / or %%, second integer cannot be zero\n");
		exit(100);
	}

	printf("%d\n", func_ptr(number1, number2));

	return (0);
}
