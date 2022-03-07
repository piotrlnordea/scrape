# -*- coding: utf-8 -*-
"""
Created on Mon Mar  7 19:04:44 2022

@author: piotr
"""

from bs4 import BeautifulSoup
from selenium import webdriver
 
option = webdriver.ChromeOptions()
#driver = webdriver.Firefox(executable_path=r'C:\selenium\geckodriver.exe')
# I use the following options as my machine is a window subsystem linux. 
# I recommend to use the headless option at least, out of the 3
option.add_argument('--headless')
option.add_argument('--no-sandbox')
option.add_argument('--disable-dev-sh-usage')
# Replace YOUR-PATH-TO-CHROMEDRIVER with your chromedriver location
driver = webdriver.Chrome(executable_path=r'C:\selenium\chromedriver.exe', options=option)
 
page = driver.get('https://www.imdb.com/chart/top/') # Getting page HTML through request
soup = BeautifulSoup(driver.page_source, 'html.parser') # Parsing content using beautifulsoup
 
totalScrapedInfo = [] # In this list we will save all the information we scrape
links = soup.select("table tbody tr td.titleColumn a") # Selecting all of the anchors with titles
first10 = links[:10] # Keep only the first 10 anchors
for anchor in first10:
    driver.get('https://www.imdb.com/' + anchor['href']) # Access the movie’s page
    infolist = driver.find_elements_by_css_selector('.ipc-inline-list')[0] # Find the first element with class ‘ipc-inline-list’
    informations = infolist.find_elements_by_css_selector("[role='presentation']") # Find all elements with role=’presentation’ from the first element with class ‘ipc-inline-list’
    scrapedInfo = {
        "title": anchor.text,
        "year": informations[0].text,
        "duration": informations[2].text,
    } # Save all the scraped information in a dictionary
    totalScrapedInfo.append(scrapedInfo) # Append the dictionary to the totalScrapedInformation list
    
print(totalScrapedInfo) # Display the list with all the information we scraped