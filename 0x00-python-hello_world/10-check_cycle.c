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

int check_cycle(listint_t *list)
{
	listint_t *current, *check;

	if (list == NULL || list->next == NULL)
		return (0);
	current = list;
	check = current->next;

	while (current != NULL && check->next != NULL
		&& check->next->next != NULL)
	{
		if (current == check)
			return (1);
		current = current->next;
		check = check->next->next;
	}
	return (0);
}