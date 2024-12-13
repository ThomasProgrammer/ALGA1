# Feladat leírása

Jones-nak el kell érnie a kincset, de ehhez át kell haladnia a **"Halál Termén"**. Ennek a szobának a padlója egy 120 egység hosszú oldalú négyzet, amely 1x1-es csempékből van kirakva, és ezek a csempék rácsba rendezve helyezkednek el. Azonban a rács egyes helyein csempék hiányoznak. Amint kinyílik a szoba ajtaja, mérgező gáz kezd el áramlani a hiányzó csempék helyeiről. Az egyetlen menekvés a gáztól, ha teljesen befedjük ezeket a helyeket deszkákkal, amelyek kívülről kerülnek a szobába. Minden egyes deszka mérete 120x1, és csak a padló oldalaihoz párhuzamosan helyezhetők el. 

Jones a következőt szeretné: minimalizálni a károkat az egészségére, hogy elég ereje maradjon a kincs megszerzésére. Rájön, hogy ehhez a legkevesebb deszkát kell felhasználni. Ő is rájön, hogy akkor is sikeresen meg tudja blokkolni a mérgező gázt, ha a deszkák átfednek egymással. Kérlek, segíts Jones-nak ezen feladat elvégzésében!

## Bemenet
- Az első sorban egy pozitív egész szám `t <= 20` található, amely a szobák számát jelöli.
- A következő `t` sor a szobák leírásait tartalmazza, egymás után.

### Szoba leírás:
- A szoba leírása egy pozitív egész számmal kezdődik, amely `n (n <= 10010)`, a hiányzó csempék számát jelöli.
- Ezután `n` sor következik, mindegyikben két egész szám `x` és `y` (0 <= x, y < 120), amelyek a hiányzó csempék koordinátáit jelzik.

## Kimenet
A programnak `t` sorral kell végeznie, mindegyik sorban az `mk` számot kell kiírni, amely a szoba `k`-hoz szükséges minimális deszkák számát jelöli.

---

## Megoldásom Pythonban:

```python
import sys

class BipartiteGraph:
    def __init__(self, max_v1, max_v2):
        self.L = [[] for _ in range(max_v1)]
        self.visited = [False] * max_v2
        self.match = [-1] * max_v2
        self.V1 = max_v1
        self.V2 = max_v2

    def clear(self, v1, v2):
        self.V1 = v1
        self.V2 = v2
        for i in range(v1):
            self.L[i].clear()

    def add_edge(self, v1, v2):
        self.L[v1].append(v2)

    def dfs(self, u):
        for v in self.L[u]:
            if not self.visited[v]:
                self.visited[v] = True
                if self.match[v] == -1 or self.dfs(self.match[v]):
                    self.match[v] = u
                    return True
        return False

    def maximum_matching(self):
        ans = 0
        self.match = [-1] * self.V2
        for i in range(self.V1):
            self.visited = [False] * self.V2
            if self.dfs(i):
                ans += 1
        return ans


def main():
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    T = int(data[index])
    index += 1
    
    G = BipartiteGraph(120, 120)
    
    eredmenyek = []
    for _ in range(T):
        n = int(data[index])
        index += 1
        
        G.clear(120, 120)
        
        for _ in range(n):
            r = int(data[index])
            c = int(data[index + 1])
            index += 2
            G.add_edge(r, c)
        
        eredmenyek.append(G.maximum_matching())
    
    for result in eredmenyek:
        print(result)

if __name__ == "__main__":
    main()
