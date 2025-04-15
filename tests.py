import pytest
from list import swap, ordered, smallest_number, largest_number, recursive_reordering

# Testing swap


def test_swap_middle():
    assert swap([1, 2, 3, 4], 1) == [1, 3, 2, 4]


def test_swap_start():
    assert swap([9, 8, 7], 0) == [8, 9, 7]


def test_swap_end_raises_index_error():
    with pytest.raises(IndexError):
        swap([5, 6], 1)  # No element at index+1


def test_swap_single_element_list_raises_index_error():
    with pytest.raises(IndexError):
        swap([1], 0)


def test_swap_empty_list_raises_index_error():
    with pytest.raises(IndexError):
        swap([], 0)


def test_swap_negative_index_raises_index_error():
    with pytest.raises(IndexError):
        swap([1, 2, 3], -1)


def test_swap_invalid_list_type_raises_type_error():
    with pytest.raises(TypeError):
        swap("not a list", 0)


# Testing ordered


def test_ordered_pair_correct_order():
    assert ordered([1, 2, 3], 0) is True
    assert ordered([3, 5, 7], 1) is True


def test_ordered_pair_equal_values():
    assert ordered([4, 4, 5], 0) is True


def test_ordered_pair_wrong_order():
    assert ordered([3, 2, 1], 0) is False
    assert ordered([9, 5], 0) is False


def test_ordered_end_of_list_raises_index_error():
    with pytest.raises(IndexError):
        ordered([1, 2], 1)  # index + 1 is out of bounds


def test_ordered_single_element_list_raises_index_error():
    with pytest.raises(IndexError):
        ordered([1], 0)


def test_ordered_empty_list_raises_index_error():
    with pytest.raises(IndexError):
        ordered([], 0)


def test_ordered_negative_index_raises_index_error():
    with pytest.raises(IndexError):
        ordered([1, 2, 3], -1)


def test_ordered_invalid_list_type_raises_type_error():
    with pytest.raises(TypeError):
        ordered("123", 0)


def test_ordered_invalid_element_type_raises_type_error():
    with pytest.raises(TypeError):
        ordered([1, "a", 3], 1)


# Test smallest number

def test_smallest_number_basic():
    assert smallest_number([5, 3, 9, 1, 7]) == 3  # 1 is smallest at index 3

def test_smallest_number_first_element():
    assert smallest_number([1, 2, 3]) == 0

def test_smallest_number_last_element():
    assert smallest_number([9, 8, 7, 0]) == 3

def test_smallest_number_duplicate_smallest():
    assert smallest_number([4, 1, 2, 1, 3]) == 1  # first occurrence of 1

def test_smallest_number_all_same():
    assert smallest_number([5, 5, 5, 5]) == 0

def test_smallest_number_one_element():
    assert smallest_number([42]) == 0

def test_smallest_number_empty_list_raises_error():
    with pytest.raises(IndexError):  # Accessing unordered_list[0]
        smallest_number([])

def test_smallest_number_invalid_list_type():
    with pytest.raises(TypeError):
        smallest_number("not a list")

def test_smallest_number_non_int_elements_raises_type_error():
    with pytest.raises(TypeError):
        smallest_number([1, 2, "three", 4])

def test_smallest_number_negative_values():
    assert smallest_number([-5, -10, 0, 2]) == 1
    
# Test largest number

def test_largest_number_basic():
    assert largest_number([1, 5, 3, 9, 2]) == 3  # 9 is largest at index 3

def test_largest_number_first_element():
    assert largest_number([10, 2, 3, 4]) == 0

def test_largest_number_last_element():
    assert largest_number([1, 2, 3, 10]) == 3

def test_largest_number_duplicate_largest():
    assert largest_number([4, 10, 7, 10, 3]) == 3  # last occurrence of 10

def test_largest_number_all_same():
    assert largest_number([5, 5, 5, 5]) == 3  # last index

def test_largest_number_one_element():
    assert largest_number([42]) == 0

def test_largest_number_empty_list_raises_index_error():
    with pytest.raises(IndexError):  # unordered_list[0] access fails
        largest_number([])

def test_largest_number_invalid_list_type():
    with pytest.raises(TypeError):
        largest_number("not a list")

def test_largest_number_non_int_elements_raises_type_error():
    with pytest.raises(TypeError):
        largest_number([1, 2, "three", 4])

def test_largest_number_with_negative_values():
    assert largest_number([-10, -5, -1, -7]) == 2  # -1 is the largest


# Test recursive ordering

def test_recursive_reordering_basic():
    assert recursive_reordering([3, 1, 2]) == [1, 2, 3]
    assert recursive_reordering([4, 2, 5, 1, 3]) == [1, 2, 3, 4, 5]

def test_recursive_reordering_already_sorted():
    assert recursive_reordering([1, 2, 3, 4]) == [1, 2, 3, 4]

def test_recursive_reordering_reverse_sorted():
    assert recursive_reordering([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]

def test_recursive_reordering_with_duplicates():
    assert recursive_reordering([4, 2, 5, 2, 3]) == [2, 2, 3, 4, 5]
    assert recursive_reordering([3, 1, 2, 1, 3]) == [1, 1, 2, 3, 3]

def test_recursive_reordering_single_element():
    assert recursive_reordering([42]) == [42]

def test_recursive_reordering_two_elements():
    assert recursive_reordering([2, 1]) == [1, 2]
    assert recursive_reordering([1, 2]) == [1, 2]

def test_recursive_reordering_empty_list():
    assert recursive_reordering([]) == []

def test_recursive_reordering_invalid_list_type():
    with pytest.raises(TypeError):
        recursive_reordering("not a list")

def test_recursive_reordering_non_int_elements():
    with pytest.raises(TypeError):
        recursive_reordering([1, "a", 3])