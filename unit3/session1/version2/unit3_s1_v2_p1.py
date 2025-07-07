from collections import deque


def time_required_to_stream(movies, k):
    """
    Understanding: [5,1,1,1]

    Inputs: movies (list)[user wants to stream 2 movies,user wants to stream 3 movies,]
    Output: returns (int) time taken for user at position k to finish streaming all movies
    """

    time_required = 0
    dq = deque(movies)
    count = 0

    # [2,3,2] k = 2
    while movies[k] != 0:
        if count == len(movies):
            count = 0

        movies[count] -= 1 #list= [1,3,2] [1,2,2] [1,2,1] [0,2,1] [0,1,1]

        if movies[count] == 0:
            first = dq.popleft() # queue= [3,2,2] [2,2,3] [2,3,2]  [2,3] 
            dq.append(first)
        
        count +=1
        time_required+=1
    
    return time_required
















print(time_required_to_stream([2, 3, 2], 2)) 
print(time_required_to_stream([5, 1, 1, 1], 0)) 