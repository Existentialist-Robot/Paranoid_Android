# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:57:57 2019

@author: eredm
"""

from json import load
import requests
from astropy.io import fits
from astropy.utils.data import download_file
import os

base_url = "ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/NEOSSAT/ASTRO/"

year_urls = [base_url + year for year in ['2015/', '2019/']]
days = [str.zfill(str(num), 3) for num in range(1, 366)]
html_days = ["""<td sortable-data="1""" + day + """">""" for day in days]

day_urls = []
valid_urls = []

for year_url in year_urls:
    for day in days:
        day_urls.append(year_url + day + '/')

for day_url in day_urls:
    try:
        requests.get(day_url)
    except:
        print("Failed:", day_url)
    else:
        valid_urls.append(day_url)

