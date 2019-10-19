# -*- coding: utf-8 -*-
"""
Created on Fri Oct 18 23:12:52 2019

@author: mengh
"""

from astropy.utils.data import download_file
from astropy.io import fits
import numpy as np
from matplotlib.colors import LogNorm
image_file = download_file('ftp://ftp.asc-csa.gc.ca/users/OpenData_DonneesOuvertes/pub/NEOSSAT/ASTRO/2017/125/DARK/FINE_POINT/NEOS_SCI_2017125084700.fits',cache = True)
hdu_list = fits.open(image_file)
hdu_list.info()
image_data = hdu_list[0].data
print(type(image_data))
print(image_data.shape)
plt.imshow()
