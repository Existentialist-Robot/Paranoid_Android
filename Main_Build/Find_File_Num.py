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



base_url = "ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/NEOSSAT/ASTRO/"
years = ['NESS/2015', '2019']
year_urls = [base_url + year + '/' for year in years]
days = ['1' + str.zfill(str(num), 3) for num in range(1, 366)]

for item in ['347-Ness', '348-Comet249P']:
    days.append(item)

image_urls = []

file = download_file(base_url +)

def get_meta_data(image_list):
    for url in image_list:
        data = fits.open(url)
        print(data['DATE'])
        # print(data.data)
        sys.exit(1)

counter = 0
start = time()
for year in years:

    """ Gets the days of each year """
    # print(base_url + year)
    year_url = urllib.request.urlopen(base_url + year)
    days = year_url.read().decode('ASCII')
    days = days.split('\r')
    del days[0]
    del days[-1]

    for day in days:
        """ Get the images for each day of each year """
        day = day.split(" ")[-1]
        # print(base_url + year + '/' + day + '/')
        day_url = urllib.request.urlopen(base_url + '/' + year + '/' + day + '/')
        images = day_url.read().decode('ASCII').split('\r')
        # print(len(images))

        for image in images:
            counter += 1
            """ Gets the image filename of each file for each day for each year """
            image = image.split(" ")[-1]
            image_urls.append(base_url + '/' + year + '/' + day + '/' + image)
            if counter > 1:
                get_meta_data(image_urls)
            # print(image)


end = time()

print("Total images read: {}.".format(counter))
print("Total seconds taken: {}. ({} minutes)".format(end - start, (end - start) / 60.0))


    

