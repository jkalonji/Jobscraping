# -*- coding: utf-8 -*-
"""
Created on Mon Nov 16 14:30:19 2020

@author: Jérémie
"""

#Source initiale : https://github.com/vprusso/youtube_tutorials/blob/master/web_scraping_and_automation/beautiful_soup/white_house_example.py
#Documentation BeautifulSoup : https://www.crummy.com/software/BeautifulSoup/bs4/doc/

import requests
from bs4 import BeautifulSoup
import pandas as pd


def getCompanyNamesIndeed(soupObject):
    liste = []
    firmNames = soupObject.find_all("span", class_="company")
    for e in firmNames:
        liste.append(e.text)
    return liste

def getAdNameIndeed(soupObject):
    liste = []
    for e in soupObject.find_all('h2'):
        a_tag = e.find('a')
        liste.append(a_tag.text)
    return liste

def getAdLinkIndeed(soupObject):
    liste = []
    for e in soupObject.find_all('h2'):
        a_tag = e.find('a')
        liste.append("https://fr.indeed.com" + str(a_tag.attrs['href']))
    return liste

def getAdDateIndeed(soupObject):
    liste = []
    for e in soupObject.find_all("span", class_="date"):
        liste.append(e.text)
    return liste



if __name__ == "__main__":
    
    listeURLs = ["https://fr.indeed.com/Paris-(75)-Emplois-Data-Analyst", 
                 "https://fr.indeed.com/Paris-(75)-Emplois-Data-Engineer",
                 "https://fr.indeed.com/Paris-(75)-Emplois-Python-NLP",
                 "https://fr.indeed.com/Paris-(75)-Emplois-Python-Fintech"]

    DF = pd.DataFrame()
    
    for address in listeURLs:
        df = pd.DataFrame()
    
        result = requests.get(address)
        src = result.content
        soup = BeautifulSoup(src, 'lxml')
        
        companyName = getCompanyNamesIndeed(soup)
        adName      = getAdNameIndeed(soup)
        link        = getAdLinkIndeed(soup)
        date        = getAdDateIndeed(soup)
    

        df['Company Name']     = companyName
        df['Ad Name']          = adName
        df['Ad Link']          = link
        df['publication date'] = date
        
        DF = pd.concat([DF, df], ignore_index=True)
        

    print(DF)
 
    
    
    
        