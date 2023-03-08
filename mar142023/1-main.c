#include "lists.h"

/**
 * main - check the code
 *
 * Return: Always 0.
 */
int main(void)
{
	list_t *head;
	list_t My = {"My", 25, NULL};
	list_t favorite = {"favorite", 25, NULL};
	list_t AXOLOTL = {"AXOLOTL!!", 25, NULL};
	size_t n;

	head = &My;
	head->next = &favorite;
	head->next->next = &AXOLOTL;

	n = print_list(head);
	printf("\t-> %lu elements\n", n);

/*
	add_node_location(&head, "animal", 1);
	n = print_list(head);
	printf("\t-> %lu elements\n", n);

	add_node_location(&head, "the", 2);
	n = print_list(head);
	printf("\t-> %lu elements\n", n);

	add_node_location(&head, "is", 2);
	n = print_list(head);
	printf("\t-> %lu elements\n", n);
*/

	return (0);
}
