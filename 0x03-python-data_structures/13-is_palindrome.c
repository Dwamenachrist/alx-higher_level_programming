#include "lists.h"

/**
 * is_palindrome - Checks if a singly linked list is a palindrome.
 * @head: Double pointer to the head of the list
 * Return: 0 if not a palindrome, 1 if palindrome
 */
int is_palindrome(listint_t **head)
{
    listint_t *slow = *head, *fast = *head, *prev, *temp;

    if (!head || !(*head))  /* Handle empty list */
        return (1);

    /* Find middle */
    while (fast && fast->next)  
    {
        slow = slow->next;
        fast = fast->next->next;
    }

    /* Reverse second half */
    prev = NULL;
    while (slow)
    {
        temp = slow->next;
        slow->next = prev;
        prev = slow;
        slow = temp;
    }

    /* Compare halves */
    temp = *head;
    while (prev)
    {
        if (temp->n != prev->n)
            return (0);
        temp = temp->next;
        prev = prev->next;
    }
    return (1);
}
