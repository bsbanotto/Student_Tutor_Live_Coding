#include "lists.h"

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
	list_t *head;
	list_t Welcome = {"Welcome", 25, NULL};
	list_t THUNDERDOME = {"THUNDERDOME!!", 25, NULL};
	list_t to = {"to", 25, NULL};
	size_t n;

	head = &Welcome;
	head->next = &to;
	head->next->next = &THUNDERDOME;

	n = print_list(head);
	printf("-> %lu elements\n", n);

/*
	add_node_location(&head, "Tulsa", 1);
	n = print_list(head);
	printf("-> %lu elements\n", n);

	add_node_location(&head, "Holberton", 1);
	n = print_list(head);
	printf("-> %lu elements\n", n);
*/

	return (0);
}
