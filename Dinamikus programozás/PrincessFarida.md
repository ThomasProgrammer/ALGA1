## Feladat leírása

Egyszer volt, hol nem volt, volt egyszer egy aranyos hercegnő, Farida, aki egy kastélyban élt az apjával, anyjával és nagybátyjával. A kastélyhoz vezető úton sok szörny élt. Mindegyiknek volt néhány aranyérméje. Bár szörnyek, nem bántanak téged. Ehelyett aranyérméket adnak neked, de csak akkor, ha nem vettél érméket a közvetlenül előttük lévő szörnytől. Ahhoz, hogy feleségül vehesd Farida hercegnőt, át kell menned az összes szörnyön, és a lehető legtöbb érmét kell összegyűjtened. Az egyes szörnyeknél lévő aranyérmék számát figyelembe véve számítsd ki a maximális érmék számát, amit összegyűjthetsz a kastélyhoz vezető úton.

## Bemenet

- Az első sor a tesztesetek számát tartalmazza.
- Minden teszteset egy `N` számmal kezdődik, a szörnyek számával, ahol `0 <= N <= 10^4`.
- A következő sorban `N` szám lesz, amelyek az egyes szörnyeknél lévő érmék számát jelölik, ahol `0 <= érmék száma szörnyenként <= 10^9`. A szörnyek a kastélyhoz vezető úton való találkozás sorrendjében vannak leírva.

## Kimenet

Minden tesztesethez nyomtasd ki `Case C: X` idézőjelek nélkül. `C` az eset száma, 1-től kezdve. `X` a maximális érmék száma, amit összegyűjthetsz.

## Példa

### Bemenet:
```
2
5
1 2 3 4 5
1
10
```

### Kimenet:
```
Case 1: 9
Case 2: 10
```

## Python kód

```python
def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    t = int(data[0])
    index = 1
    
    for i in range(t):
        n = int(data[index])
        index += 1
        
        if n == 0:
            print(f"Case {i + 1}: 0")
            continue
        
        arr = list(map(int, data[index:index + n]))
        index += n
        
        if n == 1:
            print(f"Case {i + 1}: {arr[0]}")
            continue
        
        dp = [0] * n
        dp[0] = arr[0]
        dp[1] = max(arr[0], arr[1])
        
        for j in range(2, n):
            dp[j] = max(dp[j - 1], dp[j - 2] + arr[j])
        
        print(f"Case {i + 1}: {dp[n - 1]}")

if __name__ == "__main__": 
    main()
```