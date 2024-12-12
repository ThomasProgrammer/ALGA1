# Dokumentáció a kódról

Ez a kód egy egyszerű implementációja a Josephus-problémának. A Josephus-probléma egy klasszikus kombinatorikai probléma, amelyben N ember körben ül, és minden második embert eltávolítunk addig, amíg csak egy marad. A kód az eltávolítás sorrendjét adja vissza.

## Részletes magyarázat a kódról

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

### Függvény neve: `josephus_problem`

Feladata, hogy egy adott `n` érték mellett kiszámítsa a Josephus-probléma során az eltávolítás sorrendjét.

#### Bemeneti paraméter:

- `n`: Egy pozitív egész szám, amely az emberek (gyermekek) számát jelöli.

#### Változók a függvényben:

- `children`: Egy lista, amely tartalmazza az 1-től n-ig terjedő egész számokat. Ezek az emberek az eltávolítás kezdő állapotát jelölik.
- `removal_order`: Egy üres lista, amelybe az eltávolított emberek kerülnek, az eltávolítás sorrendjében.
- `index`: Az aktuális index, amely azt mutatja, hogy melyik embert kell eltávolítani a következő lépésben.

## Működés

- Az `index` kezdetben 0, azaz az első emberre mutat.
- Egy `while` ciklus fut addig, amíg a `children` lista nem üres.
- A ciklus minden iterációjában:
    - Az `index` értékét 1-gyel növeli.
    - Az aktuális indexű elemet eltávolítja a `children` listából.
    - Az eltávolított elemet hozzáadja a `removal_order` listához.
    - Az `index` értékét modulo operátorral (és a lista aktuális hosszával) frissíti, hogy az `index` ne léphessen túl a lista határain.

## Visszatérési érték

A függvény visszaadja a `removal_order` listát, amely az eltávolított emberek sorrendjét tartalmazza.

## Bemenet és kimenet

- A felhasználó megad egy pozitív egész számot (`n`), amelyet az `input()` függvény olvas be.
- A főprogram meghívja a `josephus_problem` függvényt, majd a visszatérési értéket egy szóközökkel elválasztott sztringgé alakítja, amelyet a kimenetre ír ki.

## Példa futtatás

**Bemenet:**

```
5
```

**Kimenet:**

```
2 4 1 5 3
```

**Magyarázat:**

- Az 5 ember körben ül: `[1, 2, 3, 4, 5]`.
- Első eltávolítandó a 2-es.
- Ezután marad: `[1, 3, 4, 5]`.
- Következő eltávolítandó a 4-es.
- Ez ismétlődik, amíg mindenki el nem tűnik.
