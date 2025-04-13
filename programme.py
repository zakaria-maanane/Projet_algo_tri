import time  
import tracemalloc  # Pour mesurer l'utilisation mémoire
import heapq  # Pour le tri par tas (utilise une file de priorité = tas binaire)
import random # Pour générer les chiffres aléatoires dont l'utilisateur va choisir le nombre 
import matplotlib.pyplot as plt
import json
import os

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

# Genération de nombres aléatoires dans un fichier texte
def generer_nombres_aleatoires(fichier, quantite, min_val=0, max_val=10000):
    """
    Génère un fichier contenant 'quantite' nombres aléatoires entre min_val et max_val.
    Chaque nombre est séparé par un espace.
    """
    with open(fichier, 'w') as f:
        nombres = [str(random.randint(min_val, max_val)) for _ in range(quantite)]
        f.write(" ".join(nombres))
    print(f"✅ {quantite} nombres ont été générés dans le fichier '{fichier}'.")

def sauvegarder_resultats(resultats, fichier="resultats_tris.json"):
    """Sauvegarde les résultats des tris dans un fichier JSON"""
    with open(fichier, 'w') as f:
        json.dump(resultats, f)

def charger_resultats(fichier="resultats_tris.json"):
    """Charge les résultats des tris depuis un fichier JSON"""
    if os.path.exists(fichier):
        with open(fichier, 'r') as f:
            return json.load(f)
    else:
        # Structure initiale si le fichier n'existe pas
        return {nom: {"tailles": [], "temps": []} for nom, _ in noms_tris}

# Fonction pour tracer le graphique avec tous les résultats et annotations
def tracer_graphique_complet(resultats):
    plt.figure(figsize=(14, 8))
    
    for nom in resultats:
        # Crée des paires (taille, temps) pour pouvoir les trier
        points = list(zip(resultats[nom]["tailles"], resultats[nom]["temps"]))
        # Trie les points par taille croissante
        points.sort(key=lambda x: x[0])
        
        # Extrait les tailles et temps triés
        tailles_triees = [p[0] for p in points]
        temps_tries = [p[1] for p in points]
        
        # Trace la courbe avec points
        plt.plot(tailles_triees, temps_tries, 'o-', label=nom)
        
        # Ajoute les annotations avec le nombre de chiffres triés pour chaque point
        for taille, temps in zip(tailles_triees, temps_tries):
            # Ajoute une petit décalage pour éviter que les annotations se superposent
            plt.annotate(f"{taille}", 
                        (taille, temps),
                        textcoords="offset points", 
                        xytext=(0, 10),  # Décalage par rapport au point
                        ha='center',     # Alignement horizontal centré
                        fontsize=8,      # Taille de police plus petite
                        bbox=dict(boxstyle="round,pad=0.3", fc="white", alpha=0.7))
    
    plt.xlabel("Nombre de données")
    plt.ylabel("Temps d'exécution (s)")
    plt.title("Temps d'exécution des algorithmes de tri selon la taille des données")
    plt.legend()
    plt.grid(True)
    plt.yscale('log')  # Échelle logarithmique
    plt.xscale('log')  # Échelle logarithmique aussi pour x
    plt.tight_layout()
    plt.show()

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

    # Demander si on doit réinitialiser les résultats
    reset = input("Voulez-vous réinitialiser les résultats précédents ? (o/n): ").lower() == 'o'
    
    if reset:
        resultats = {nom: {"tailles": [], "temps": []} for nom, _ in noms_tris}
    else:
        resultats = charger_resultats()
    
    # Génération du fichier de nombres
    fichier = "nombres.txt"
    nb_nombres = int(input("Combien de nombres veux-tu générer dans le fichier ? "))
    generer_nombres_aleatoires(fichier, nb_nombres)

    # Lecture des données depuis le fichier texte
    data = charger_nombres(fichier)

    # Liste pour stocker les résultats (nom, temps, tableau trié)
    resultats_tri = []

    print("\nRésultats pour chaque algorithme :\n")

    for nom, fonction in noms_tris:
        print(f"Exécution de {nom}...")
        nom_tri, temps, memoire_ko, resultat_tri = mesurer_temps_et_tri(nom, fonction, data)
        resultats_tri.append((nom_tri, temps, memoire_ko, resultat_tri))  # On garde les données sans les afficher
        
        # Ajouter les résultats aux données existantes pour le graphique
        resultats[nom]["tailles"].append(nb_nombres)
        resultats[nom]["temps"].append(temps)
        
        print(f"{nom} → {temps:.6f} sec | {memoire_ko} Ko utilisés")

    # Trie les algorithmes par temps (plus rapide en premier)
    resultats_tri.sort(key=lambda x: x[1])

    # Affiche le classement final par rapidité
    print("\n🏁 Classement final des algorithmes par rapidité :")
    for i, (nom, temps, memoire_ko, _) in enumerate(resultats_tri, 1):
        print(f"{i}. {nom} → {temps:.6f} sec | {memoire_ko} Ko utilisés")

    # Trie les résultats par mémoire utilisée (du plus petit au plus grand)
    resultats_par_memoire = sorted(resultats_tri, key=lambda x: x[2])  # x[2] = mémoire en Ko

    # Affiche le classement final par mémoire
    print("\n💾 Classement final des algorithmes par mémoire utilisée :")
    for i, (nom, temps, memoire_ko, _) in enumerate(resultats_par_memoire, 1):
        print(f"{i}. {nom} → {memoire_ko} Ko | {temps:.6f} sec")
    
    # Sauvegarder tous les résultats
    sauvegarder_resultats(resultats)
    
    # Tracer le graphique avec tous les résultats accumulés
    tracer_graphique_complet(resultats)