# 🔢 Comparative Sorting Algorithms in Python

Ce projet Python met en œuvre **plusieurs algorithmes de tri classiques** pour trier une liste de nombres stockée dans un fichier `.txt`.  
Il compare les performances **en temps d'exécution** et **en complexité spatiale** de chaque algorithme, et établit un **classement final**.

---

## 📂 Structure du projet

- `data.txt` : fichier contenant la liste de nombres à trier (un seul nombre par ligne, ou séparés par des virgules/espaces).
- `main.py` : script principal contenant l'exécution des algorithmes, les mesures, et le classement.
- `sorting_algorithms.py` : implémentation des algorithmes de tri.
- `results.txt` *(optionnel)* : export des résultats comparatifs.

---

## 🚀 Algorithmes de tri implémentés

- 🔹 Tri par sélection *(Selection Sort)*
- 🔸 Tri à bulles *(Bubble Sort)*
- 🔹 Tri par insertion *(Insertion Sort)*
- 🔸 Tri fusion *(Merge Sort)*
- 🔹 Tri rapide *(Quick Sort)*
- 🔸 Tri par tas *(Heap Sort)*
- 🔹 Tri à peigne *(Comb Sort)*

---

## 📊 Objectif

- Charger une liste de nombres à partir d’un fichier texte.
- Appliquer chaque algorithme de tri à la même liste.
- **Mesurer :**
  - Le **temps d'exécution** de chaque tri
  - La **mémoire utilisée** pendant l’exécution
- Générer :
  - Un **classement des tris les plus rapides**
  - Un **classement des tris les plus économes en espace**

---

## 📈 Exemple de sortie (console)

```bash
Résultats - Temps d'exécution (en secondes) :
1. Quick Sort        -> 0.00012 s
2. Merge Sort        -> 0.00015 s
3. Heap Sort         -> 0.00018 s
...

Résultats - Complexité spatiale estimée :
1. Insertion Sort    -> 1.01x
2. Selection Sort    -> 1.01x
3. Comb Sort         -> 1.02x
...

Tri le plus rapide : Quick Sort
Tri le plus économique en mémoire : Insertion Sort
