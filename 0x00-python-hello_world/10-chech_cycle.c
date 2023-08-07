#include "lists.h"

/**
 * check_cycle - This function checks if a singly linked list has a cycle in it.
 * @list: The function that points to the beginning of the node
 * Return: Return 0 if no cycle, Return 1 if there is a cycle
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