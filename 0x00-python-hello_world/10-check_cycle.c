#include "lists.h"
/**
 * check_cycle - Checks if a singly linked list has a cycle in it.
 * @list: A pointer to the head of the listint_t list.
 *
 * Return: 0 if there is no cycle, 1 if there is a cycle.
 */
int check_cycle(listint_t *list)
{
    listint_t *tortoise = list;
    listint_t *hare = list;

    // Traverse the list
    while (hare != NULL && hare->next != NULL) {
        tortoise = tortoise->next;            // Move tortoise one step
        hare = hare->next->next;              // Move hare two steps

        // If hare and tortoise meet, there's a cycle
        if (tortoise == hare) {
            return 1;
        }
    }

    // If we reach here, there is no cycle
    return 0;
}
