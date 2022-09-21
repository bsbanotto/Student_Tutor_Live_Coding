#include "header.h"
#include <stdio.h>

/**
 * do_while_loop - Executes a do while loop
 * @endNum: End number for loop
 *
 * Return: 0 on success
 */

int do_while_loop(int endNum)
{
	int i = 0;

	do {
		printf("%d, ", i);
		i++;
	} while (i <= endNum);
	printf("endNum = %d\n", endNum);
	printf("i = %d\n", i);
	printf("\n");
	return (0);
}
