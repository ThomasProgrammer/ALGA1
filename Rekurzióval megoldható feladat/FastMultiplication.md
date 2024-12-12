# Gyors Szorzás

## Probléma Leírása

A feladat adott számok párosainak szorzása.

### Bemenet
- `n`: A szorzások száma (<= 1000)
- `l1 l2`: Szorzandó számok párosai (minden szám legfeljebb 10000 tizedesjegyű lehet)

### Kimenet
- A szorzások eredményei.

### Példa
#### Bemenet
```
3
123 456
789 101112
131415 161718
```

#### Kimenet
```
56088
79701048
21222327370
```

## Megoldás

A probléma megoldása:

```python
n = int(input())
eredmenyek = []

for _ in range(n):
    l1, l2 = map(int, input().split())
    eredmenyek.append(l1 * l2)

for eredmeny in eredmenyek:
    print(eredmeny)
```