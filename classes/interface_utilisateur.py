# Import pour histogramme :
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg



class InterfaceUtilisateur:
    """
    indices_categorie_produit est sous cette forme :
    indice_catégorie_produit = {'france': {'high_tech': [1, 2, 3], 'fruit': [4, 5, 6]}}
    boucle for pour acéder à tout:
    for values in indice_catégorie_produit.values():
        for keys in indice_catégorie_produit.keys():

    """
    def __init__(self, indices_produits, indices_categorie_produit):
        self._indices_produits = indices_produits
        self._indices_categorie_produit = indices_categorie_produit


    def plot_histogramme(self):

        def tracer_histogramme(index_selectionne, categorie_selectionnee):
            plt.clf()  # Effacer le tracé précédent
            indices = []
            for k in self._indices_categorie_produit.values():
                indices.append(k[categorie_selectionnee][index_selectionne-1])
            fig, ax = plt.subplots(figsize=(8, 6))  # Ajuster la taille du tracé
            ax.bar(range(1, len(self._indices_categorie_produit) + 1), indices, color='skyblue')
            ax.set_xlabel('Pays')
            ax.set_ylabel("Valeur de l'indice")
            ax.set_title(f"Histogramme pour la catégorie '{categorie_selectionnee}' pour l'indice {index_selectionne}")
            ax.yaxis.grid(True)  # Ajouter une grille horizontale
            ax.set_xticks(range(1,len(self._indices_categorie_produit)+1))  # Définir les positions des ticks sur l'axe des abscisses (+1 car sinon le premier pays s'affiche en 0)
            ax.set_xticklabels(self._indices_categorie_produit.keys())  # Attribuer les noms des pays aux positions des ticks

            canvas = FigureCanvasTkAgg(fig, master=fenetre)
            canvas.draw()
            canvas.get_tk_widget().grid(row=1, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")


        def on_index_selected(event):
            index_selectionne = int(selecteur_index.get()) # important de metre un
            # entier car str par défault
            categorie_selectionnee = selecteur_categorie.get()
            tracer_histogramme(index_selectionne, categorie_selectionnee)

        def on_category_selected(event):
            index_selectionne = int(selecteur_index.get())
            categorie_selectionnee = selecteur_categorie.get()
            tracer_histogramme(index_selectionne, categorie_selectionnee)

        # Création de la fenêtre principale
        fenetre = tk.Tk()
        fenetre.title('Histogramme interactif')

        # Sélecteur d'indices
        indices = list(range(1, len(self._indices_categorie_produit['France']['High-Tech']) + 1))
        selecteur_index = ttk.Combobox(fenetre, values=indices)
        selecteur_index.grid(row=0, column=0, padx=10, pady=10)
        selecteur_index.current(0)
        selecteur_index.bind("<<ComboboxSelected>>", on_index_selected)

        # Sélecteur de catégorie
        categories = list(self._indices_categorie_produit['France'].keys())
        selecteur_categorie = ttk.Combobox(fenetre, values=categories)
        selecteur_categorie.grid(row=0, column=1, padx=10, pady=10)
        selecteur_categorie.current(0)
        selecteur_categorie.bind("<<ComboboxSelected>>", on_category_selected)

        # Affichage initial de l'histogramme
        tracer_histogramme(indices[0], categories[0])

        # Lancement de la boucle principale
        fenetre.mainloop()

    def AfficherCarte(self):
        return 'yo'

    def ChargerNouveauxIndices():
        return 'yo'

# test histogramme
dic_test = {
            'France': {
                'High-Tech': [82, 75, 90, 85],
                'Fruit': [60, 65, 70, 68]
            },
            'Allemagne': {
                'High-Tech': [75, 70, 80, 78],
                'Fruit': [55, 60, 65, 63]
            },
            'USA': {
                'High-Tech': [90, 85, 95, 92],
                'Fruit': [70, 75, 80, 78]
            }}

mon_test = InterfaceUtilisateur({"f": 5}, dic_test)
mon_test.plot_histogramme()

# test carte
