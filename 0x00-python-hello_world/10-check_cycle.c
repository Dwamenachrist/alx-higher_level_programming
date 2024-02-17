#include "lists.h"

/**
 * check_cycle - Determines if a singly linked list contains a cycle 
 * (where a node points back to a previous node in the list).  
 * 
 * Implementation uses the 'Tortoise and Hare' technique:  two pointers traverse 
 * the list at different speeds. If they ever meet, a cycle is present.  
 * 
 * @list: Pointer to the head of the linked list.
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */

int check_cycle(listint_t *list) {

    if (list == NULL || list->next == NULL) 
        return (0); 

    listint_t *slow = list;
    listint_t *fast = list->next;

    while (slow && fast && fast->next) { 
        if (slow == fast) {
            return 1; // Cycle found
        }
        slow = slow->next; 
        fast = fast->next->next; 
    }

    return 0; // No cycle 
}
