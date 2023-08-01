from django.shortcuts import render, redirect
import os
import folium

# Create your views here.
def home(request):
    shp_dir = os.path.join(os.getcwd(), 'media', 'data')
    m = folium.Map(location=[-1.3605, 35.7407], zoom_start=10)
    style_Narok = {'fillColor': '#228B22','color': '#228B22'}
    style_rivers = {'color': 'blue'}

    folium.GeoJson(os.path.join(shp_dir,'Narok.geojson'),name='Narok County',
    style_function = lambda x:style_Narok).add_to(m)
    folium.GeoJson(os.path.join(shp_dir,'rivers.geojson'),name='Narok Rivers',
    style_function = lambda x:style_rivers).add_to(m)

    folium.LayerControl().add_to(m)

    m = m._repr_html_()

    context={'my_map': m}
    return render(request,'geoApp/home.html',context)
