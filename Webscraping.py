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

#result = requests.get("https://www.whitehouse.gov/briefings-statements/")
result = requests.get("https://fr.indeed.com/Paris-(75)-Emplois-Data-Analyst")

src = result.content
soup = BeautifulSoup(src, 'lxml')

# annonces = []
# for h2_tag in soup.find_all('h2'):
#     a_tag = h2_tag.find('a')
#     annonces.append(a_tag.attrs['title'])
#     # urls.append(a_tag.attrs['href'])
# print('Voici le premier élément de la liste :')
# print(annonces)



def getCompanyNamesIndeed(soupObject):
    liste = []
    firmNames = soupObject.find_all("span", class_="company")
    for e in firmNames:
        liste.append(e.text)
    return liste

def getAdName(soupObject):
    liste = []
    for e in soupObject.find_all('h2'):
        a_tag = e.find('a')
        liste.append(a_tag.text)
    return liste

def getAdLink(soupObject):
    liste = []
    for e in soupObject.find_all('h2'):
        a_tag = e.find('a')
        liste.append("https://fr.indeed.com" + str(a_tag.attrs['href']))
    return liste

def getAdDate(soupObject):
    liste = []
    for e in soupObject.find_all("span", class_="date"):
        liste.append(e.text)
    return liste


if __name__ == "__main__":
    
    result = requests.get("https://fr.indeed.com/Paris-(75)-Emplois-Data-Analyst")
    src = result.content
    soup = BeautifulSoup(src, 'lxml')
    
    companyName = getCompanyNamesIndeed(soup)
    adName      = getAdName(soup)
    link        = getAdLink(soup)
    date        = getAdDate(soup)
    
    
    df = pd.DataFrame()
    df['Company Name'] = companyName
    df['Ad Name']      = adName
    df['Ad Link']      = link
    df['publication date'] = date
    print(df['Ad Name'])
    # n = len(link)
    
    # for i in range(n):
    #     print(str(companyName[i]) + "\n" + str(adName[i]) + "\n" + str(link[i]))
    
    
    
        