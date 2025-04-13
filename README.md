# 🔢 Comparative Sorting Algorithms in Python

Ce projet Python met en œuvre **plusieurs algorithmes de tri classiques** pour trier une liste de nombres stockée dans un fichier `.txt`.  
Il compare les performances **en temps d'exécution** et **en complexité spatiale** de chaque algorithme, et établit un **classement final**.

---

## 📂 Structure du projet

-programm.py contien le code python qui déploit les tri sur les chiffres du fichier txt 

-nombre.txt contien les chiffres choisit 


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
SORTIE GRAPHIQUE 
![image](https://github.com/user-attachments/assets/ce6cafc7-d26c-43be-a6ea-7df2a51fc0a7)

[Capture d'écran 2025-04-11 131206](https://github.com/user-attachments/assets/fe7cd9b0-07ef-4b22-8706-83fc2ed1e870)

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
!

