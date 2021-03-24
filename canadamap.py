import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
#install folium
!conda install -c conda-forge folium=0.5.0 --yes
import folium
#print('Folium installed and imported!')
# define the world map
#world_map = folium.Map()
# display world map
#world_map
# define the world map centered around Canada with a low zoom level
world_map = folium.Map(location=[56.130, -106.35], zoom_start=4)
# display world map
world_map

#for higher zoom
# define the world map centered around Canada with a higher zoom level
#world_map = folium.Map(location=[56.130, -106.35], zoom_start=8)

# display world map
#world_map

