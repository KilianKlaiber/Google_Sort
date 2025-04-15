from typing import Any


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
