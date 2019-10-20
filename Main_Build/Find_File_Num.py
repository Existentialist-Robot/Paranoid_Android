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
placeholder = ['a;lsdkj', '3dlsaf']
year_urls = [base_url + year + '/' for year in years]
days = ['1' + str.zfill(str(num), 3) for num in range(1, 366)]
html_days = ["""<td sortable-data="1""" + day + """">""" for day in days]

image_urls = []

def get_meta_data(image_list):
    codeList = ['cp037', 'cp273', 'cp424', 'cp437', 'cp500', 'cp720', 
    'cp737', 'cp775', 'cp850', 'cp852', 'cp855', 'cp856', 'cp857', 
    'cp858', 'cp860', 'cp861', 'cp862', 'cp863', 'cp864', 'cp865', 
    'cp866', 'cp869', 'cp875', 'cp949', 'cp1006', 'cp1026', 'cp1125', 
    'cp1140', 'cp1250', 'cp1251', 'cp1252', 'cp1253', 'cp1254', 
    'cp1255', 'cp1256', 'cp1257', 'cp1258', 'gbk', 'gb18030', 'latin_1', 
    'iso8859_2', 'iso8859_3', 'iso8859_4', 'iso8859_5', 'iso8859_6', 
    'iso8859_7', 'iso8859_8', 'iso8859_9', 'iso8859_10', 'iso8859_11', 
    'iso8859_13', 'iso8859_14', 'iso8859_15', 'iso8859_16', 'koi8_r', 
    'koi8_t', 'koi8_u', 'kz1048', 'mac_cyrillic', 'mac_greek', 'mac_iceland', 
    'mac_latin2', 'mac_roman', 'mac_turkish', 'ptcp154', 'shift_jis_2004', 'shift_jisx0213']

    for url in image_list:
        url = urllib.request.urlopen(url)
        data = url.read()
        # print(str(data[34559:34562]))
        data = str(data).split('                                                                                                                                                                                               ')[0]
        newData = str(data[:33600]).split('/')
        print(newData[-1])
        # for datapoint in newData:
        #     print(datapoint)
        # print(str(data[:5000]).split('                  '))
        # for code in codeList:
        #     try:
        #         data = data.decode(code)
        #     except:
        #         pass
        #     else:
        #         print("Successful decoding! Code: {}".format(code))
        # data = data.decode("cp037")

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
            if counter > 200:
                get_meta_data(image_urls)
            if counter > 250:
                sys.exit(1)
            # print(image)


end = time()

print("Total images read: {}.".format(counter))
print("Total seconds taken: {}. ({} minutes)".format(end - start, (end - start) / 60.0))


    

