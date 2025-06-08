def split_haycorns(quantity):
    lst = []
    for i in range(quantity+1):
        if quantity % (i+1) == 0:
            lst.append(i+1)

    print(lst)


quantity = 6
split_haycorns(quantity)

quantity = 1
split_haycorns(quantity)