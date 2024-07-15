# Problem F. Range Majority Query
# array, and sliding window?, and hashmap
# i have a prefix sum-like solution in mind, im sure it will work. its just that storing 10^5 dicts could mess with or hit memory limits, so i dont know if my proposed solution would be valid
# I will implement this solution tomorrow
l = int(input())
arr = input().split(' ')
for i in range(len(arr)):
    arr[i] = int(arr[i])
