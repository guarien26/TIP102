def find_cruise_length(cruise_lengths, vacation_length):
    # Understand
    # input:
    # 1. a list of integers cruise_lengths
    # 2. an integer vacation_length
    # output:
    # boolean
    # constraint:
    # 1. the list sorted in ascending order
    # 2. use binary search
    # edge case:
    # empty list -> return False

    # Plan
    # binary search
    # 1. non-recursive approach
    # use 2 pointers (low, high)
    # middle index = (low + high) // 2
    # if target > middle:
    # low = middle + 1
    # middle = ((low + high) // 2)
    # elif: # target < middle:
    # high = middle - 1
    # middle = ((low + high) // 2)
    # else: # (target == middle):
    # return True
    
    # edge case
    if cruise_lengths == []:
        return False

    low = 0
    high = len(cruise_lengths) - 1

    while low <= high:
        middle = (low + high) // 2
        if vacation_length > cruise_lengths[middle]:
            low = middle + 1
        elif vacation_length < cruise_lengths[middle]:
            high = middle - 1
        else:
            return True
        
    return False


    # 2. recursive approach

    # non-recursive approach
    # low = 0
    # high = len()





print(find_cruise_length([9, 10, 11, 12, 13, 14, 15], 13))
print(find_cruise_length([8, 9, 12, 13, 13, 14, 15], 11))
# True
# False