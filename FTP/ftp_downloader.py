# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 12:06:12 2018

@author: Vivek
"""

from ftplib import FTP, error_perm
import os

# dowload_file_via_ftp_with("010010-99999", 2010, 2014)

def dowload_file_via_ftp_with(stationId, startYear, endYear,
                              url = "ftp.pyclass.com",
                              username = "student@pyclass.com",
                              password = "student123"):
    ftp = FTP(url)
    ftp.login(username, password)
    if not os.path.exists("C:\\Users\\Vivek\\in"):
        os.makedirs("C:\\Users\\Vivek\\in")
    os.chdir("C:\\Users\\Vivek\\in")
    
    for year in range(startYear, endYear + 1):
        fullPath = "/Data/%s/%s-%s.gz" % (year, stationId, year)
        filename = os.path.basename(fullPath)
        try:
            with open(filename, "wb") as file:
                ftp.retrbinary("RETR %s" % fullPath, file.write)
                print("%s successfully downloaded" % filename)
        except error_perm:
            print("%s is not available" % filename)
            os.remove(filename)
        
    ftp.close()