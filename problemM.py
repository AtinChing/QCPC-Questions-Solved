# Problem M. Abdo With Array, incomplete
# Categories are tough to categorise for this one, I think this is meant to be an easy dynamic programming question
for test in range(int(input())):
    inp1 = input().split(' ')
    n = int(inp1[0])
    x = int(inp1[1])
    arr = input().split(' ')
    for i in range(len(arr)):
        arr[i] = int(arr[i])
    
# Ideas:
"""
    create an array of length of the input array-1, where each element is sum of current and next element.
    create a hashmap, sum:index of sum in arr
    order by size of sum
    from highest sum to lowest: look up that sum, look for biggest number, minus by (X-sum), minus accordingly, repeat until largest sum <= X 
    only problem is this isnt a dynamic programming implementation, seems like a greedy implementation
"""