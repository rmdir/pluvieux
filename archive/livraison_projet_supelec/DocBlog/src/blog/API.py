import openeo
from unittest.mock import Mock
import rasterio.plot
import matplotlib.pyplot as plt
import rasterio
import numpy as np
import earthpy.plot as ep

# connect with the backend

url = "https://openeo.vito.be"
username = "baptiste.barraque@gmail.com"
password = "Applipluie12345*"
start_date = "2020-03-06"
end_date = "2020-03-07"
conn = openeo.connect(url)

# Setup process parameters

conn.authenticate_oidc('terrascope')
bbox = {'west': 5.05, 'south': 51.20, 'east': 5.15,
        'north': 51.24, 'crs': 'EPSG:4326'}
cube = conn.load_collection('TERRASCOPE_S2_TOC_V2',
                            bands=['B04', 'B03', 'B02', 'B01'])
cube = cube.filter_temporal("2020-03-06", "2020-03-15")
cube = cube.filter_bbox(bbox=bbox)
cube.download('basic.tiff', format='GTIFF')
