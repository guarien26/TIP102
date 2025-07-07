from collections import deque

def process_performance_requests(requests):
    queue = deque(requests)
    result = []

    # While queue is not empty
    while queue:
        # Step 1: Find max priority in current queue
        max_priority = max([priority for priority, _ in queue])
        
        # Step 2: Loop through queue and extract highest priority
        size = len(queue)
        for _ in range(size):
            priority, name = queue.popleft()
            if priority == max_priority:
                result.append(name)  # process this one now
            else:
                queue.append((priority, name))  # put it back for next round

    return result


print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))