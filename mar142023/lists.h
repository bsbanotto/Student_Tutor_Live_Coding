#ifndef LIST_H
#define LIST_H

/* Standard libraries */
#include <stddef.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

/* Structures */

/**
 * struct list_s - singly linked list
 * @str: string - (malloc'ed string)
 * @len: length of the string
 * @next: points to the next node
 *
 * Description: singly linked list node structure
 */

typedef struct list_s
{
	char *str;
	unsigned int len;
	struct list_s *next;
} list_t;

/* Prototypes */

size_t print_list(const list_t *h);
list_t *add_node_location(list_t **head, const char *str, int position);


/* Compile Command */

/* gcc -Wall -pedantic -Werror -Wextra -std=gnu89 *.c -o runit */

#endif
