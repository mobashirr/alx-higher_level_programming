#include "lists.h"

listint_t *insert_node(listint_t **head, int number)
{

	listint_t *temp, *new, *next;

	if (!head)
	{
		new = add_nodeint_end(head, number);
		return(new);
	}

	temp = (*head);

	while(temp && temp->next)
	{
		if(temp->next->n > number || (*head)->n < number)
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
	}

		return(NULL);
}
/*
int main(void)
{
    listint_t *head;

    head = NULL;
    add_nodeint_end(&head, 0);
    add_nodeint_end(&head, 1);
    add_nodeint_end(&head, 2);
    add_nodeint_end(&head, 3);
    add_nodeint_end(&head, 4);
    add_nodeint_end(&head, 98);
    add_nodeint_end(&head, 402);
    add_nodeint_end(&head, 1024);
    print_listint(head);

    printf("-----------------\n");

    insert_node(&head, 27);

    print_listint(head);

    free_listint(head);

    return (0);
}
*/
