import numpy as np  # useful for many scientific computing in Python
import pandas as pd # primary data structure library
#install folium
!conda install -c conda-forge folium=0.5.0 --yes
import folium
#print('Folium installed and imported!')
# define the world map
world_map = folium.Map()
# display world map
world_map
