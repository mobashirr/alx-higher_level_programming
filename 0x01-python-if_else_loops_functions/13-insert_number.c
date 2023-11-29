#include "lists.h"

listint_t *add(listint_t **head, int num)
{
	listint_t *temp = NULL, *new, *next;
	/*set if no list or if head->n less that number*/

			if((*head))
				temp = (*head);

			/*set he new node:*/
			new = malloc(sizeof(listint_t));

			if(!new)
				return(NULL);
			new->n = num;	/*set the value*/

			if(temp)
			{
				if (temp->n > num)		/*case insert at first num < first elment*/
				{
					new->next = temp;
					(*head) = new;		/*update the head required*/
					return(new);
				}
				if(temp->next)
				{
					next = temp->next;
					temp = new;
					new->next = next;
					return(temp);
				}
				return(temp);
			}
			new->next = NULL;
			(*head) = new;
			return(new);	/*return the new node*/
}
listint_t *insert_node(listint_t **head, int number)
{

	listint_t *temp, *new, *next;

/*the fuction add handle some cases were the list is not valid 
	or the number is less than the first elment*/
	if(!(*head) || (*head)->n > number)
		return(add(head, number));

	temp = (*head);		/*we don't need to lost the head*/

	/*my algorithm is to keep going on the linkedlist 
	till it find element that is less than number 
	but the next node contain number that is bigger than than number*/
	while(temp && temp->next)
	{
		if(temp->next->n > number)
		{
			/*set he new node:*/
			new = malloc(sizeof(listint_t));
			next = temp->next;	/*save the next ptr*/

			if(!new)
				return(NULL);
			new->n = number;	/*set the value*/
			new->next = next;	/*set the next ptr*/
			temp->next = new;
			return(new);	/*return the new node*/
		}
		temp = temp->next;
		if(!temp->next && temp->n < number)
		{
			new = malloc(sizeof(listint_t));
			new->n = number;	/*set the value*/
			temp->next = new;
			return(new);
		}
	}

		return(NULL);
}
/*
int main(void)
{
    listint_t *head;

    head = NULL;

    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 2);
    add_nodeint_end(&head, 3);
    add_nodeint_end(&head, 4);
    add_nodeint_end(&head, 402);
    add_nodeint_end(&head, 1024);
    print_listint(head);

    printf("-----------------\n");

    insert_node(&head, -7);
	add_nodeint_end(&head, 3);
    print_listint(head);

    free_listint(head);

    return (0);
}
*/
