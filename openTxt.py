
accounts = {}
a = 0
s = []
with open('accountLists.txt', 'r+') as f:

    for i in f:
        for j in f:
            if i:
                if '=' in i and '=' in j:
                    print (i, j)
                    continue











