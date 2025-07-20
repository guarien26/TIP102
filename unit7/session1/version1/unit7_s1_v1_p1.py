def count_suits_iterative(suits):
    """
    suits -> list of strings
    count each suit
    """
    count = 0
    for i in suits:
        count+=1
    return count

def count_suits_recursive(suits):
    if not suits:
        return 0
    
    return 1 + count_suits_recursive(suits[:-1])


print(count_suits_iterative(["Mark I", "Mark II", "Mark III"]))
print(count_suits_recursive(["Mark I", "Mark I", "Mark III", "Mark IV"]))