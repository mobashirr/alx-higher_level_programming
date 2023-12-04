#include "lists.h"

/**
 * rev - reverse array
 * @arr: array of int
 * @len: length of array
*/
void rev(int **arr, int len)
{
	int i, j, k;

	k = len / 2;

	for (i = 0; i < k; i++)
	{
		j = *arr[i];
		*arr[i] = *arr[len];
		*arr[len] = j;
		++i;
		--len;
	}
}
/**
 * count - count length of linked list
 * @head: head of list
 * Return: length
*/
int count(listint_t *head)
{
	listint_t *temp = NULL;
	int i = 0;

	if (!head)
		return (0);

	temp = head;

	while (temp)
	{
		if (temp->next)
			temp = temp->next;
		else
			temp = NULL;
		++i;
	}
	/*printf("len=%d\n",i); */
	return (i);
}
/**
 * is_palindrome - check for palindrome linked list
 * @head: head of list
 * Return: 1 if palindrome of 0 if not
*/
int is_palindrome(listint_t **head)
{
	listint_t *fast, *slow, *new;

	if (!(*head))
		return (1);
	fast = (*head);
	if (fast->next && !fast->next->next->next)
		return(0);

	slow = fast;
	new = NULL;

	while(1)
	{
		fast = fast->next->next;
		slow = slow->next;
		if (!fast->next->next)
		{
			new = slow->next;
			break;
		}
		else if (!fast->next)
		{
			new = slow->next;
			break;
		}
	}

	slow = (*head);
	while (new)
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