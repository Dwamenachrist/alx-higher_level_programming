#include "lists.h"
#include <stdlib.h> 
#include <stddef.h> 

/**
 * Required for the 'listint_t' data structure and 'add_nodeint_end' function
 * used within the 'insert_node' implementation.
 */

listint_t *insert_node(listint_t **head, int number)
{
    listint_t *new_node, *current;

    /* Allocate memory for the new node */
    new_node = malloc(sizeof(listint_t));
    if (new_node == NULL)
        return (NULL);

    /* Initialize the new node */ 
    new_node->n = number;

    /* Handle insertion at the head of the list */
    if (*head == NULL || (*head)->n >= number) 
    {
        new_node->next = *head;
        *head = new_node;
        return (new_node);
    }

    /* Find the insertion point in the sorted list */
    current = *head;
    while (current->next != NULL && current->next->n < number)
        current = current->next;  

    /* Insert the new node */
    new_node->next = current->next;
    current->next = new_node;
    return (new_node);
}