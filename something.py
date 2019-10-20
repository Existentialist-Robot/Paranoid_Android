# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:12:52 2019

@author: mengh
"""

from astropy.utils.data import download_file
from astropy.io import fits
import numpy as np
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt


pauls_num = 133

year = "2019"
folder = "133" # throw folder into a loop - for folder in range(len(folders))
fname ="NEOS_SCI_2019133041551.fits"
base_url = "ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/NEOSSAT/ASTRO/"
image_file_1 = download_file(base_url + '2019/133/NEOS_SCI_2019133041551.fits')

hdu_list_1 = fits.open(image_file_1)
hdu_list_1.info()

image_data_1 = hdu_list_1[0].data
print(type(image_data_1))
print(image_data_1.shape)
RawVolt_1 = hdu_list_1[1].data
ACS_History_1 = hdu_list_1[2].data
Image_RD_1 = hdu_list_1[3].data
CCD_History_1 = hdu_list_1[4].data
RawTlm_1 = hdu_list_1[5].data
#image_data = fits.getdata(image_file)
#plt.figure(figsize=(15, 15))
#plt.imshow(image_data,cmap = 'gray',vmin=1587,vmax = 3000)
#plt.colorbar()
#NBINS = 1000
#histogram = plt.hist(image_data.flatten(),NBINS)

#hdu_list[0].header['DATE']

Params = [None]*10
Params[1] = 'abs'
Params[0] = '20190101'










