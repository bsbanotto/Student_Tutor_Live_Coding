#include "lists.h"

/**
 * add_node_location - Adds a node at a given location
 * @head: pointer to head of singly linked list
 * @str: string to be added
 * @position: Node to insert new node after
 *
 * Return: Address of head of list, or NULL if failed
 */

list_t *add_node_location(list_t **head, const char *str, int position)
{
	list_t *temp, *new;
	int i;

	temp = malloc(sizeof(list_t));
	if (temp == NULL)
		return (NULL);

	temp->str = strdup(str);

	new = *head;
	for (i = 0; i < position; i++)
	{
		new = new->next;
	}
	temp->next = new->next;
	new->next = temp;

	return (new);
}
