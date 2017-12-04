#include "lists.h"

/**
 * check_cycle    - Checks if @list is a circular list
 *
 * @list:           A singly linked list
 *
 * Return:          (0) @list is not circularly linked
 *                  (1) @list is circularly linked
 */

int check_cycle(listint_t *list)
{
	int *address = &list->n;
	int flag = 0;

	while (list != NULL)
	{
		if (flag != 0)
		{
			if (&list->n == address)
			{
				return (1);
			}

		}
		flag = 1;
		list = list->next;
	}

	return (0);
}
