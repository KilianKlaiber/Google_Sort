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
from helper_functions import get_largest_item_index, get_smallest_item_index, swap, ordered


def main():
    """Execute recursive ordering function"""

    unordered_list = [2, 7, 3, 8, 7, 7, 5, 2, 1, 4, 5, 4, 3, 5, 6, 8]

    ordered_list = google_sort(unordered_list)

    print("ordered list: ", ordered_list)


def google_sort(unordered_list: list[int]) -> list[int]:
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

    largest_item_index = get_largest_item_index(unordered_list)
    smallest_item_index = get_smallest_item_index(unordered_list)
    last_index = len(unordered_list) - 1
    largest_item_distance = last_index - largest_item_index

    if smallest_item_index <= largest_item_distance:
        # Move the smallest number to the start of the list
        for index in range(smallest_item_index - 1, -1, -1):
            unordered_list = swap(unordered_list, index)

        if len(unordered_list) >= 2:
            # Recursively order the remaining list without the first element.
            return [unordered_list[0]] + google_sort(unordered_list[1:])
        else:
            return unordered_list

    else:
        # Move the largest number to the end of the list.
        for index in range(largest_item_index, last_index):
            unordered_list = swap(unordered_list, index)

        if len(unordered_list) >= 2:

            # Recursively order the remaining list without the last element.
            return google_sort(unordered_list[:-1]) + [unordered_list[-1]]
        else:
            return unordered_list



if __name__ == "__main__":
    main()
