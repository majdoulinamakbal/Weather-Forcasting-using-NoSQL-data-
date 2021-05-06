import json
import urllib.request

import pymongo
import requests
from django.http import HttpResponse

from django.shortcuts import render
from geopy.geocoders import Nominatim
from pymongo import MongoClient
import datetime
# Create your views here.


def home(request):
    return render(request, 'home.html', {})
def mapp(request):
    return render(request, 'map.html', {})

def température(request):
    client=MongoClient('mongodb://localhost:27017')
    db=client.test_weather
    geolocator = Nominatim()
    place = request.GET['ville']
    location = geolocator.geocode(place)
    la=location.latitude
    lg=location.longitude
    collection = db.place
    url='https://api.darksky.net/forecast/a0331a38a059d30797abd018c443cf00/%s,%s?units=si'%(la,lg)
    json_obj=urllib.request.urlopen(url)
    data=json.load(json_obj)
    datasummary=data['hourly']
    for item in datasummary['data']:
        collection.insert(item)
    Listcity=collection.find()
    temperature=[]
    time=[]
    # humidity=[]
    # precipIntensity=[]
    for item in Listcity:
        x=datetime.datetime.fromtimestamp(item['time']).strftime('%Y-%m-%d %H')
        time.append(x)
        temperature.append(item['temperature'])
        # humidity.append(item['humidity'])
        # precipIntensity.append(item['precipIntensity'])

    
    return render(request,'temperature.html',{'temperature': temperature, 'time': time,'place':place})


def humidité(request):
    client=MongoClient('mongodb://localhost:27017')
    db=client.test_weather
    geolocator = Nominatim()
    place = request.GET['ville']
    location = geolocator.geocode(place)
    la=location.latitude
    lg=location.longitude
    collection = db.place
    url='https://api.darksky.net/forecast/a0331a38a059d30797abd018c443cf00/%s,%s?units=si'%(la,lg)
    json_obj=urllib.request.urlopen(url)
    data=json.load(json_obj)
    datasummary=data['hourly']
    for item in datasummary['data']:
        collection.insert(item)
    Listcity=collection.find()
    time=[]
    humidity=[]
    # precipIntensity=[]
    for item in Listcity:
        x=datetime.datetime.fromtimestamp(item['time']).strftime('%Y-%m-%d %H')
        time.append(x)
        humidity.append(item['humidity'])
        # precipIntensity.append(item['precipIntensity'])

    
    return render(request,'humidity.html',{'time': time,'place':place,'humidity':humidity})


def precipitations(request):
    client=MongoClient('mongodb://localhost:27017')
    db=client.test_weather
    geolocator = Nominatim()
    place = request.GET['ville']
    location = geolocator.geocode(place)
    la=location.latitude
    lg=location.longitude
    collection = db.place
    url='https://api.darksky.net/forecast/a0331a38a059d30797abd018c443cf00/%s,%s?units=si'%(la,lg)
    json_obj=urllib.request.urlopen(url)
    data=json.load(json_obj)
    datasummary=data['hourly']
    for item in datasummary['data']:
        collection.insert(item)
    Listcity=collection.find()
    time=[]
    windSpeed=[]
    for item in Listcity:
        x=datetime.datetime.fromtimestamp(item['time']).strftime('%Y-%m-%d %H')
        time.append(x)
        windSpeed.append(item['windSpeed'])

    
    return render(request,'precipitations.html',{'time': time,'place':place,'windSpeed':windSpeed})
