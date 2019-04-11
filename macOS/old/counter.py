
list1 = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r']
b = len(list1)
print (b)
count = 0
c = 0
print('init count:'+str(count))
while count <= 100:
    count += 100/b
    c += 1
    print(str(c)+'   '+str(count))
