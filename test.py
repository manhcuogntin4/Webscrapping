from bs4 import BeautifulSoup
import urllib.request
import re
url="https://www.prix-or.fr/or/pieces-d-or/"
soup=urllib.request.urlopen(url)
content= BeautifulSoup(soup, 'html.parser')
class website:
     pass
headers = content.body.find_all("a",href="cours-de-l-or/")
head1=content.find_all("title")
print (head1)
for link in headers:
    #b=link.body.find_all("span")
    #print(b.text)
    b=link.span
    if b:
          print(b.text)


url2="https://fr.yahoo.com/"
url3="https://wwws.airfrance.fr/search?connections=PAR:20190923%3EBOD:A-BOD:A%3EPAR&pax=1:0:0:0:0:0&sessionId=A9D7403148A1BFE010FD11DBDE2AC5D8.a68s2&market=fr_FR_fr&cabinClass=ECONOMY&bookingFlow=LEISURE&activeConnection=0"

user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0)'
headers = {'User-Agent': user_agent}
def getcontent(url):
    soup = urllib.request.urlopen(url,heder=headers)
    content = BeautifulSoup(soup, 'html.parser')
    print(content.title)
    return content
def getprice(url):
    content=getcontent(url)
    print(content.title)
    pricerow = content.find_all("div","class:bw-flight-info-row qa-search-flight-info-row ng-star-inserted")
    print(pricerow)

getprice(url3)
