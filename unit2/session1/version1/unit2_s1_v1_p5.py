def best_set(votes):
    vote_count = {}
    max_count = 0
    popular = ""

    for vote in votes:
        if votes.get(vote) not in vote_count:
            vote_count[votes.get(vote)] = 1
        else:
            vote_count[votes.get(vote)] += 1
        if vote_count[votes.get(vote)] > max_count:
            max_count = vote_count[votes.get(vote)]
            popular = votes.get(vote)
 
    return popular

votes1 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA",
    1239: "SZA"
}

votes2 = {
    1234: "SZA", 
    1235: "Yo-Yo Ma",
    1236: "Ethel Cain",
    1237: "Ethel Cain",
    1238: "SZA"
}

print(best_set(votes1))
print(best_set(votes2))