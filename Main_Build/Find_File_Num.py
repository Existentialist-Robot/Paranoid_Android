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

#%%

from astropy.utils.data import download_file
from astropy.io import fits
import numpy as np
import matplotlib.pyplot as plt

year = "2019"
folder = "133" # throw folder into a loop - for folder in range(len(folders))
fname ="NEOS_SCI_2019133041551.fits"
base_url = "ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/NEOSSAT/ASTRO/"
image_file_1 = download_file(base_url + '2019/133/NEOS_SCI_2019133041551.fits')

hdu = fits.open(image_file_1)
hdu.info()
hdu[0].header

hdu[0].header['JPOS2_1'] # X
hdu[0].header['JPOS2_2'] # Y
hdu[0].header['JPOS2_3'] # Z

image_data_1 = hdu[0].data
ACS_History_1 = hdu[2].data
Image_RD_1 = hdu[3].data
CCD_History_1 = hdu[4].data # 
RawTlm_1 = hdu[5].data # Raw Telemetry

## Check Image
#print(type(image_data_1))
#print(image_data_1.shape)
#RawVolt_1 = hdu[1].data
#image_data = fits.getdata(image_file)
#plt.figure(figsize=(15, 15))
#plt.imshow(image_data,cmap = 'gray',vmin=1587,vmax = 3000)
#plt.colorbar()
#NBINS = 1000
#histogram = plt.hist(image_data.flatten(),NBINS)

'''
 Attitude Control System (ACS)
 (-0.131125, '16 - FINE_POINT', '85 - OPEN', 0.93560696, 0.23001328, -0.26094922, 0.060323898, -6.1442245e-07, -5.1281575e-07, -6.3954195e-07)
 Time from exposure start (s)
 Attitude control state ()
 Shutter state
 Estimated q0 (s) 
 Estimated q1 (s)
 Estimated q2 (s)
 Estimated q3 (s)
 Estimated w0 (s)
 Estimated w1 (s)
 Estimated w2 (s)
 
JPOS2_1 =           -3747.5000 / J2000 Position at Exp middle, X-component (km) 
JPOS2_2 =            2484.5916 / J2000 Position at Exp middle, Y-component (km) 
JPOS2_3 =           -5585.4644 / J2000 Position at Exp middle, Z-component (km)

POINTING	CMD	Commanded spacecraft pointing (Celestial Coordinates).
ELA min/maxk	Earth limb angle.
Vel_nnn	Velocity around X/Y/Z.
Roll / Avg / Dec_VEL	Roll, Avg, Declination velocity @ midpoint of exposure.
RA_VEL  =           -0.0000007 / [hr/s] Average angular slew vel. in RA over exp
DEC_VEL =           -0.0000078 / [deg/s] Average angular slew vel. in Dec over e
ROL_VEL =            0.0000026 / [deg/s] Average angular slew vel. in Roll over 
'''




    

