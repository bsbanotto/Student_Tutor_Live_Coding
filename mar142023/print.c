#include "lists.h"

/**
 * print_list - Function that prints all elements of a list
 * @h: pointer to head of singly linked list
 *
 * Return: Number of elements in list
 */

size_t print_list(const list_t *h)
{
	const list_t *temp = h;
	unsigned int i = 0;

	while (temp)
	{
		printf("<%p> [%u] %s\n", (void *)temp, temp->len, temp->str);
		temp = temp->next;
		i++;
	}
	return (i);
}
