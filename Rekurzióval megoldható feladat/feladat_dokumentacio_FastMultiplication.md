# FastMultiplication kód dokumentáció

## A program funkciója

Ez a program képes több két számból álló bemenetet fogadni, majd minden egyes pár szám szorzatát kiszámítani és megjeleníteni.

## A kód működése lépésről lépésre

### Adatbemenet a felhasználótól

```python
n = int(input())
```

A program első lépésben bekéri a felhasználótól, hogy hány számpárt szeretne feldolgozni. Ez az érték az `n` változóban tárolódik.

### Lista inicializálása

```python
results = []
```

Egy üres listát hozunk létre, amely a kész szorzatokat fogja tárolni.

### Adatfeldolgozás ciklussal

```python
for _ in range(n):
    l1, l2 = map(int, input().split())
    results.append(l1 * l2)
```

Egy `for` ciklust használunk az ismétléshez, amely pontosan `n` alkalommal fut le. A felhasználó minden iterációban két számot ad meg, amelyeket egy szóköz választ el egymástól. Ezeket a számokat az `l1` és `l2` változókban tároljuk. A két szám szorzatát kiszámítjuk, és az eredményt hozzáadjuk a `results` listához.

### Eredmények kiírása

```python
for result in results:
    print(result)
```

Egy második ciklussal végigmegyünk a `results` listán. Minden egyes elemét (szorzatát) kiírjuk a konzolra.

## Példa futtatásra

### Bemenet:

```
3
2 3
4 5
6 7
```

### Működés:

- `n = 3`, tehát 3 számpárt dolgozunk fel.
- Az első számpár: 2 és 3 → szorzat: 6
- A második számpár: 4 és 5 → szorzat: 20
- A harmadik számpár: 6 és 7 → szorzat: 42

### Kimenet:

```
6
20
42
```