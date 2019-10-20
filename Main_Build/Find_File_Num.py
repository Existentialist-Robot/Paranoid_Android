# -*- coding: utf-8 -*-
"""
Created on Sat Oct 19 12:57:57 2019

@author: eredm
"""

from json import load
from time import time
import urllib
from bs4 import BeautifulSoup as bs4
from astropy.io import fits
from astropy.utils.data import download_file
import os
import sys


# ftp = FTP('ftp.asc-csa.gc.ca')
# ftp.login()
# ftp.cwd('/users/OpenData_DonneesOuvertes/pub/NEOSSAT/ASTRO/')



base_url = "ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/NEOSSAT/ASTRO"
years = ['NESS/2015', '2019']
year_urls = [base_url + year + '/' for year in years]
days = ['1' + str.zfill(str(num), 3) for num in range(1, 366)]

for item in ['347-Ness', '348-Comet249P']:
    days.insert(0, item)

image_urls = []

def get_meta_data(image_list):
    for url in image_list:
        data = fits.open(url)
        print(data['DATE'])
        # print(data.data)
        sys.exit(1)

counter = 0
start = time()
for year in years:
    for day in days:
        counter += 1
        print(base_url + '/' + year + '/' + day + '/')
        if counter > 10:
            sys.exit(1)
        """ Get the images for each day of each year """
        try:
            day_url = urllib.request.urlopen(base_url + '/' + year + '/' + day + '/')
            images = day_url.read().decode('ASCII').split('\r')
        except Exception as e:
            pass
        else:
            for image in images:
                counter += 1
                """ Gets the image filename of each file for each day for each year """
                image = image.split(" ")[-1]
                print('reading in')
                image_urls.append(download_file(base_url + '/' + year + '/' + day + '/' + image))
            # print(image)


end = time()

print("Total images read: {}.".format(counter))
print("Total seconds taken: {}. ({} minutes)".format(end - start, (end - start) / 60.0))


    

