#include "lists.h"

int is_palindrome(listint_t **head)
{
	int len = 0, *arr,i = 0,j;
	int pal = 0;    /*palndrome*/
	listint_t *temp = NULL;

	if (!(*head))
		return(1);

	temp = (*head);
	len = count(temp);
	arr = malloc(sizeof(int) * (len / 2) );

	while(i < len/2 && temp)
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
			if(temp->n != arr[j])
			{
				pal = 1;
				break;
			}
		if(temp->next)
			temp = temp->next;
		else
		temp = NULL;
	}
	return(pal);
}
