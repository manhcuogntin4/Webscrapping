from bs4 import BeautifulSoup
import urllib.request
from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import platform
import os
import sys
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
url3="https://wwws.airfrance.fr/search?connections=PAR:C:20190922%3EBOD:A-BOD:A:20190922%3EPAR:C&pax=1:0:0:0:0:0:0&sessionId=C33A980114E6F601F894BF64CD4DDF85.a68s2&market=fr_FR_fr&cabinClass=ECONOMY&bookingFlow=LEISURE&activeConnection=0"
url4="https://wwws.airfrance.fr/search?connections=PAR:C:20190925%3EBOD:A-BOD:A:20190925%3EPAR:C&pax=1:0:0:0:0:0&sessionId=C33A980114E6F601F894BF64CD4DDF85.a68s2&market=fr_FR_fr&cabinClass=ECONOMY&bookingFlow=LEISURE&activeConnection=0"
user_agent = 'Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:43.0)'
headers = {'User-Agent': user_agent}
chrome_options = Options()
chrome_options.add_argument("--no-sandbox")
chrome_options.add_argument('--ignore-certificate-errors')

chrome_options.add_argument('--headless')
def Driver(nav="chromium",options=None):
    nav=nav.capitalize()
    if nav=="Chromium":
        return (webdriver.Chrome("/snap/bin/chromium.chromedriver",options=options))
    if nav=="Firefox":
        return (webdriver.Firefox(options=options))
def getcontent(url):
    driver = Driver()
    driver.get(url)
    time.sleep(100)
    #soup = urllib.request.urlopen(url)
    cont = BeautifulSoup(driver.page_source, 'html.parser')

    return cont
def searchdeep(cont,tag,cla):
    try:
       mv = cont.find_all(tag,class_ = cla)
    except:
        mv=None
    return mv
def getprice(url):

    cont = getcontent(url)

    vg = cont.find_all("div")
    #mydivs = searchdeep(cont,"div","bw-flight-info-row qa-search-flight-info-row ng-star-inserte")

    for v in vg:
        try:
            cl=v["class"]
            print(cl)
        except:
           print("noclass")
    #print(mydivs)
    #print(len(mydivs))
    print(len(vg))
def searchword(word,content):
    found=re.findall(word,content.text)
    return (len(found)>0)

def searchterm(term):
    client=getdistrub()
    client=client.lower()
    urlterm="https://www.google.com/search?q={}&oq={}&aqs=chrome.0.69i59j0l5.1460j0j7&client={}&sourceid=chrome&ie=UTF-8".format(term,term,client)
    driver = Driver(options=chrome_options)

    driver.get(urlterm)
    time.sleep(60)
    cont = BeautifulSoup(driver.page_source, 'html.parser')
    divs =cont.find_all("div",class_="g",limit=10)
    for div in divs:
        link=div.a.get("href")
        print(link)
        for vt in div.div.find_all("div",class_="ellip"):
            print(vt.text)
        for sp in div.find_all("span",class_="st"):
            print(sp.text)
    print(driver.title,driver.name)
def getdistrub():
    try:
        client= platform.linux_distribution()
    except:
        client=None
    if client is not None:
        return client[0]
    return platform.system()
#getprice(url4)

#searchterm("prix or paris")

#dist=getdistrub()
#print(dist.lower())
def getcoursor():
    urlorparis="https://www.gold.fr/achat-or/"
    content = getcontent(urlorparis)
    divs=content.find_all("div", class_= "rsContent")


    for div in divs:
        titles = div.find_all("div", class_="title")
        prices=div.find_all("div",class_="prix")
        tprice={}
        for b in range(len(titles)):
            tprice[titles[b].text]=prices[b].text
        print(tprice)
def gettables(content):
    tables = content.find_all("table")
    return tables
def getheaders(table):
    texts=[]
    th=None
    try:
      th=table.thead.find_all("th")
    except:
        pass
    if th !=None:
         for t in th:
             text=t.text
             if text in texts:
                 text=text+"2"
             texts.append(text)

    return(texts,th)
def trheaders(tr):
    headers = []
    if tr!=None:
        try:
            th = tr.find_all("th")
        except:
            th=None
        if th != None:
            for t in th:
                text=t.text
                if text in headers:
                    text = text + "2"
                headers.append(text)
    return headers

def gettr(tab):
    tr=tab.find_all("tr")
    return tr
#put a given table row to a dictionnary
def gettdtextorimg(td):
    texts=[]
    try :
        text=td.text
    except:
        text=""
    if text=="":
        try:
           imgs= td.find_all("img")
        except:
            imgs =[]
            print(imgs)
        if len(imgs)>0:
            for img in imgs:
              texts.append(img["src"])
    else:
        return (text)
    if len(texts)>0:
        return texts[0]
    return ("")

def trtodict(tr,tab):
    if trheaders(tr)!=[]:
       th = trheaders(tr)
    else:
        th=getheaders(tab)[0]
    p={}

    tds=tr.find_all("td")
    if len(tds)>0:
        m =len(tds)-len(th)
        if m >0:
           for i in range(m):
               th=[str(i)]+th
        if m<0:
            for i in range(-m):
                tds = [str(i)] + tds

        for td in range(len(th)):
              p[th[td]]=gettdtextorimg(tds[td])
    return p
#drop key with whites spaces value
def cleandict(d):
    if d!=None:
        newd = {key.strip(" \n\t"):d[key].strip(" \n\t") for key in d.keys()}

        return(newd)
#filter tables  containing some key words and drop them
def cleantables(tables):
    blacklist=["cookies" ,"Cookies","cookie","HTTP"]

    clean = [t for t in tables if any([searchword(w,t) for w in blacklist])==False and t!={}]
    return (clean)
#return a cotation for a given url
def getcotation(urlcours):
    print(urlcours)
    content = getcontent(urlcours)
    tables = cleantables(content.find_all("table"))
    tablecontents=[]
    for tab in tables:
        trlist=[]
        trs=gettr(tab)
        for tr in trs:
            p=cleandict(trtodict(tr,tab))
            if p!={}:
             trlist.append(p)

        tablecontents.append(trlist)
    print (tablecontents[0])
    return tablecontents
def geteuropiece(uri):
    content = getcontent(uri)
    print(uri)
    divs=content.find_all("div", class_= "euro_line")
    headers=["name","poids","price"]
    cotation=[]
    for div in divs:
        spans=div.find_all("span")
        images=div.find_all("img")
        p={}
        p["image"]=images[0]["src"]
        for i in range(len(headers)):
          p[headers[i]]=spans[i].text
        if p!={}:
          cotation.append(p)

    return [cotation]
def getcategory(name):
    category ="Lingotin" if "Lingotin" in name else ("Lingot" if "Lingot" in name else "piece")
    return category

class Website:
    def __init__(self,uri,naming, poids="",image="" ,getcot=None):
        self.uri=uri
        self.naming=naming
        self.poids=poids
        self.image=image
        self.getcot = getcot
        self.content=self.getlisting()
    def getlisting(self):
        p=eval("self.getcot(self.uri)")
        print(p[0])
        return(p[0])

    @property
    def staticdata(self):
        data=[]
        for cont in self.content:
             p={}
             p["name"]=cont[self.naming]
             p["category"]=getcategory(p["name"])
             p["poids"]=cont[self.poids]
             p["image"]=cont[self.image]
             data.append(p)
        return(data)

goldfruri="https://www.gold.fr/cours-or-prix-de-l-or/"

cdturi="https://www.cdt.fr/or/bourse-cours/cours.html"
bullionvaulturi="https://www.bullionvault.com/gold-price-chart.do"
goldmarketuri="https://www.goldmarket.fr/s/"
europieceuri="https://www.europiecedor.fr/cours-piece-achat-or/"
getcotation(cdturi)
#getcotation(bullionvault)
#europiece=Website(europieceuri,"name","category" ,"poids","image",geteuropiece)
#print(europiece.staticdata)
cdt=Website(cdturi,"Pièces ou Lingots d'Or","Poids net","0",getcotation)
print(cdt.staticdata)
searchterm("achat or paris")
