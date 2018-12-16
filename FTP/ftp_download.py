# -*- coding: utf-8 -*-
"""
Created on Sun Dec 16 11:13:33 2018

@author: Vivek
"""
from ftplib import FTP
import os


# download_file_via_ftp_with("isd-lite-format.pdf")

def download_file_via_ftp_with(filename, 
                               hostname = "ftp.pyclass.com", 
                               username = "student@pyclass.com", 
                               password = "student123"):
    ftp = FTP(hostname)
    ftp.login(username, password)
    #print(ftp.nlst)
    ftp.cwd("Data")
    os.chdir("C://Users")
    with open(filename, "wb") as file:
        ftp.retrbinary("RETR %s" % filename, file.write)
    
    ftp.close()