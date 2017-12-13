#include "lists.h"

/**
 * is_palindrome     - Checks if @head is a palindrome
 *
 * @head:              A singly linked list
 *
 * Return:             (1) @head is a palindrome
 *                     (0) @head is not a palindrome
 */

int is_palindrome(listint_t **head)
{
	listint_t *reversed = *head;
	listint_t *right, *left = NULL;
	int counter = 0;
	int *array = NULL;

	while (*head != NULL)
	{
		counter++;
		*head = (*(head))->next;
	}
	array = malloc(sizeof(int) * counter);

	counter = 0;
	while (reversed)
	{
		array[counter] = reversed->n;

		right = reversed->next;
		reversed->next = left;
		left = reversed;
		reversed = right;
		counter++;
	}
	reversed = left;

	counter = 0;
	while (reversed != NULL)
	{
		if (reversed->n != array[counter])
		{
			return (0);
		}
		reversed = reversed->next;
		counter++;
	}

	return (1);
}
