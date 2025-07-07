from collections import deque

"""
U: go through the list and append accordingly, if we reach cancel, we pop it from the list
   if we reach a reschedule, we readd the most recently canceled performance

P: 
Inputs: changes (list)
Output: return (list) of schedules
Constraints: strictly typed commands
Edge: empty

I:

"""


def manage_stage_changes(changes):
    schedules = []
    canceled_schedules = []

    for change in changes:
        if (change == "Cancel" or change == "Reschedule") and len(schedules) == 0 :
            continue
        elif change == "Cancel":
            canceled_schedules.append(schedules.pop())
        elif change == "Reschedule":
            schedules.append(canceled_schedules.pop())
        else:
            schedules.append(change[-1])
    
    return schedules






print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"])) 