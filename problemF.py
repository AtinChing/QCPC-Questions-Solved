# Problem F. Range Majority Query
# array, and sliding window?, and hashmap
# i have a prefix sum-like solution in mind, im sure it will work. its just that storing 10^5 dicts could mess with or hit memory limits, so i dont know if my proposed solution would be valid
# I will implement this solution tomorrow
l = int(input())
arr = input().split(' ')
arrdict = []
data = {}
for i in range(len(arr)):
    arr[i] = int(arr[i])
    data[arr[i]] = data.get(arr[i], 0) + 1
    arrdict.append(data.copy())
queries = int(input())
for q in range(queries):
    query = input().split(' ')
    l = int(query[0])
    r = int(query[1])
    dictmore = arrdict[r]
    if l == 0:
        dictminus = {}
    else: dictminus = arrdict[l-1]
    for k,v in dictminus.items():
        dictmore[k] -= v
        if dictmore[k] == 0:
            del dictmore[k]
    amount = r-l + 1
    dom = False
    for k,v in dictmore.items():
        if v > (amount/2):
            print('Yes')
            print(k)
            dom = True
            break
    if not dom:
        print('No')