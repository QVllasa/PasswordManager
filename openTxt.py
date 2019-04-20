accounts = {}
with open('accountLists.txt', 'r') as f:
    d = []
    for i in f:
        if '=' in i:
            d = i.strip().split(' ')
            accounts[d[0]] = []
        elif '=' not in i and not len(i.strip()) == 0:
            i = i.strip()
            accounts[d[0]].append(i.strip())
        else:
            continue

for key, value in accounts.items():
    print(key, value)
