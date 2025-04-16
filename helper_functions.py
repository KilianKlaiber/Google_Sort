from error_handlers import handle_index_error, handle_list_error, handle_value_error


def get_largest_item_index(unordered_list: list[int]) -> int:
    """Return index of largest number in list"""
    handle_list_error(unordered_list)
    
    def get_value(index: int) -> tuple:
        return unordered_list[index]
        
    # range(len(unordered_list)-1, -1, -1) loops from the largest index
    # to the smalles index of the unordered list
    # get_value returns the value for each index
    # max returns the first index, which yields the smallest value.
    largest_item_index = max(range(len(unordered_list)-1, -1, -1), key=get_value)

    return largest_item_index


def get_smallest_item_index(unordered_list: list[int]) -> int:
    """Return index of smallest number in list"""
    
    handle_list_error(unordered_list)
    
    def get_value(index: int) -> int:
        return unordered_list[index]
        
    # range(len(unordered_list)) represents the indexes of the unordered list
    # return_value returns the value for each index
    # min returns the index, which yields the smallest value.
    smallest_item_index = min(range(len(unordered_list)), key=get_value)

    return smallest_item_index


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
    
    # Create a copy of the list
    swapped_list = unordered_list[:]

    swapped_list[index] = second_value
    swapped_list[index + 1] = first_value

    return swapped_list

