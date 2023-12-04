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
	int len = 0, *arr, i = 0, j;
	int pal = 0;
	listint_t *temp = NULL;

	if (!(*head))
		return (1);

	temp = (*head);
	len = count(temp);
	arr = malloc(sizeof(int) * (len / 2));

	while (i < len / 2 && temp)
	{
		arr[i] = temp->n;
		if (temp->next)
			temp = temp->next;
		else
			break;
		i++;
	}
	rev(&arr, len / 2);

	if (len % 2 != 0 && temp->next)
		temp = temp->next;

	for (j = 0; temp; j++)
	{
		if (temp->n != arr[j])
		{
			pal = 1;
			break;
		}
		if (temp->next)
			temp = temp->next;
		else
		temp = NULL;
	}
	return (pal);
}
