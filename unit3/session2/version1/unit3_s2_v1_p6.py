def next_greater_event(schedule1, schedule2):
    res = []
    for i in range(len(schedule1)):
        flag = False
        if schedule1[i] in schedule2:
            try:
                for j in schedule2[schedule2.index(schedule1[i]) + 1:]:
                    if j > schedule1[i]:
                        res.append(j)
                        flag = True
                        break
                if not flag:
                    res.append(-1)
            except:
                res.append(-1)
    return res

print(next_greater_event([4, 1, 2], [1, 3, 4, 2]))
print(next_greater_event([2, 4], [1, 2, 3, 4]))   
