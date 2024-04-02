import pandas as pd
import geopandas as gpd
import folium
import branca.colormap as cm
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

    def AfficherCarte(self):
        # Créer une carte centrée sur une position initiale
        map_world = folium.Map(location=[0, 0], zoom_start=2)

        # Ajouter la couche de fond de carte OpenStreetMap
        folium.TileLayer('openstreetmap').add_to(map_world)

        # Afficher la carte
        map_world


    def plot_histogram(self, selected_index):
        countries = list(self._indices_categorie_produit.keys())
        indices = [data[country][selected_index] for country in countries]

        fig, ax = plt.subplots()
        color = colors[selected_index]  # Changer la couleur en fonction de l'indice
        ax.bar(countries, indices, color=color)
        ax.set_xlabel('Pays')
        ax.set_ylabel('Indice')
        ax.set_title(f'Histogramme pour l\'indice {selected_index}')

        canvas = FigureCanvasTkAgg(fig, master=window)
        canvas.draw()
        canvas.get_tk_widget().grid(row=1, column=0)
    # mettre a jour la fenêtre si je zoom
        window.update_idletasks()

# Exemple de données (remplacez cela par votre dictionnaire de données)
data = {
    'Pays1': [10, 20, 30],
    'Pays2': [15, 25, 35],
    'Pays3': [12, 22, 32]
}

def on_index_selected(event):
    selected_index = index_selector.current()
    plot_histogram(selected_index)

colors =['blue', 'green', 'red']
# Créer la fenêtre principale
window = tk.Tk()
window.title('Histogramme interactif')

# Créer un menu déroulant pour sélectionner l'indice
index_selector = ttk.Combobox(window, values=list(range(len(data['Pays1']))))
index_selector.grid(row=0, column=0)
index_selector.current(0)
index_selector.bind("<<ComboboxSelected>>", on_index_selected)

# Afficher l'histogramme initial
plot_histogram(index_selector.current())

# Lancer la boucle principale de l'interface
window.mainloop()



def ChargerNouveauxIndices():
    return 'yo'

x = InterfaceUtilisateur()
x.AfficherCarte()
