import folium
import pandas

#Read volcano data
data = pandas.read_csv("Volcanoes_USA.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
name = list(data["NAME"])
status = list(data["STATUS"])
elev = list(data["ELEV"])
vol_type = list(data["TYPE"])

#Returns color depending on elevation
def color_finder(elev):
    if (elev < 2000):
        return "green"
    elif (elev < 3000):
        return "orange"
    else:
        return "red"

#Create Map object of USA
map = folium.Map(location=[39.639507,-95.8480806], zoom_start=5.15)

#Create Feature Group with Volcanoes
fg_vol = folium.FeatureGroup(name="Volcanoes")

for lt, ln, nm, st, el, tp in zip(lat, lon, name, status, elev, vol_type):
    clr = color_finder(el)
    fg_vol.add_child(folium.CircleMarker(
        location=[lt,ln],
        radius=7,
        popup=folium.Popup("Name: "+nm+" | Elevation: "+str(el)+"m | Status: "+st+" | Type: "+tp, parse_html=True),
        fill_color=clr, color="grey", fill=True, fill_opacity=0.7))
    
#Add json file with Population data
pop_data = open('world.json', 'r', encoding='utf-8-sig')
#Create Feature Group with Population
fg_pop = folium.FeatureGroup(name="Population")
fg_pop.add_child(folium.GeoJson(data=pop_data.read(),
                           style_function=lambda x: {'fillColor':'lightgreen' if x['properties']['POP2005'] < 10000000
                                                    else 'green' if 10000000 <= x['properties']['POP2005'] < 20000000
                                                    else 'yellow' if 20000000 <= x['properties']['POP2005'] < 50000000
                                                    else 'orange' if 50000000 <= x['properties']['POP2005'] < 100000000
                                                    else 'red'}))

#Add Feature Groups to Map
map.add_child(fg_vol)
map.add_child(fg_pop)
#Add Layer Control
map.add_child(folium.LayerControl())

map.save("WorldMap.html")
pop_data.close()