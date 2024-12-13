# Kód dokumentációja

## 1. BipartiteGraph osztály

Ez az osztály reprezentálja a kétoldalú gráfot és tartalmazza az ehhez szükséges adatstruktúrákat és algoritmusokat.

### `__init__(self, max_v1, max_v2)`

Az osztály inicializálása.
- `max_v1` és `max_v2` a két oldalon lévő csúcsok maximális száma.
- Az osztály két listát tárol:
  - `self.L`: A gráf szomszédsági listája, amely minden csúcsnak tartalmazza az őt elérő másik oldalon lévő csúcsokat.
  - `self.visited`: Ez a lista követi, hogy mely csúcsokat látogattuk meg a mélységi keresés (DFS) során.
  - `self.match`: Ez a lista tartalmazza, hogy melyik csúcs van párosítva egy másikkal. Ha egy csúcs nincs párosítva, akkor értéke -1.
  - `self.V1` és `self.V2`: A két oldal csúcsainak száma, amit az inicializáláskor megadunk.

### `clear(self, v1, v2)`

A gráfot törli és újra inicializálja a megadott méretekkel. Minden oldalon lévő csúcsok szomszédsági listája kiürül.

### `add_edge(self, v1, v2)`

Egy él hozzáadása a gráfhoz. Az él a `v1` csúcsból a `v2` csúcsba vezet. Az él irányított, tehát csak egy irányban van kapcsolat.

### `dfs(self, u)`

A mélységi keresés (DFS) algoritmus, amelyet a párosítás megtalálására használunk. A függvény megpróbálja megtalálni, hogy a `u` csúcs párosítható-e egy másik csúccsal az ellentétes oldalon. Ha sikerül, akkor `True`-t ad vissza, különben `False`-t.

### `maximum_matching(self)`

A maximális párosítás kiszámítása. A `dfs` függvényt hívja meg minden csúcsra az egyik oldalon (`V1`), és ha a párosítás sikeres, akkor növeli az eredményt. A párosítást a `self.match` listában tartja nyilván.

## 2. main függvény

Ez a függvény olvassa be a bemeneti adatokat, használja a `BipartiteGraph` osztályt a maximális párosítás kiszámítására, és kiírja az eredményt.

### `input = sys.stdin.read`

Az összes bemeneti adatot egyszerre olvassa be. Ez hatékonyabb, mint soronkénti beolvasás, mivel az adatokat tömbbé alakítja a `split` metódussal.

### `T = int(data[index])`

Az első adat a tesztesetek számát jelöli (`T`).

### `G = BipartiteGraph(120, 120)`

Létrehozunk egy `BipartiteGraph` objektumot 120 csúccsal mindkét oldalon. A 120 érték a maximális csúcsszámot jelenti a gráf mindkét oldalán.

### `eredmenyek = []`

Ez a lista tárolja a minden egyes teszteset eredményét (a maximális párosítások számát).

### A bemeneti adat feldolgozása és gráfépítés

A for ciklusokban beolvassuk a tesztesetek adatokat. Minden tesztesetben először töröljük a gráfot a `G.clear(120, 120)` hívással, majd minden élhez hozzáadjuk azt a két csúcsot, amely között kapcsolat van (`G.add_edge(r, c)`).

### Maximális párosítás számítása

Minden teszteset után meghívjuk a `G.maximum_matching()` függvényt, amely kiszámítja a maximális párosítást a gráfban. Az eredményt hozzáadjuk az `eredmenyek` listához.

### Eredmény kiírása

Az összes teszteset eredményét kiírjuk a végén.

## 3. Futtatás

A program akkor fut, ha közvetlenül indítjuk, vagyis a `if __name__ == "__main__":` blokkban található `main()` függvény meghívása történik.
