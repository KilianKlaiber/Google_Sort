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

from typing import Any


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
        for index in range(smallest_number_distance - 1, -1, -1):
            unordered_list = swap(unordered_list, index)

        if len(unordered_list) >= 2:
            return [unordered_list[0]] + recursive_reordering(unordered_list[1:])
        else:
            return unordered_list

    else:
        for index in range(largest_number_index, last_index):
            unordered_list = swap(unordered_list, index)

        if len(unordered_list) >= 2:
            return recursive_reordering(unordered_list[:last_index]) + [
                unordered_list[-1]
            ]
        else:
            return unordered_list


def largest_number(unordered_list: list[int]) -> int:
    """Return index of largest number in list"""

    handle_list_error(unordered_list)

    largest_number = unordered_list[0]
    largest_number_index = 0

    for index, value in enumerate(unordered_list):

        handle_value_error(value)

        # >= instead of > in order to get the last index, if the largest_number is not unique
        if value >= largest_number:
            largest_number = value
            largest_number_index = index

    return largest_number_index


def smallest_number(unordered_list: list[int]) -> int:
    """Return index of smallest number in list"""

    handle_list_error(unordered_list)

    smallest_number = unordered_list[0]
    smallest_number_index = 0

    for index, value in enumerate(unordered_list):
        handle_value_error(value)
        # < instead of <= in order to get the first index, if the smallest_number is not unique
        if value < smallest_number:

            smallest_number = value
            smallest_number_index = index

    return smallest_number_index


def ordered(unordered_list: list[int], index: int) -> bool:
    """
    Returns True, if adjacent numbers at index, index +1 are ordered, 
    else Return False.
    """

    # Error Handling

    handle_list_error(unordered_list)
    handle_index_error(unordered_list, index)

    # Ordering adjacent values

    first_index = index
    first_value = unordered_list[first_index]
    second_index = index + 1
    second_value = unordered_list[second_index]

    handle_value_error(first_value)
    handle_value_error(second_value)

    if second_value >= first_value:
        return True
    else:
        return False


def swap(unordered_list: list[int], index: int) -> list[int]:
    """Returns list of integers with elements at index and index+1 swapped
    """

    # Error Handling

    handle_list_error(unordered_list)
    handle_index_error(unordered_list, index)

    # Swapping adjacent values:

    first_index = index
    first_value = unordered_list[index]
    second_index = index + 1
    second_value = unordered_list[second_index]

    unordered_list[first_index] = second_value
    unordered_list[second_index] = first_value

    return unordered_list


def handle_list_error(unordered_list: Any):
    """Raise type error if unordered list is not of type list"""
    if not isinstance(unordered_list, list):
        raise TypeError(f"Unordered list {unordered_list} must be of type list[int]")


def handle_index_error(unordered_list: Any, index: Any):
    "Raise Error if index is not integer or out of bounds"

    if not isinstance(index, int):
        raise TypeError(f"The index {index} must be of type integer")

    last_index = len(unordered_list) - 1
    if index >= last_index or index < 0:

        error_message = f"Your index {index} is out of bounds."

        raise IndexError(error_message)


def handle_value_error(value: Any):
    """Raise error if value ist not of type int"""
    if not isinstance(value, int):
        raise TypeError(f"Element {value} must be of type int")


if __name__ == "__main__":
    main()
