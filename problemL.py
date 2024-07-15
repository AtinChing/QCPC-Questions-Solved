# Problem L. Second Best Gain, complete
# Categories: greedy
l = int(input())
arr = input().split(' ')
for i in range(len(arr)):
    arr[i] = int(arr[i])
arr.sort()
arr.reverse()
m = arr[1]
print((l-2)*m)