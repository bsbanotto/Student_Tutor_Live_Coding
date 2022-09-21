#include "header.h"
#include <stdio.h>

/**
 * main - This will call all of our functions
 *
 * Return: void
 */

int main(void)
{
	printf("Output of for_loop(1, 10)\n");
	for_loop(1, 10);
	printf("\n\n");
	printf("Output of while_loop(14)\n");
	while_loop(14);
	printf("\n\n");
	printf("Output of do_while_loop(12)\n");
	do_while_loop(12);
	printf("\n\n");
	printf("Output of do_while_loop(-4)\n");
	do_while_loop(-4);
	return (0);
}

/**
 * for_loop - Executes a for loop from startNum to endNum
 * @startNum: Number where we start
 * @endNum: Number where we end
 *
 * Return: 0 on success
 */


int for_loop(int startNum, int endNum)
{
	if (startNum > endNum)
	{
		for (startNum = startNum; startNum >= endNum; startNum--)
		{
			printf("%d, ", startNum);
		}
	}

	else if (startNum < endNum)
	{
		for (endNum = endNum; endNum >= startNum; endNum--)
		{
			printf("%d, ", endNum);
		}
	}

	return (0);
}

/**
 * while_loop - Counts from 0 to endNum
 * @endNum: Number we end on
 *
 * Return: 0 on succes
 */

int while_loop(int endNum)
{
	int i = 0;

	while (i < endNum)
	{
		printf("%d, ", i);
		i++;
	}

	return (0);
}
