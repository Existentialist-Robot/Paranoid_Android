# -*- coding: utf-8 -*-
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:12:52 2019

@author: mengh
"""

from astropy.utils.data import download_file
import matplotlib
from astropy.io import fits
import numpy as np
from matplotlib.colors import LogNorm
import matplotlib.pyplot as plt
base_url = "ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/NEOSSAT/ASTRO/"
image_file_1 = download_file('ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/NEOSSAT/ASTRO/2017/125/DARK/FINE_POINT/NEOS_SCI_2017125084700.fits',cache = True)
image_file_2018_survey_1=download_file(base_url+'/2018/318/Survey__237.5_-8.0_322.8/FINE_POINT/NEOS_SCI_2018318193822.fits',cache = True)
image_file_2018_survey_2=download_file(base_url+'/2018/318/Survey__239.1_-6.5_323.1/FINE_POINT/NEOS_SCI_2018318225914.fits',cache = True)
image_file_2019_1 = download_file(base_url+'/2019/006/NEOS_SCI_2019006000157.fits')
image_file_2019_2 = download_file(base_url+'/2019/006/NEOS_SCI_2019006000404_clean.fits')
image_file_2019_3 = download_file(base_url+'/2019/029/NEOS_SCI_2019029001813.fits')
image_file_2019_4 = download_file(base_url+'/2019/133/NEOS_SCI_2019133041551.fits')
test = download_file('ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/NEOSSAT/ASTRO/2017/272/1989_VB/RATE_SLEW/NEOS_SCI_2017272221250.fits',cache = True)

hdu_list_1 = fits.open(image_file_1)
hdu_list_1.info()
hdu_list_2 = fits.open(image_file_2018_survey_1)
hdu_list_2.info()
hdu_list_3 = fits.open(image_file_2018_survey_2)
hdu_list_3.info()
hdu_list_4 = fits.open(image_file_2019_1)
hdu_list_4.info()
hdu_list_5 = fits.open(image_file_2019_2)
hdu_list_5.info()
hdu_list_6 = fits.open(image_file_2019_3)
hdu_list_6.info()
hdu_list_6 = fits.open(image_file_2019_4)
hdu_list_6.info()
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










