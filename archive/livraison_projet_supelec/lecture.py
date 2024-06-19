import netCDF4 as nc
from netCDF4 import Dataset

# Ouvrir le fichier NetCDF
fichier_nc = nc.Dataset('./download_files/ndvi.nc')

# Accéder aux variables et aux dimensions
# print(fichier_nc.variables)  # Afficher les variables
# print(fichier_nc.dimensions)  # Afficher les dimensions

ndvi_variable = fichier_nc.variables['NDVI']

# Lire les données NDVI dans une liste de listes
# Cela lit toutes les données NDVI dans une matrice numpy
ndvi_data = ndvi_variable[:]

# Convertir la matrice numpy en liste de listes
ndvi_liste = ndvi_data.tolist()
print(fichier_nc.variables.keys())
# Fermer le fichier NetCDF

fichier_nc.close()
