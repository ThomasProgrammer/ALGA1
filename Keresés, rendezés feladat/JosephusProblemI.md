# Josephus Probléma
## A Feladat Leírása

A klasszikus Josephus probléma egy ismert algoritmus feladat, amelyben n személy áll körben, számozva 1-től n-ig. A folyamat során minden második személyt eltávolítanak a körből, amíg egyetlen személy nem marad.

## Specifikáció

### Bemenet
- `n`: egyetlen egész szám, a kezdeti körben álló személyek száma (1 ≤ n ≤ 2 × 10⁵)

### Kimenet
- Az eltávolított személyek sorszámai a kivétel sorrendjében (n darab egész szám)

## Példa
```
Bemenet: n = 7
Kimenet: 2 4 6 1 5 3 7
```

## Megoldás

Az alábbi Python kód megvalósítja a Josephus probléma megoldását:

```python
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
```