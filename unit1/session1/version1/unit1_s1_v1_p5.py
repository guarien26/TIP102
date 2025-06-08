def sum_honey(hunny_jars):
    if len(hunny_jars) == 0:
        print(0)
    else: 
        res = 0
        for i in hunny_jars:
            res+=i
        print(res)
	

hunny_jars = [2, 3, 4, 5]
sum_honey(hunny_jars)

hunny_jars = []
sum_honey(hunny_jars)