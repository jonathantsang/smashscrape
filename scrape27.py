# import libraries
import urllib2  
from bs4 import BeautifulSoup  
import csv  
from datetime import datetime  

quote_page = "https://smash.gg/tournament/smash-summit-3/voting"

# query the website and return the html to the variable 'page'
page = urllib2.urlopen(quote_page)  

# parse the html using beautiful soap and store in variable `soup`
soup = BeautifulSoup(page, 'html.parser')

# Take out the value
count =  soup.find_all("small", { "class" : "text-muted"})
name = soup.find_all("div", { "class" : "gamertag-title-lg"})

print count
print name

co = []
na = []

for c in count:
    co.append(c.get_text())
for n in name:
    na.append(n.get_text())
    
print co[0]
print na[1]

f = open('test.csv', 'wb')
#out = csv.writer(f, delimiter=",")
#i = 0
#while(i < len(co)):
#    print co[i]
#    print na[i]
#    out.writerow([co[i], na[i], datetime.time])
#    i += 1
f.close()