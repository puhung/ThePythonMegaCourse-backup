import folium
import pandas
import fontawesome

data = pandas.read_csv("Volcanoes.txt")
lat = list(data["LAT"])
lon = list(data["LON"])
elev = list(data["ELEV"])

def color_producer(elevation):
    if elevation < 1000:
        return 'green'
    elif 1000 <= elevation <3000:
        return 'orange'
    else:
        return 'red'

map = folium.Map(location=[38.58, -99.09],zoom_start=6, tiles = "Stamen Terrain")

#feature group Volcano
#marker is a feature and with feature groups you can add multiple features to the feature and keep the code more organized.
fgv= folium.FeatureGroup(name="Volcanoes")
#marker layer
#use for loop to create nultiple marker
#you can load the location from excel or csv files
#zip function can be used to loop through multiple lists
#type of el is a float number
for lt, ln, el in zip(lat, lon, elev) :
    fgv.add_child(folium.CircleMarker(location=[lt, ln], radius = 6, popup=str(el)+ " m", fill_color=color_producer(el),  color = 'grey', fill_opacity = 0.7))

#feature group Population
fgp= folium.FeatureGroup(name="Population")
#polygon layer
#adding polygons via folium is by using the folium.GeoJson method
#create GeoJson object
#open py method  is used for creating file objects, the parameter is the path of the file. 'r' == read mode
#The recent version of folium needs a string instead of a file as data input, thus we need to use read() method
#style_function attribute expects lambda functions, which are like normal functions but are written in single line of code 
fgp.add_child(folium.GeoJson(data=open('world.json', 'r', encoding='utf-8-sig').read(), 
style_function=lambda x : {'fillColor': 'yellow' if x['properties']['POP2005']<10000000 
else 'orange' if 10000000 <= x['properties']['POP2005'] < 20000000 else 'red'}))



#map object's children
map.add_child(fgv)
map.add_child(fgp)
#layer control: it is added as a child. You need to add feature group which is an object that contains the JSON layer and the marker layer. 
#Thus! you need to put this line after you added the feature group layer to the map
#Also, this layerControl method looks for objects added to map with add_child() and considers these each objects as 1 single item.
map.add_child(folium.LayerControl())

map.save("Map1.html")