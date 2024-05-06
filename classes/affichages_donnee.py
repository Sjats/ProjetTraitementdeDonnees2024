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

# import pour donnée les plus récentes
# from produit import Produit
# from categorie_produit import CategorieProduit


class AffichageDonnees:
    def __init__(self, indices_produits: dict,
                 indices_categorie_produit: dict):
        """
        Initialise une instance de la classe InterfaceUtilisateur.

        Attributes:
        indices_produits : dict
            Un dictionnaire contenant les indices des produits par pays.
        indices_categorie_produit : dict
            Un dictionnaire contenant les indices des catégories de produits
            par pays.
        """
        if not isinstance(indices_produits, dict):
            raise TypeError("Les indices des produits doivent"
                            " être renseignés sous la forme "
                            "d'un dictionnaire.")
        if not isinstance(indices_categorie_produit, dict):
            raise TypeError("Les indices des catégories de produits"
                            " doivent être renseignés sous "
                            "la forme d'un dictionnaire.")
        for key1, value1 in indices_produits.items():
            if not isinstance(value1, dict):
                raise TypeError("Les informations pour un pays dans produit"
                                " doivent être sous forme de dictionnaire")
            for key2, value2 in value1.items():
                if not isinstance(value2, list):
                    raise TypeError("Les valeures numériques des indices des "
                                    "produits doivent être renseignés sous"
                                    " forme de liste")
        for key, value1 in indices_categorie_produit.items():
            if not isinstance(value1, dict):
                raise TypeError("Les informations pour un pays dans catégorie"
                                " doivent être sous forme de dictionnaire")
            for key2, value2 in value1.items():
                if not isinstance(value2, list):
                    raise TypeError("Les valeures numériques des indices des "
                                    "catégories doivent être renseignés sous"
                                    " forme de liste")

        self._indices_produits = indices_produits
        self._indices_categorie_produit = indices_categorie_produit
        self.canvas = None
        self.mon_dict = None

    def plot_histogramme(self, sur_quoi: bool, execute_apres):
        # à faire : remplacer par le nom des indices sur le sélecteur.
        """
        Génère un histogramme interactif permettant de sélectionner la
        catégorie ou le produit (en fonction de notre choix) et l'indice.

        Attributes
        sur_quoi : bool
            T : si on veut s'intéresser aux produits
            F : si on veut s'intéresser aux catégories
        """
        if not isinstance(sur_quoi, bool):
            raise TypeError("sur_quoi doit être une instance de bool.")
        if not sur_quoi:
            mon_dict = self._indices_categorie_produit
        else:
            mon_dict = self._indices_produits

        indices = ["indice01", "indicefrance"]
        categories_ou_produit = list(mon_dict['France'].keys())

        def tracer_histogramme(index_selectionne,
                               categorie_ou_produit_selectionnee,
                               indices):
            """
            Crée l'histogramme pour un indice et une catégorie précise
            déjà sélectionnée.
            """
            plt.clf()
            index_selectionne_num = indices.index(index_selectionne)
            indices = []
            for k in mon_dict.values():
                if k[categorie_ou_produit_selectionnee] is not None:
                    ind = k[categorie_ou_produit_selectionnee]
                    ind = ind[index_selectionne_num]
                    indices.append(ind)
                else:
                    indices.append(0)
            fig, ax = plt.subplots(figsize=(8, 6))
            ax.bar(mon_dict.keys(), indices, color='skyblue')
            ax.set_xlabel('Pays')
            ax.set_ylabel("Valeur de l'indice")
            if sur_quoi:
                ax.set_title("Histogramme pour le produit "
                             f"'{categorie_ou_produit_selectionnee}' pour "
                             f"l'indice {index_selectionne}")
            if not sur_quoi:
                ax.set_title("Histogramme pour la catégorie "
                             f"'{categorie_ou_produit_selectionnee}' pour "
                             f"l'indice {index_selectionne}")
            ax.yaxis.grid(True)
            plt.xticks(rotation=90)
            plt.tight_layout()

            return fig

        def on_selected(event):
            """
            Met à jour l'histogramme en fonction de la sélection de
            l'utilisateur dans les listes déroulantes d'indices et
              de catégories.

            Args:
                event: L'événement déclenché par la sélection de l'utilisateur.
            """
            if self.canvas:
                # Détruire l'ancien widget du graphique
                self.canvas.get_tk_widget().destroy()
            index_selectionne = selecteur_index.get()
            categorie_ou_produit_selectionnee = selecteur_categorie.get()
            fig = tracer_histogramme(index_selectionne,
                                     categorie_ou_produit_selectionnee,
                                     indices)
            self.canvas = FigureCanvasTkAgg(fig, master=frame_graphe)
            self.canvas.draw()
            self.canvas.get_tk_widget().pack(fill=tk.BOTH, expand=True)

        # Création de la fenêtre principale
        fenetre = tk.Tk()
        fenetre.title('Histogramme interactif')

        # Sélecteur d'indices
        selecteur_index = ttk.Combobox(fenetre, values=indices)
        selecteur_index.pack(padx=10, pady=10)
        selecteur_index.current(0)
        selecteur_index.bind("<<ComboboxSelected>>", on_selected)

        # Sélecteur de catégorie

        selecteur_categorie = ttk.Combobox(fenetre,
                                           values=categories_ou_produit)
        selecteur_categorie.pack(padx=10, pady=10)
        selecteur_categorie.current(0)
        selecteur_categorie.bind("<<ComboboxSelected>>", on_selected)

        frame_graphe = tk.Frame(fenetre)
        frame_graphe.pack(fill=tk.BOTH, expand=True)

        # Affichage initial de l'histogramme
        on_selected(None)

        def on_close():
            fenetre.destroy()
            execute_apres()

        fenetre.protocol("WM_DELETE_WINDOW", on_close)
        # Lancement de la boucle principale
        fenetre.mainloop()

    def AfficherCarte(self, sur_quoi: bool):
        """
        Affiche une carte interactive permettant
        de séléctionner la catégorie de produit et l'indice.
        La carte affiche les indices par pays sous forme
        d'un dégradé de couleurs

        Attributes
        sur_quoi : bool
            T : si on veut s'intéresser aux produits
            F : si on veut s'intéresser aux catégories
        """
        if not isinstance(sur_quoi, bool):
            raise TypeError("sur_quoi doit être une instance de bool.")
        if not sur_quoi:
            mon_dict = self._indices_categorie_produit
        else:
            mon_dict = self._indices_produits
        chemin_geojson = 'donnees/world_country_boundaries.geojson.json'
        gdf = gpd.read_file(chemin_geojson)  # Chemin vers le fichier GeoJSON

        country_code_map = {
            country.alpha_2: country.name for country in pycountry.countries
            }
        gdf['code'] = gdf['code'].map(country_code_map)
        # remplacer code alpha2 par nom du pays
        indices_t = ["indice01", "indicefrance"]
        categories_ou_produits = list(mon_dict['France'].keys())
        indice = st.sidebar.selectbox("Choisissez un indice :", indices_t)
        index_indice = indices_t.index(indice)
        if not sur_quoi:
            categories_ou_produits = st.sidebar.selectbox(
                "Choisissez une catégorie :", categories_ou_produits)
            st.markdown(
                f"<h1 style='text-align: center; color: purple; font-size: "
                f"24px;'>Visualisation de l'indice {indice} par pays pour "
                f"la catégorie {categories_ou_produits}</h1>",
                unsafe_allow_html=True)
        else:
            categories_ou_produits = st.sidebar.selectbox(
                "Choisissez un produit :", categories_ou_produits)
            st.markdown(
                f"<h1 style='text-align: center; color: purple; font-size:"
                f" 24px;'>Visualisation de l'indice {indice} par pays pour"
                f" le produit {categories_ou_produits}</h1>",
                unsafe_allow_html=True)

        # Extraire les données pour l'indice et la catégorie sélectionnés
        data = {}
        for pays, valeurs in mon_dict.items():
            if categories_ou_produits in valeurs:
                if valeurs[categories_ou_produits] is not np.nan:
                    data[pays] = valeurs[categories_ou_produits][index_indice]
                else:
                    data[pays] = np.nan

        # Dataframe car Plotly prend un dataframe en entrée
        df_plotly = pd.DataFrame({'pays': list(data.keys()),
                                  'Indice': list(data.values())})

        # Créer la carte avec Plotly
        fig = px.choropleth(df_plotly,
                            geojson=gdf,
                            locations='pays',
                            color='Indice',
                            color_continuous_scale='YlGnBu',
                            range_color=(min(data.values()),
                                         max(data.values())),
                            featureidkey='properties.code',
                            projection='natural earth',
                            labels={'Indice': f'Indice {indice}'}
                            )

        # Afficher la carte dans Streamlit
        st.plotly_chart(fig)


"""
# test histogramme
categories_test = {
            'France': {
                'High-Tech': [82, 75, 90, 85],
                'Articles de sport et de plein air': [60, 65, 70, 68]
            },
            'Greenland': {
                'High-Tech': [75, 70, 80, 78],
                'Articles de sport et de plein air': [55, 60, 65, 63]
            },
            'Russian Federation': {
                'High-Tech': [90, 85, 95, 50],
                'Articles de sport et de plein air': [70, 75, 80, 50]
            }}

# produits_test = {
            'France': {
                'Sac à dos imperméable': [82, 75, 90, 85],
                'Tapis de yoga antidérapant': [60, 65, 70, 68]
            },
            'Greenland': {
                'Sac à dos imperméable': [75, 70, 80, 78],
                'Tapis de yoga antidérapant': [55, 60, 65, 63]
            },
            'Russian Federation': {
                'Sac à dos imperméable': [90, 85, 95, 50],
                'Tapis de yoga antidérapant': [70, 75, 80, 50]
            }}

#mon_test = AffichageDonnees(produits_test, categories_test)

# ne pas executer les deux en même temps
#mon_test.plot_histogramme(False)
#mon_test.AfficherCarte(False)
"""
