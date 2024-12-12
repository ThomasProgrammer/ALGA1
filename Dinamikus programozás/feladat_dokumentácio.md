# Dinamikus programozási algoritmus

## Ha legalább 2 szörny van:

- **arr**: Ez egy lista, amely az aktuális tesztesetben szereplő szörnyek érméinek számát tartalmazza.
- **dp**: Ez egy dinamikus programozási tömb, amelyben `dp[j]` az `arr[0:j+1]` tartományból elérhető maximális érmeösszeget tárolja.

```python
dp[0] = arr[0]  # Ha csak az első szörny érméi elérhetők.
dp[1] = max(arr[0], arr[1])  # Az első két szörny közül az érmek maximális száma érhető el.
```

### Ciklus a dinamikus tömb feltöltéséhez:

```python
for j in range(2, n):  # Az aktuális szörnyek között iterál.
    dp[j] = max(dp[j - 1], dp[j - 2] + arr[j])
    # Ha kihagyod az aktuális szörnyet: dp[j - 1].
    # Ha elviszed az aktuális szörny érméit: Az aktuális szörny érméi (arr[j]) hozzáadódnak a két szörny előtti maximális összeghez (dp[j - 2]).
```

Az utolsó érték, `dp[n - 1]`, tartalmazza az adott teszteset maximális érméit.

## Kimenet

```python
print(f"Case {i + 1}: {dp[n - 1]}")  # Az aktuális teszteset maximális érméit írja ki az adott formátumban.
```

## Kód működése példán

### Bemenet:

```
2
3
2 1 4
5
1 2 9 4 5
```

### Kimenet:

```
Case 1: 6
Case 2: 12
```

### 1. teszteset:

- Szörnyek érméi: `[2, 1, 4]`.
- **dp kiszámítása**:
  ```python
  dp[0] = 2
  dp[1] = max(2, 1) = 2
  dp[2] = max(2, 2 + 4) = 6
  ```
- Maximális érme: `6`.

### 2. teszteset:

- Szörnyek érméi: `[1, 2, 9, 4, 5]`.
- **dp kiszámítása**:
  ```python
  dp[0] = 1
  dp[1] = max(1, 2) = 2
  dp[2] = max(2, 1 + 9) = 10
  dp[3] = max(10, 2 + 4) = 10
  dp[4] = max(10, 10 + 5) = 12
  ```
- Maximális érme: `12`.