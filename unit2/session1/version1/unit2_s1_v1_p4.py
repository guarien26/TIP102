def identify_conflicts(venue1_schedule, venue2_schedule):
    conflicts = {}

    for ven1 in venue1_schedule:
        if ven1 in venue2_schedule and venue1_schedule[ven1] == venue2_schedule[ven1]:
            conflicts.update({ven1:venue1_schedule[ven1]})
    return conflicts


venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule))