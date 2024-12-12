n = int(input())
results = []

for _ in range(n):
    l1, l2 = map(int, input().split())
    results.append(l1 * l2)

for result in results:
    print(result)