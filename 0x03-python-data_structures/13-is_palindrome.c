#include "lists.h"

/**
 * is_palindrome - check for palindrome linked list
 * @head: head of list
 * Return: 1 if palindrome of 0 if not
*/
int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *new;

	if (!(*head) || !((*head)->next))
		return (1);

	fast = (*head);
	slow = (*head);
	new = NULL;	/*this will be head of the second half of list*/

	while(1)
	{
		if (fast->next && fast->next->next)
			fast = fast->next->next;
		if (slow->next)
			slow = slow->next;

		if (!fast->next->next)
		{	/*case even:*/
			new = slow->next;
			break;
		}
		else if (!fast->next)
		{	/*case odd*/
			new = slow->next->next;
			break;
		}
	}

	slow = (*head);
	while (new && slow)
	{
		if (new->n != slow->n)
			return(1);
		if (new->next && slow->next)
		{
			new = new->next;
			slow = slow->next;
		}
		else
			break;
	}
	return(0);
}

/**
 * reverse_list - reverse a linked list
 * @head: head of list
 * Return: head of reversed list
 */
listint_t *rev(listint_t **head)
{
    listint_t *prev = NULL, *current = *head, *next = NULL;

    while (current)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return prev;
}