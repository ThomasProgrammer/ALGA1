# Dokumentáció a kódról

## 1. Funkció áttekintés

A kód egy algoritmust valósít meg, amely ellenőrzi, hogy egy adott gráf bipartit-e. A **bipartit gráf** olyan gráf, amely csúcspontjai két különböző halmazra oszthatók úgy, hogy egyetlen él sem köt össze azonos halmazbeli csúcspontokat.

---

## 2. Az `is_bipartite` függvény működése

### Bemenet:
- `graph`: A gráf szomszédsági listával tárolva.
- `n`: A gráf csúcspontjainak száma.

### Lépések:
1. **Szín inicializálása**:  
   Egy `color` tömb jön létre, amely `-1`-re inicializálva jelzi, hogy a csúcspontok még nincsenek besatírozva.

2. **BFS segédfüggvény**:  
   - A gráfot Breadth-First Search (**BFS**) algoritmussal járja be.  
   - Egy adott kezdő csúcsponttól kiindulva próbálja két színnel besatírozni a csúcspontokat (`0` és `1`).  
   - Ha él mentén két azonos színű csúcspontot talál, a gráf **nem bipartit**.

3. **Gráf bejárása**:  
   - Minden csúcspontot ellenőriz.  
   - Ha egy komponens nincs még bejárva, meghívja rá a BFS függvényt.  
   - Ha valamelyik komponens nem bipartit, az algoritmus azonnal visszatér és `False`-t ad vissza.

### Kimenet:
- `True`: Ha a gráf bipartit.
- `False`: Ha a gráf nem bipartit.

---

## 3. A `main` függvény működése

### Bemenet feldolgozása:
- Az adatokat a szabványos bemenetről olvassa be (általában egy szövegfájlból vagy konzolról).  
- Az **első szám** a tesztesetek számát jelöli.  
- Minden teszteset sorban tartalmazza:
  - `n`: Csúcspontok száma.
  - `m`: Az élek száma.
  - A következő `m` sor páronként tartalmazza az élek csúcsteit.

### Gráf felépítése:
- A gráfot egy szomszédsági lista alapján hozza létre.

### Eredmények kiírása:
- Az `is_bipartite` függvény eredménye alapján eldönti, hogy:
  - **„gyanús hibák”** (nem bipartit gráf) vannak-e, vagy  
  - **nincs hiba** (bipartit gráf).  
- Minden tesztesethez egy-egy összefoglaló szöveget generál, amelyet a program végén kiír.

---

## 4. Kimenet

A kimenet formája:

- **Pozitív eset**:  
  ```text
    Scenario #1:
    No suspicious bugs found!
- **Negativ eset**:  
  ```text
    Scenario #12:
    Suspicious bugs found!