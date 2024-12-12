# Professor Hopper Kísérlete - Feladatleírás és Megoldás

## Feladat

Professor Hopper egy ritka bogárfaj szexuális viselkedését kutatja. Feltételezi, hogy a faj két különböző nemű bogárból áll, és hogy csak az ellentétes nemű bogarak lépnek kölcsönhatásba egymással. A kísérlet során az egyes bogarakat és kölcsönhatásaikat könnyen azonosítani lehetett, mivel számok voltak nyomtatva a hátukra.

Egy bogarak közötti kölcsönhatásokat tartalmazó lista alapján el kell dönteni, hogy a kísérlet alátámasztja-e a professzor feltételezését a két nemről és a kizárólag heteroszexuális viselkedésről, vagy tartalmaz-e olyan kölcsönhatásokat, amelyek ezt cáfolják.

### Bemenet

Az első sor a forgatókönyvek számát tartalmazza. Minden forgatókönyv egy sorral kezdődik, amely megadja a bogarak számát (legalább egy, legfeljebb 2000) és a kölcsönhatások számát (legfeljebb 1 000 000), egyetlen szóközzel elválasztva. A következő sorokban minden kölcsönhatás két különböző bogár számával van megadva, szintén szóközzel elválasztva. A bogarak számozása egytől kezdődik.

### Kimenet

Minden forgatókönyv esetén egy sort kell kiírni a következő formátumban:

```
Scenario #i:
```

ahol *i* az aktuális forgatókönyv sorszáma (1-től kezdve), majd egy új sor következik, amelyben az alábbi két üzenet egyike szerepel:

- `No suspicious bugs found!`, ha a kísérlet összhangban van a professzor feltételezésével.
- `Suspicious bugs found!`, ha a professzor feltételezése biztosan hibás.

---

## Megoldás Pythonban

```python
def is_bipartite(graph, n):
    color = [-1] * (n + 1)
    
    def bfs(start):
        queue = [start]
        color[start] = 0
        
        while queue:
            node = queue.pop(0)
            for neighbor in graph[node]:
                if color[neighbor] == -1:
                    color[neighbor] = 1 - color[node]
                    queue.append(neighbor)
                elif color[neighbor] == color[node]:
                    return False
        return True
    
    for i in range(1, n + 1):
        if color[i] == -1:
            if not bfs(i):
                return False
    return True

def main():
    import sys
    input = sys.stdin.read
    data = input().split()
    
    index = 0
    scenarios = int(data[index])
    index += 1
    results = []
    
    for scenario in range(1, scenarios + 1):
        n = int(data[index])
        m = int(data[index + 1])
        index += 2
        
        graph = [[] for _ in range(n + 1)]
        
        for _ in range(m):
            u = int(data[index])
            v = int(data[index + 1])
            index += 2
            graph[u].append(v)
            graph[v].append(u)
        
        if is_bipartite(graph, n):
            results.append(f"Scenario #{scenario}:\nNo suspicious bugs found!")
        else:
            results.append(f"Scenario #{scenario}:\nSuspicious bugs found!")
    
    print("\n".join(results))

if __name__ == "__main__":
    main()
