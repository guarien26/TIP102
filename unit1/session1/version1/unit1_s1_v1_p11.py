def tiggerfy(s):
    tiger = ['t','i','g','e','r','T','I','G','E','R']
    res = []
    for i in s:
        if i in tiger:
            continue
        else:
            res.append(i)

    print("".join(res))





s = "suspicerous"
tiggerfy(s)

s = "Trigger"
tiggerfy(s)

s = "Hunny"
tiggerfy(s)