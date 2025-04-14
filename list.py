def main():

    unordered_list = [2, 7, 3, 8, 7, 7, 5, 2, 1, 4, 5, 4, 3, 5, 6, 8]

    ordered_list = recursive_reordering(unordered_list)

    print("ordered list", ordered_list)


def recursive_reordering(unordered_list: list[int]) -> list[int]:
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

    largest_number_index = largest_number(unordered_list)
    smallest_number_index = smallest_number(unordered_list)
    last_index = len(unordered_list) - 1
    smallest_number_distance = smallest_number_index
    largest_number_distance = last_index - largest_number_index

    if smallest_number_distance <= largest_number_distance:
        for index in range(smallest_number_distance - 1, -1, -1):
            unordered_list = swap(unordered_list, index)
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
            return (
                recursive_reordering(unordered_list_without_last_index)
                + last_ordered_index
            )
        else:
            return unordered_list


def largest_number(unordered_list: list[int]) -> int:
    """Return index of largest number in list"""
    largest_number = unordered_list[0]
    largest_number_index = 0

    for index, value in enumerate(unordered_list):
        # >= instead of > in order to get the last index, if the largest_number is not unique
        if value >= largest_number:
            largest_number = value
            largest_number_index = index

    return largest_number_index


def smallest_number(unordered_list: list[int]) -> int:
    """Return index of smallest number in list"""

    smallest_number = unordered_list[0]
    smallest_number_index = 0

    for index, value in enumerate(unordered_list):
        # < instead of <= in order to get the first index, if the smallest_number is not unique
        if value < smallest_number:
            smallest_number = value
            smallest_number_index = index

    return smallest_number_index


def ordered(unordered_list: list[int], index: int) -> bool:
    """Determine, whether adjacent numbers are ordered correctly

    Returns:
        bool: True, if adjacent numbers are ordered, else False.
    """

    # Error Handling

    if not isinstance(index, int):
        raise TypeError("The index must be of type integer")

    last_index = len(unordered_list) - 1
    if index >= last_index or index < 0:
        error_message = f"Your index {index} is out of bounds."

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
    """Swap adjacent Elements

    Returns:
        list[int]: list of integers with elements at index and index+1 swapped
    """

    # Error Handling

    if not isinstance(index, int):
        raise TypeError("The index must be of type integer")

    last_index = len(unordered_list) - 1
    if index >= last_index or index < 0:

        error_message = f"Your index {index} is out of bounds."

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
