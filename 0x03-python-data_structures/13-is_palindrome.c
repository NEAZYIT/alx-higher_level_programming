#include <stdio.h>
#include <stdlib.h>
#include "lists.h"

/**
 * reverse_listint - reverses a linked list
 * @head: pointer to the first node in the list
 *
 * Return: pointer to the first node in the new list
 */

listint_t *reverse_listint(listint_t *head)
{
    listint_t *prev = NULL;
    listint_t *current = head;
    listint_t *next = NULL;

    while (current != NULL)
    {
        next = current->next;
        current->next = prev;
        prev = current;
        current = next;
    }

    return (prev);
}

/**
 * is_palindrome - checks if a linked list is a palindrome
 * @head: double pointer to the linked list
 *
 * Return: 1 if it is, 0 if not
 */

int is_palindrome(listint_t **head)
{
    if (*head == NULL || (*head)->next == NULL)
        return (1);

    listint_t *slow = *head;
    listint_t *fast = *head;
    listint_t *prev = NULL;

    // Find the middle of the linked list
    while (fast && fast->next)
    {
        fast = fast->next->next;
        prev = slow;
        slow = slow->next;
    }

    // If the length of the list is odd, move slow one step forward
    if (fast)
        slow = slow->next;

    // Reverse the second half of the list
    prev->next = reverse_listint(slow);

    listint_t *first = *head;
    listint_t *second = prev->next;

    // Compare the first half and reversed second half
    while (second)
    {
        if (first->n != second->n)
            return (0);
        first = first->next;
        second = second->next;
    }

    // Restore the original list by reversing the second half again
    prev->next = reverse_listint(prev->next);

    return (1);
}
