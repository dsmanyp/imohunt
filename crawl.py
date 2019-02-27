import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.immobilienscout24.de/Suche/S-T/Wohnung-Kauf/Berlin/Berlin/-/1,50-?enteredFrom=one_step_search")
doc = BeautifulSoup(r.text, "html.parser")

#print (doc)

for cont in doc.select(".grid-item .result-list-entry__data-container"):
    #print(cont)
    link = cont.select(".font-s .href")
    print(link)
    allVar = cont.select(".grid-item .result-list-entry__primary-criterion .font-line-xs")
    print(allVar)
    print ("Preis: ",allVar[0].text)
    print ("Flaeche: ", allVar[1].text )
    
    #print(link.attrs["href"])
    break