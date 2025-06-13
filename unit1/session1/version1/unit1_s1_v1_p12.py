def locate_thistles(items):
    res = []
    for i in range(len(items)):
        if items[i] == "thistle":
            res.append(i)

    print(res)

items = ["thistle", "stick", "carrot", "thistle", "eeyore's tail"]
locate_thistles(items)

items = ["book", "bouncy ball", "leaf", "red balloon"]
locate_thistles(items)