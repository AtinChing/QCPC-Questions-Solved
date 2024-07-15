# Problem N. No Adjacent Sum, Incomplete
# Categories: this could be math and simulation
# constraints is 10^18, so no way we can do O(n^2)
# Giving it a shot anyway
for test in range(int(input())):
    inp = input().split(' ')
    a = int(inp[0])
    b = int(inp[1])
    k = int(inp[2])
    count = 0

    for num in range(a, b+1):
        arr = [int(n) for n in str(num)]
    print(count)