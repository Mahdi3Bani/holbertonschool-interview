#include "palindrome.h"

/**
 * sandpiles_sum - checks whether or not a given unsigned integer is a palindrome
 * @n: number to be checked
 * Return: return 1 if n is a palindrome, and 0 otherwise
 */

int is_palindrome(unsigned long n)
{
	unsigned long reverse, original;

	original = n;
	reverse = 0;

	while (n != 0)
	{
		reverse = reverse * 10 + n % 10;
		n /= 10;
	}

	if (original == reverse)
		return 1;
	else
		return 0;
}