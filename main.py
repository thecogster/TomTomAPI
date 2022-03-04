from turtle import pd


import pandas as pd
import numpy as np
import requests
import json

def datacollection():
    url = 'https://api.tomtom.com/search/2/poiSearch/Chinese%20Restaurant.json?key=MaG1sGHK8IEzPNsP2CsGt31gTcMGJx1E&categoryset=7315&countrySet=NL&limit=50'
    r = requests.get(url)
    parsed = json.loads(r.content)
    data = parsed['results']
    return data
