#include "lists.h"

/**
 * is_palindrome - check for palindrome linked list
 * @head: head of list
 * Return: 1 if palindrome, 0 if not
 */
int is_palindrome(listint_t **head)
{
    listint_t *fast, *slow, *new;

    if (!(*head) || !((*head)->next))
        return (1);  /* Empty list or single node is a palindrome */

    fast = (*head);
    slow = (*head);
    new = NULL; /* This will be the head of the second half of the list */

    while (fast && fast->next)
    {
        fast = fast->next->next;
        slow = slow->next;
    }

    /* Reverse the second half of the list */
    new = reverse_list(&slow);

    /* Compare the first and reversed second halves of the list */
    while (new && *head)
    {
        if (new->n != (*head)->n)
            return (0); /* Not a palindrome */

        new = new->next;
        *head = (*head)->next;
    }

    return (1); /* Palindrome */
}

/**
 * reverse_list - reverse a linked list
 * @head: head of list
 * Return: head of reversed list
 */
listint_t *reverse_list(listint_t **head)
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

