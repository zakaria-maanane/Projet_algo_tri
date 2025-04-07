import time  
import tracemalloc  # Pour mesurer l'utilisation mémoire
import heapq  # Pour le tri par tas (utilise une file de priorité = tas binaire)

# -------------------------
# Fonction : Tri par sélection
# -------------------------
def tri_selection(arr):
    arr = arr.copy()  # On copie la liste pour ne pas modifier l'originale
    for i in range(len(arr)):
        min_idx = i  # On suppose que l'élément à l'index i est le plus petit
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:  # On cherche un plus petit élément
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]  # On échange
    return arr

# -------------------------
# Fonction : Tri à bulles
# -------------------------
def tri_bulles(arr):
    arr = arr.copy()
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):  # Parcourt les éléments non triés
            if arr[j] > arr[j + 1]:  # Si l'élément suivant est plus petit, on échange
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

# -------------------------
# Fonction : Tri par insertion
# -------------------------
def tri_insertion(arr):
    arr = arr.copy()
    for i in range(1, len(arr)):
        key = arr[i]  # Élément à insérer
        j = i - 1
        while j >= 0 and key < arr[j]:  # Décale les éléments supérieurs
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key  # Place l'élément à la bonne position
    return arr

# -------------------------
# Fonction : Tri fusion
# -------------------------
def tri_fusion(arr):
    if len(arr) <= 1:  # Cas de base : 1 ou 0 élément = déjà trié
        return arr
    mid = len(arr) // 2  # Milieu du tableau
    left = tri_fusion(arr[:mid])  # Tri récursif de la moitié gauche
    right = tri_fusion(arr[mid:])  # Tri récursif de la moitié droite
    return fusion(left, right)  # Fusionne les deux moitiés triées

# Fonction auxiliaire pour fusionner deux listes triées
def fusion(left, right):
    result = []  # Résultat fusionné
    i = j = 0  # Indices de parcours
    while i < len(left) and j < len(right):  # Tant qu'on a des éléments des deux côtés
        if left[i] < right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]  # Ajoute les restes de la liste gauche (s'il en reste)
    result += right[j:]  # Ajoute les restes de la liste droite
    return result

# -------------------------
# Fonction : Tri rapide (quicksort)
# -------------------------
def tri_rapide(arr):
    if len(arr) <= 1:  # Cas de base
        return arr
    pivot = arr[0]  # Pivot = premier élément
    less = [x for x in arr[1:] if x <= pivot]  # Éléments plus petits ou égaux
    greater = [x for x in arr[1:] if x > pivot]  # Éléments plus grands
    return tri_rapide(less) + [pivot] + tri_rapide(greater)  # Tri récursif + pivot au milieu

# -------------------------
# Fonction : Tri par tas
# -------------------------
def tri_tas(arr):
    arr = arr.copy()
    heapq.heapify(arr)  # Transforme la liste en un tas (min-heap)
    return [heapq.heappop(arr) for _ in range(len(arr))]  # Extrait les éléments triés

# -------------------------
# Fonction : Tri à peigne (Comb sort)
# -------------------------
def tri_peigne(arr):
    arr = arr.copy()
    gap = len(arr)  # Intervalle initial = taille du tableau
    shrink = 1.3  # Facteur de rétrécissement
    sorted = False

    while not sorted:
        gap = int(gap / shrink)  # On réduit l'écart
        if gap <= 1:
            gap = 1
            sorted = True  # Supposé trié

        i = 0
        while i + gap < len(arr):
            if arr[i] > arr[i + gap]:  # Si un élément est plus grand que celui à gap
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                sorted = False  # Pas encore trié
            i += 1
    return arr

# -------------------------
# Fonction : Chargement des nombres depuis un fichier texte
# -------------------------
def charger_nombres(fichier):
    with open(fichier, 'r') as f:
        contenu = f.read()  # Lit tout le contenu
    # Transforme le texte en liste de nombres (en séparant par espace ou retour à la ligne)
    nombres = list(map(int, contenu.replace('\n', ' ').split()))
    return nombres

# -------------------------
# Fonction : Exécute un tri, mesure le temps et retourne le résultat
# -------------------------
def mesurer_temps_et_tri(nom, fonction, tableau):
    tracemalloc.start()  # Démarre le suivi de mémoire

    debut = time.perf_counter()  # Démarre le chrono
    resultat = fonction(tableau)  # Trie les données
    fin = time.perf_counter()  # Arrête le chrono

    memoire_actuelle, memoire_max = tracemalloc.get_traced_memory()  # Mémoire utilisée
    tracemalloc.stop()  # Arrête le suivi

    duree = round(fin - debut, 6)  # Temps en secondes
    memoire_ko = round(memoire_max / 1024, 3)  # Convertit la mémoire en Ko

    return nom, duree, memoire_ko, resultat

# -------------------------
# Programme principal
# -------------------------
if __name__ == "__main__":
    # Liste des tris à comparer
    noms_tris = [
        ("Tri à bulles", tri_bulles),
        ("Tri par sélection", tri_selection),
        ("Tri par insertion", tri_insertion),
        ("Tri par fusion", tri_fusion),
        ("Tri rapide", tri_rapide),
        ("Tri par tas", tri_tas),
        ("Tri à peigne", tri_peigne),
    ]

    # Lecture des données depuis le fichier texte
    data = charger_nombres("nombres.txt")

    # Liste pour stocker les résultats (nom, temps, tableau trié)
    resultats = []

    print("\nRésultats pour chaque algorithme :\n")

    for nom, fonction in noms_tris:
        nom_tri, temps, memoire_ko, resultat = mesurer_temps_et_tri(nom, fonction, data)
        resultats.append((nom_tri, temps, memoire_ko, resultat))  # On garde les données sans les afficher


    # Trie les algorithmes par temps (plus rapide en premier)
    resultats.sort(key=lambda x: x[1])

    # Affiche le classement final
    print("\n🏁 Classement final des algorithmes par rapidité :")
    for i, (nom, temps, memoire_ko, _) in enumerate(resultats, 1):
        print(f"{i}. {nom} → {temps:.6f} sec | {memoire_ko} Ko utilisés")

    # Trie les résultats par mémoire utilisée (du plus petit au plus grand)
    resultats_par_memoire = sorted(resultats, key=lambda x: x[2])  # x[2] = mémoire en Ko

    print("\n💾 Classement final des algorithmes par mémoire utilisée :")
    for i, (nom, temps, memoire_ko, _) in enumerate(resultats_par_memoire, 1):
        print(f"{i}. {nom} → {memoire_ko} Ko | {temps:.6f} sec")
