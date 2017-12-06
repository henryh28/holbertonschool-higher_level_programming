#include "lists.h"

/**
 * insert_node   - Insert @number into @head
 *
 * @head:            Sorted singly linked list
 * @number:          Number to be inserted into @head
 *
 * Return:           Success: Address of the new node
 *                   Failure: NULL
 */

listint_t *insert_node(listint_t **head, int number)
{
	listint_t *current = *head;
	listint_t *new;

	new = malloc(sizeof(listint_t));
	if (new == NULL)
		return (NULL);
	new->n = number;

	if (*head == NULL)
	{
		new->next = NULL;
		*head = new;
		return (*head);
	}
	while (current != NULL)
	{
		if (number < current->n)
		{
			new->next = *head;
			*head = new;
			return (*head);
		}
		else
		{
			if (current->next == NULL)
			{
				current->next = new;
				break;
			}
			else if (number <= current->next->n)
			{
				new->next = current->next;
				current->next = new;
				break;
			}
			else
				current = current->next;
		}
	}
	return (*head);
}
