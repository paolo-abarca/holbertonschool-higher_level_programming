#include "lists.h"

/**
 * is_palindrome - function is palindrome
 *
 * @head: listint_t
 * Return: 1
 */

int is_palindrome(listint_t **head)
{
	listint_t *slow_ptr = *head, *fast_ptr = *head;

	if (*head == NULL)
		return (1);

	while (fast_ptr != NULL && fast_ptr->next != NULL)
	{
		fast_ptr = fast_ptr->next->next;
		slow_ptr = slow_ptr->next;
	}

	slow_ptr = reverse_list(&slow_ptr);
	fast_ptr = *head;

	while (slow_ptr != NULL && fast_ptr != NULL)
	{
		if (slow_ptr->n != fast_ptr->n)
			return (0);
		fast_ptr = fast_ptr->next;
		slow_ptr = slow_ptr->next;
	}

	return (1);
}

/**
 * reverse_list - function reverse linked list
 *
 * @head: double pointer
 * Return: head
 */

listint_t *reverse_list(listint_t **head)
{
	listint_t *prev = NULL;
	listint_t *next = NULL;

	while (*head)
	{
		next = (*head)->next;
		(*head)->next = prev;
		prev = *head;
		*head = next;
	}

	*head = prev;
	return (*head);
}
