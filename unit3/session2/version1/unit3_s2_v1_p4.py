def booth_navigation(clues):
    result = []

    for clue in clues:
        if clue == "back":
            if not result:
                continue
            result.pop()
        else:
            result.append(clue)

    return result




clues = [1, 2, "back", 3, 4]
print(booth_navigation(clues)) 

clues = [5, 3, 2, "back", "back", 7]
print(booth_navigation(clues)) 

clues = [1, "back", 2, "back", "back", 3]
print(booth_navigation(clues)) 