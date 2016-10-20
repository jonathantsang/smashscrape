# import libraries
import urllib2  
from bs4 import BeautifulSoup  
import requests
import csv  
import sys
from datetime import datetime  

quote_page = "https://smash.gg/tournament/smash-summit-3/voting"

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)  

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the value
count =  soup.find_all(['small']) 
name = soup.find_all("div", { "class" : "gamertag-title-lg"})

print count
print name

co = []
na = []

for c in count:
    co.append(c)
for n in name:
    na.append(n)
    
print co[0]
print na[1]

# File Writing
ofile  = open('ttest.csv', "wb")
writer = csv.writer(ofile, delimiter='	', quotechar='"', quoting=csv.QUOTE_ALL)

for row in co:
    writer.writerow(row)
for row in na:
    writer.writerow(row)

ofile.close()
