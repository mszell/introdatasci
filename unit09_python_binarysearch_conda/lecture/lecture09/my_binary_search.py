def binary_search(my_item, my_sorted_list):
    '''
    function that uses the binary search algorithm
    to find whether my_item is in my_list,
    and if so, in which position
    '''

    # define the "search limits"
    left_limit = 0
    right_limit = len(my_sorted_list) - 1

    # while we still have a list with more than 1 number to search:
    while left_limit <= right_limit:
        middle_index = (right_limit + left_limit) // 2
        # if at the "middle" position we have something smaller than my_item,
        # my_item must be in the right half of the search space,
        # so we need to modify the left limit:
        if my_sorted_list[middle_index] == my_item:
            return True
        elif my_sorted_list[middle_index] < my_item:
            left_limit = middle_index + 1
        # if at the "middle" position we have something BIGGER than my_item,
        # then my_item must be in the left half of the search space,
        # so we need to modify the right limit:
        else:
            right_limit = middle_index - 1
        
    return False