import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.append(parent_dir)

# Import pour histogramme :
import tkinter as tk
from tkinter import ttk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
# Import pour la carte interactive
import streamlit as st
import geopandas as gpd
import numpy as np
import plotly.express as px
import pandas as pd
import pycountry


class InterfaceUtilisateur:
    """
    indices_categorie_produit est sous cette forme :
    indice_catégorie_produit = {'france': {'high_tech': [1, 2, 3], 'fruit': [4, 5, 6]}}
    boucle for pour acéder à tout:
    for values in indice_catégorie_produit.values():
        for keys in indice_catégorie_produit.keys():

    """
    def ChargerNouveauxIndices():
        """
        fonction d'acutalisation qui s'assure d'avoir les données
         les plus récentes
        """
        return 'yo'

    def __init__(self, indices_produits, indices_categorie_produit):
        """
        Initialise une instance de la classe InterfaceUtilisateur.

        Attributes:
        indices_produits : dict
            Un dictionnaire contenant les indices des produits par pays.
        indices_categorie_produit : dict
            Un dictionnaire contenant les indices des catégories de produits par pays.
        """
        if not isinstance(indices_produits : dict):
            raise TypeError("les indices des produits doivent être renseignés sous la forme d'un dictionnaire.")
        if not isinstance(indices_categorie_produit : dict):
            raise TypeError("Les indices des catégories de produits doivent être renseignés sous la forme d'un dictionnaire.")
        self._indices_produits = indices_produits
        self._indices_categorie_produit = indices_categorie_produit


    def plot_histogramme(self):
        """
        Histogramme interactif qui permet de sélectionner la catégorie et l'indice.
        Il renvoie sous forme d'un histogramme l'indice par pays.

        """
        def tracer_histogramme(index_selectionne, categorie_selectionnee):
            """
            Crée l'histogramme pour un indice et une catégorie précise déjà séléctionnée.
            """
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
            """

            """
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
        """
        Affiche une carte interactive permettant
        de séléctionner la ctégorie de produit et l'indice.
        La carte affiche les indices par pays sous forme
        d'un dégradé de couleurs
        """
        chemin_geojson = 'classes/world_country_boundaries.geojson.json'
        gdf = gpd.read_file(chemin_geojson) # Chemin vers le fichier GeoJSON

        country_code_map = {country.alpha_2: country.name for country in pycountry.countries}
        gdf['code'] = gdf['code'].map(country_code_map) # remplacer code alpha2 par nom du pays
        list_pays = gdf['code'].tolist()
        indices_n = list(range(1, len(self._indices_categorie_produit['France']['High-Tech']) + 1)) # liste numérique des indices
        indices_t = ["indice_marius1", "indice_marius2", "indice_marius3", "indice_marius4"]
        categories = categories = list(self._indices_categorie_produit['France'].keys())
        indice = st.sidebar.selectbox("Choisissez un indice :", indices_t)
        index_indice = indices_t.index(indice)
        categorie = st.sidebar.selectbox("Choisissez une catégorie :", categories)
        st.markdown(f"<h1 style='text-align: center; color: purple; font-size: 24px;'>Visualisation de l'indice {indice} par pays pour la catégorie {categorie}</h1>", unsafe_allow_html=True)

        # Extraire les données pour l'indice et la catégorie sélectionnés
        data = {}
        for pays, valeurs in self.items():
            if categorie in valeurs:
                data[pays] = valeurs[categorie][index_indice-1]

        # Dataframe car Plotly prend un dataframe en entrée
        df_plotly = pd.DataFrame({'pays': list(data.keys()), 'Indice': list(data.values())})

        # Créer la carte avec Plotly
        fig = px.choropleth(df_plotly,
                            geojson=gdf,
                            locations='pays',
                            color='Indice',
                            color_continuous_scale='YlGnBu',
                            range_color=(min(data.values()), max(data.values())),
                            featureidkey='properties.code',
                            projection='natural earth',
                            labels={'Indice': f'Indice {indice}'}
                            )


        # Afficher la carte dans Streamlit
        st.plotly_chart(fig)

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

mon_test = InterfaceUtilisateur({"f": 5}, dic_test) # {"f": 5} dico de merde car on teste pas la dessus.
# mon_test.plot_histogramme()
mon_test.AfficherCarte()
