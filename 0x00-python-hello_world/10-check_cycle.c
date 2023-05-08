#include "lists.h"

/**
* check_cycle - checks if a linked list has a cycle
* @list: head node
*
* Return: 1 if there is a cycle, 0 if otherwise
*/

int check_cycle(listint_t *list)
{
	listint_t *slow, *fast;

	slow = fast = list;

	while (slow && fast && fast->next)
	{
		slow = slow->next;
		fast = fast->next->next;

		if (fast == slow)
		{
			return (1);
		}
	}
	return (0);

}
