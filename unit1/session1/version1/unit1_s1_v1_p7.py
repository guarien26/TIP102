def count_less_than(race_times, threshold):
    res = 0
    for i in race_times:
        if i < threshold:
            res+=1		
    
    print(res)





race_times = [1, 2, 3, 4, 5, 6]
threshold = 4
count_less_than(race_times, threshold)

race_times = []
threshold = 4
count_less_than(race_times, threshold)