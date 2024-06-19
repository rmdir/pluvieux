import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
import cartopy.crs as ccrs


fichier_nc = nc.Dataset(
    'projet-900M2/ndvi.nc', 'r')


# print(fichier_nc.variables)
# print(fichier_nc.dimensions)


# Extraire les données nécessaires
lat = fichier_nc.variables['latitude'][:]
lon = fichier_nc.variables['longitude'][:]
# Première instance temporelle pour 'ps'
ndvi = fichier_nc.variables['NDVI'][:]


# Convertir la pression de Pa à hPa pour une meilleure lisibilité

print(fichier_nc.variables['NDVI'])
# Fermer le fichier NetCDF
fichier_nc.close()


# Création de la carte
fig = plt.figure(figsize=(10, 5))
ax = fig.add_subplot(1, 1, 1, projection=ccrs.PlateCarree())
ax.set_global()
ax.coastlines()


# Ajouter les données de pression à la carte
# La fonction contourf crée une carte de contours remplie
contour = ax.contourf(lon, lat, ndvi, 60,
                      transform=ccrs.PlateCarree(), cmap='viridis')


# Ajouter une barre de couleur pour la légende
cbar = plt.colorbar(contour, orientation='horizontal', pad=0.05, aspect=50)
cbar.set_label('NDVI: Normalized Difference Vegetative Index')


# Titre et labels et sauvegarde de la carte
plt.title('Global NDVI')
plt.savefig('CarteNDVI2.png')

# Afficher la carte

plt.show()
