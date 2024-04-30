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
import pandas as pd

chemin_geojson = 'classes/world_country_boundaries.geojson.json'
gdf = gpd.read_file(chemin_geojson) # Chemin vers le fichier GeoJSON
print(gdf)