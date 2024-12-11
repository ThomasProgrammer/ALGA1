def josephus_problem(n):
    children = list(range(1, n + 1))
    removal_order = []
    index = 0
    
    while children:
        index = (index + 1) % len(children)
        removal_order.append(children.pop(index))
    
    return removal_order

n = int(input())
result = josephus_problem(n)
print(" ".join(map(str, result)))
