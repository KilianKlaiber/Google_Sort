"""Order the list with the minimum number of swaps of adjacent elements:

Explanation: Swapping the largest and shortest numbers to the beginning
and ending does not affect the relative order of the residual numbers.
Each swap is necessary, in order to bring the largest and smallest numbers
to their final position. Since the algorithm never perform an unnecessary swap,
it reaches the final solution with the least number of swaps.


If the elements in the list are not unique then the smallest index for the smallest number
, which is closest to the beginning, is chosen and vice versa
for the largest number closest to the end. This guarantees that the algorithm
also uses the minimum amount of swaps for lists with duplicates.
"""


from error_handlers import handle_list_error
from helper_functions import largest_number, smallest_number, swap, ordered


def main():
    """Execute recursive ordering function"""

    unordered_list = [2, 7, 3, 8, 7, 7, 5, 2, 1, 4, 5, 4, 3, 5, 6, 8]

    ordered_list = recursive_reordering(unordered_list)

    print("ordered list: ", ordered_list)


def recursive_reordering(unordered_list: list[int]) -> list[int]:
    """
    Return list of ordered integers.
    """

    handle_list_error(unordered_list)

    # Exit conditions for recursion

    if len(unordered_list) <= 1:
        return unordered_list

    if len(unordered_list) == 2:
        if ordered(unordered_list, 0):
            return unordered_list
        else:
            return swap(unordered_list, 0)

    largest_number_index = largest_number(unordered_list)
    smallest_number_index = smallest_number(unordered_list)
    last_index = len(unordered_list) - 1
    smallest_number_distance = smallest_number_index
    largest_number_distance = last_index - largest_number_index

    if smallest_number_distance <= largest_number_distance:
        # Move the smallest number to the start of the list
        for index in range(smallest_number_distance - 1, -1, -1):
            unordered_list = swap(unordered_list, index)

        if len(unordered_list) >= 2:
            # Recursively order the remaining list without the first element.
            return [unordered_list[0]] + recursive_reordering(unordered_list[1:])
        else:
            return unordered_list

    else:
        # Move the largest number to the end of the list.
        for index in range(largest_number_index, last_index):
            unordered_list = swap(unordered_list, index)

        if len(unordered_list) >= 2:

            # Recursively order the remaining list without the last element.
            return recursive_reordering(unordered_list[:-1]) + [unordered_list[-1]]
        else:
            return unordered_list



if __name__ == "__main__":
    main()
