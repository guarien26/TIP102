"""
Understand: search through the list using recursion to find the element and return its index
    inputs: list[ints] and int (to search for)
    outputs: the index of the value found in the list
    constraints: recursion, sorted, log(n)
    edge cases: the list could be empty, and the value could not be in the list

Plan:

    #

    # [1, 3, 5, 6], 5 -> answer would be index 2
    keep track of an index number
    at index 0, if 1 != 5 so call

    if middle < target 5: the recursion should be [middle+1:]
    if middle > target 5: the recursive call should be [:middle -1]


    if the value isnt in the list
    #[1,3,5,6], 2 -> answer should be index 1 because 2 isn't present in the list
    the next value would be greater than 2 so return the index + 1 

"""


def find_cabin_index(cabins, preferred_deck):
    # index, compare numbers
    low = 0
    high = len(cabins) - 1
    middle = (low+high) // 2

    # [1,3,5,6], 2  -> [1,2,3,5,6]
    # if cannot find 2 in the list, return the index of 


    # [1, 3, 5, 6], 5
    # [5,6], 5

    if not cabins:
        return 0

    if cabins[middle] < preferred_deck:
        # result = find_cabin_index(cabins[middle + 1:],preferred_deck)
        # return middle + result
        return middle + find_cabin_index(cabins[middle + 1:],preferred_deck) + 1
    elif cabins[middle] > preferred_deck:
        return find_cabin_index(cabins[:middle],preferred_deck) 
    else:
        return middle




print(find_cabin_index([1, 3, 5, 6], 5))
print(find_cabin_index([1, 3, 5, 6], 2))
print(find_cabin_index([1, 3, 5, 6], 7))