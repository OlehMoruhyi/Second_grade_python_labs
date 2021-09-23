max_weight = int(input())
weight = list(map(int, input().split()))
weight.sort()
for i in range(len(weight)-1, -1, -1):
    if weight[i] > max_weight:
        weight.pop()
    else:
        break
backpack = [1] + [0] * max_weight
for i in weight[::-1]:
    for k in range(max_weight, i-1, -1):
        if backpack[k-i] == 1:
            backpack[k] = 1
for i in range(max_weight, -1, -1):
    if backpack[i]:
        print(i)
        break
