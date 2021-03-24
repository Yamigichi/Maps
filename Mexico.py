import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
#install folium
!conda install -c conda-forge folium=0.5.0 --yes
import folium
#print('Folium installed and imported!')
# define the world map
#define Mexico's geolocation coordinates
mexico_latitude = 23.6345 
mexico_longitude = -102.5528
mexico_map = folium.Map(location=[mexico_latitude, mexico_longitude], zoom_start=4)
# display world map
mexico_map
