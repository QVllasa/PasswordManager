
accounts = {}

with open('accountLists.txt', 'r+') as f:
    s = []

    for i in f:
        if '[' and '='in i:
            s = i.strip().split(' ')
        if ']' in i:
            l = i.strip()
            s.append(l)
        if not '[' in i:
            if not ']' in i:
                account = i.strip()
                print(account)






