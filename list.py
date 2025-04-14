

def main():
    
    uno_list = [2, 7, 3, 8, 7, 7, 5, 2, 1, 4, 5, 4, 3, 5, 6, 8]
    
    
    ord_list = recursive_reordering(uno_list)
    
    print("ordered list", ord_list)

def recursive_reordering(uno_list: list[int]) -> list[int]:
    """Order the list with the minimun number of swaps of adjacent elements:
    
    Find the largest and smallest number in the list
    Find the distance of the smallest number to the beginning
    and the distance of the largest number to the end of the list
    Chose to swap the smallest number to the beginning, 
    if its distance is the smallest. Otherwise swap the larget number
    to the end of the list. Detach the smallest number from the
    beginning or the largest number from the end of the list.
    Recursively perform the swap on the rest of the list and 
    add the result together with the beginng or end.
    This algorithm orders the list with the minimum number of swaps.
    
    Explanation: Swapping the largest and shortest numbers to the beginning
    and ending does not affect the relative order of the residual numbers.
    Each swap is necessary, in order to bring the largest and smallest numbers
    to their final position. Since I never perform an unnecessary swap,
    I reach the order with the least number of swaps.
    
    
    If the elements in the list are not unique then the smallest index for the smallest number
    , which is closest to the beginning, is chosen and and vice versa
    for the largest number closest to the end. This guarantees that the algorithm
    also uses the minimum amount of swaps for lists with duplicates.

    Args:
        uno_list (list[int]): unordered list of integers

    Returns:
        list[int]: ordered list of integers.
    """
    print("uno_list", uno_list)
    
    # Exit conditions for recursion
    
    if len(uno_list) <= 1:
        return uno_list
    
    if len(uno_list) == 2:
        if ordered(uno_list, 0):
            return uno_list
        else:
            return swap(uno_list,0)
    
    # identifying largest and smallest values and the respective indices
    largest_tuple = largest_number(uno_list)
    smallest_tuple = smallest_number(uno_list)
    last_index = len(uno_list) - 1
    smallest_distance = smallest_tuple[0]
    largest_distance = last_index - largest_tuple[0]
    
    if smallest_distance <= largest_distance:
        # move the smallest number to the beginning of the list
        # by swapping consecutive numbers
        for index in range(smallest_distance-1, -1, -1):
            uno_list = swap(uno_list, index)
    
        # Remove the first element from the list, which is ordered and
        # Recursively order the rest of the list. 
        # Add the first element to the returned ordered rest list.
        if len(uno_list) >= 2:
            unobeginning = [uno_list[0]]
            return unobeginning + recursive_reordering(uno_list[1:])
        else:
            return uno_list
        
    else:
        for index in range(largest_tuple[0], last_index):
            uno_list = swap(uno_list, index)
            
        unoending = [uno_list[-1]]
        unoslice = uno_list[:last_index]
        
        if len(uno_list) >= 2:   
            return recursive_reordering(unoslice) + unoending
        else:
            return uno_list



def largest_number(uno_list: list[int]) -> tuple[int, int]:
    """Return index and value of largest number in list

    Args:
        uno_list (list[int]): unordered list of integers

    Returns:
        tuple[int, int]: (index, value) of the largest number in the list
    """
    largest_value = uno_list[0]
    largest_index = 0
    
    for index, value in enumerate(uno_list):
        # The >= makes sure that the largest index for the largest value is returned
        # in case the largest value occurs several times.
        if value >= largest_value:
            largest_value = value
            largest_index = index
    
    return(largest_index, largest_value)

def smallest_number(uno_list: list[int]) -> tuple[int, int]:
    
    """Return index and value of smalles number in list

    Args:
        uno_list (list[int]): unordered list of integers

    Returns:
        tuple[int, int]: (index, value) of the smallest number in the list
    """
    
    
    smallest_value = uno_list[0]
    smallest_index = 0
    
    for index, value in enumerate(uno_list):
        # The smaller sign < guarantees that the smallest index is chosen,
        # even if the smallest value occurs several tims.
        if value < smallest_value:
            smallest_value = value
            smallest_index = index
    
    return(smallest_index, smallest_value)

def ordered(uno_list: list[int], index: int) -> bool:
    """Determine, whether adjacent numbers are ordered correctly

    Args:
        uno_list (list[int]): unordered list of numbers
        index (int): first index of adjacent indices to be ordered

    Returns:
        bool: True, ordered, False if unordered.
    """
    
    # Error Handling
    last_index = len(uno_list) -1
    if not isinstance(index, int):
        print("The index must be of type integer")
        return
    
    if index >= last_index or index < 0:
        
        error_message = "The chosen index must be greater than or equal to 0 \n"
        error_message += f"or smaller than the last index {last_index} of the list\n"
        error_message += f"Your index {index} is out of bounds"
        print(error_message)
        return
    
    first_index = index
    first_value = uno_list[first_index]
    second_index = index + 1
    second_value = uno_list[second_index]
    
    if second_value >= first_value:
        return True
    else:
        return False
    

def swap(uno_list: list[int], index: int) -> list[int]:
    """Swap Elements
        Swap the elements in the list positioned at the index with the
        element at the next index

    Args:
        uno_list (list[int]): list of integers
        index (int): index of the first integer

    Returns:
        list[int]: list of integers with elements and index and index+1 swapped 
    """
    
    
    # Error Handling
    
    last_index = len(uno_list) -1
    if not isinstance(index, int):
        print("The index must be of type integer")
        return
    
    if index >= last_index or index < 0:
        
        error_message = "The chosen index must be greater than or equal to 0 \n"
        error_message += f"or smaller than the last index {last_index} of the list\n"
        error_message += f"Your index {index} is out of bounds"
        print(error_message)
        return
    
    first_index = index
    first_value = uno_list[index]
    second_index = index + 1
    second_value = uno_list[second_index]
    
    uno_list[first_index] = second_value
    uno_list[second_index] = first_value
    
    return uno_list
    


if __name__ == "__main__":
    main()