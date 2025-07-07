def merge_schedules(schedule1, schedule2):
    result = []

    if len(schedule1) > len(schedule2):
        for i in range(len(schedule2)):
            result.append(schedule1[i])
            result.append(schedule2[i])
        result.extend(schedule1[len(schedule2)::])

    elif len(schedule2) > len(schedule1):
        for i in range(len(schedule1)):
            result.append(schedule1[i])
            result.append(schedule2[i])
        result.extend(schedule2[len(schedule1)::])
    else:
        for i in range(len(schedule1)):
            result.append(schedule1[i])
            result.append(schedule2[i])

    return "".join(result)


# runtime: O(n+m)


print(merge_schedules("abc", "pqr")) 
print(merge_schedules("ab", "pqrs")) 
print(merge_schedules("abcd", "pq"))