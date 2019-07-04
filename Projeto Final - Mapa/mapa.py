# -*- coding: utf-8 -*-
"""mapa.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1UOFjZoU2UUuzDZrIbrVvzxPXGqNXOvCH
"""

!pip install selenium

# https://python-visualization.github.io/folium/modules.html#module-folium.map
# https://python-visualization.github.io/folium/quickstart.html#Getting-Started
import pandas as pd
from selenium import webdriver
import folium
# import imgkit

# url = 'https://raw.githubusercontent.com/python-visualization/folium/master/examples/data'
country_geo = f'https://raw.githubusercontent.com/johan/world.geo.json/master/countries.geo.json'
#country_geo = f'https://raw.githubusercontent.com/johan/world.geo.json/master/countries/FIN.geo.json'
#country_geo1 = f'https://raw.githubusercontent.com/johan/world.geo.json/master/countries/BRA.geo.json'

state_data = pd.read_csv('result.csv')

# m = folium.Map(location=[20, 15],zoom_start=1.5, png_enabled=True)
# m = folium.Map(location=[20, 15],zoom_start=1.5)
# Em cima do CEFET
# m = folium.Map(location=[-22.9120758, -43.2251424],zoom_start=100)
m = folium.Map(location=[-22.9120758, -43.2251424],zoom_start=1)

# adiciona marcador
#folium.Marker(
#    location=[-22.9120758, -43.2251424],
#    popup='CEFET/RJ',
#    icon=folium.Icon(color='darkblue', prefix='fa', icon="fa-angle-double-down")
#).add_to(m)

folium.Choropleth(
    geo_data=country_geo,
    name='choropleth',
    data=state_data,
# 1 columns=['code', 'Surface area (km2)'],
# 2   columns=['code', 'Population in thousands (2017)'],  # esse
# 3   columns=['code', 'Sex ratio (m per 100 f, 2017)'],   # alguns legais, fogem muito
# 4   columns=['code', 'Urban population (% of total population)'], # esse
# 5   columns=['code', 'GDP per capita (current US$)'],
# 6   columns=['code', 'Energy production, primary (Petajoules)'],
# 7   columns=['code', 'CO2 emission estimates (million tons/tons per capita)'], # esse
# 8   columns=['code', 'Threatened species (number)'], # esse
   columns=['code', 'Individuals using the Internet (per 100 inhabitants)'], # metrica meio zoada... coisas acima de 100.
    key_on='feature.id',
    fill_color='YlOrRd',  # Escolher a cor https://www.datanovia.com/en/blog/the-a-z-of-rcolorbrewer-palette/
    fill_opacity=0.7,
    line_opacity=0.2,
    nan_fill_color = 'pink',
    nan_fill_opacity = 0.1,
    #legend_name='Unemployment Rate'    
).add_to(m)

# remove legend
for key in m._children:
    if key.startswith('choropleth'):
        print(m._children[key].__dict__['color_scale'])
        m._children[key].__dict__['color_scale'] = 0

folium.LayerControl().add_to(m)


m

#m.save('map.html')

#browser = webdriver.Firefox()
# browser.get('map.html')
# browser.save_screenshot('screenie.png')
