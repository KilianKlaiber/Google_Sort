from error_handlers import handle_index_error, handle_list_error, handle_value_error


def get_largest_item_index(unordered_list: list[int]) -> int:
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


def get_smallest_item_index(unordered_list: list[int]) -> int:
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

    handle_list_error(unordered_list)
    handle_index_error(unordered_list, index)

    first_value = unordered_list[index]
    second_value = unordered_list[index + 1]

    handle_value_error(first_value)
    handle_value_error(second_value)

    return second_value >= first_value


def swap(unordered_list: list[int], index: int) -> list[int]:
    """Returns list of integers with elements at index and index+1 swapped"""

    handle_list_error(unordered_list)
    handle_index_error(unordered_list, index)

    first_value = unordered_list[index]
    second_value = unordered_list[index + 1]

    handle_value_error(first_value)
    handle_value_error(second_value)

    unordered_list[index] = second_value
    unordered_list[index + 1] = first_value

    return unordered_list

