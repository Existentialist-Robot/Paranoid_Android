# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:57:57 2019

@author: eredm
"""

from astropy.io import fits
from astropy.utils.data import download_file
import os

base_url = "ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/NEOSSAT/ASTRO/"
years = {'2017':{},'2018':{},'2019':{}}
year_url = list(years.keys())
year_list = year_url
#print(list(years.keys()))
for index in range(len(year_url)):
    year_url[index] = base_url + str(year_url[index] + '/')
    years[year_list] = [os.path.join(year_url[index],o) for o in os.listdir(year_url[index]) 
                    if os.path.isdir(os.path.join(url[index],o))]
    
    
    
    
    

[x for x in os.listdir('ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/NEOSSAT/ASTRO/') if os.path.isfile(x)] # only files


d='.'
[os.path.join(d, o) for o in os.listdir(d) 
                    if os.path.isdir(os.path.join(d,o))]




for root, dirs, files in os.walk("."):
    path = root.split(os.sep)
    print((len(path) - 1) * '---', os.path.basename(root))
    for file in files:
        print(len(path) * '---', file)

image_file = download_file('http://data.astropy.org/tutorials/FITS-images/HorseHead.fits', cache=True )


[x for x in os.listdir('.') if os.path.isfile(x)] # only files





    
    
  