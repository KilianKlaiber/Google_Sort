def main():

    unordered_list = [2, 7, 3, 8, 7, 7, 5, 2, 1, 4, 5, 4, 3, 5, 6, 8]

    ordered_list = recursive_reordering(unordered_list)

    print("ordered list", ordered_list)


def recursive_reordering(unordered_list: list[int]) -> list[int]:
    """Order the list with the minimun number of swaps of adjacent elements:

    Explanation: Swapping the largest and shortest numbers to the beginning
    and ending does not affect the relative order of the residual numbers.
    Each swap is necessary, in order to bring the largest and smallest numbers
    to their final position. Since the algorithm never perform an unnecessary swap,
    it reaches the final solution with the least number of swaps.


    If the elements in the list are not unique then the smallest index for the smallest number
    , which is closest to the beginning, is chosen and and vice versa
    for the largest number closest to the end. This guarantees that the algorithm
    also uses the minimum amount of swaps for lists with duplicates.

    Args:
        unordered_list (list[int]): unordered list of integers

    Returns:
        list[int]: ordered list of integers.
    """
    print("unordered_list", unordered_list)

    # Exit conditions for recursion

    if len(unordered_list) <= 1:
        return unordered_list

    if len(unordered_list) == 2:
        if ordered(unordered_list, 0):
            return unordered_list
        else:
            return swap(unordered_list, 0)

    # identifying index of largest and smallest values.
    largest_number_index = largest_number(unordered_list)
    smallest_number_index = smallest_number(unordered_list)
    last_index = len(unordered_list) - 1
    smallest_number_distance = smallest_number_index
    largest_number_distance = last_index - largest_number_index

    if smallest_number_distance <= largest_number_distance:
        # move the smallest number to the beginning of the list
        # by swapping consecutive numbers
        for index in range(smallest_number_distance - 1, -1, -1):
            unordered_list = swap(unordered_list, index)

        # Remove the first element from the list, which is ordered and
        # Recursively order the rest of the list.
        # Add the first element to the returned ordered rest list.
        if len(unordered_list) >= 2:
            first_ordered_index = [unordered_list[0]]
            return first_ordered_index + recursive_reordering(unordered_list[1:])
        else:
            return unordered_list

    else:
        for index in range(largest_number_index, last_index):
            unordered_list = swap(unordered_list, index)

        last_ordered_index = [unordered_list[-1]]
        unordered_list_without_last_index = unordered_list[:last_index]

        if len(unordered_list) >= 2:
            return recursive_reordering(unordered_list_without_last_index) + last_ordered_index
        else:
            return unordered_list


def largest_number(unordered_list: list[int]) -> int:
    """Return index and value of largest number in list

    Args:
        unordered_list (list[int]): unordered list of integers

    Returns:
        tuple (int): index of the largest number in the list
    """
    largest_number = unordered_list[0]
    largest_number_index = 0

    for index, value in enumerate(unordered_list):
        # The >= makes sure that the largest index for the largest value is returned
        # in case the largest value occurs several times.
        if value >= largest_number:
            largest_number = value
            largest_number_index = index

    return largest_number_index


def smallest_number(unordered_list: list[int]) -> int:
    """Return index and value of smalles number in list

    Args:
        unordered_list (list[int]): unordered list of integers

    Returns:
        tuple[int]: index of the smallest number in the list
    """

    smallest_number = unordered_list[0]
    smallest_number_index = 0

    for index, value in enumerate(unordered_list):
        # The smaller sign < guarantees that the smallest index is chosen,
        # even if the smallest value occurs several times.
        if value < smallest_number:
            smallest_number = value
            smallest_number_index = index

    return smallest_number_index


def ordered(unordered_list: list[int], index: int) -> bool:
    """Determine, whether adjacent numbers are ordered correctly

    Args:
        unordered_list (list[int]): unordered list of numbers
        index (int): first index of adjacent indices to be ordered

    Returns:
        bool: True, ordered, False if unordered.
    """

    # Error Handling

    if not isinstance(index, int):
        raise TypeError("The index must be of type integer")

    last_index = len(unordered_list) - 1
    if index >= last_index or index < 0:
        error_message = (
            "The chosen index must be greater than or equal to 0\n"
            f"and smaller than the last index {last_index} of the list.\n"
            f"Your index {index} is out of bounds."
        )
        raise IndexError(error_message)

    # Ordering adjacent values

    first_index = index
    first_value = unordered_list[first_index]
    second_index = index + 1
    second_value = unordered_list[second_index]

    if second_value >= first_value:
        return True
    else:
        return False


def swap(unordered_list: list[int], index: int) -> list[int]:
    """Swap Elements
        Swap the elements in the list positioned at the index with the
        element at the next index

    Args:
        unordered_list (list[int]): list of integers
        index (int): index of the first integer

    Returns:
        list[int]: list of integers with elements and index and index+1 swapped
    """

    # Error Handling

    if not isinstance(index, int):
        raise TypeError("The index must be of type integer")

    last_index = len(unordered_list) - 1
    if index >= last_index or index < 0:

        error_message = "The chosen index must be greater than or equal to 0 \n"
        error_message += f"or smaller than the last index {last_index} of the list\n"
        error_message += f"Your index {index} is out of bounds"

        raise IndexError(error_message)

    # Swapping adjacent values:

    first_index = index
    first_value = unordered_list[index]
    second_index = index + 1
    second_value = unordered_list[second_index]

    unordered_list[first_index] = second_value
    unordered_list[second_index] = first_value

    return unordered_list


if __name__ == "__main__":
    main()
