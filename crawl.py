import requests
from bs4 import BeautifulSoup

r = requests.get("https://www.immobilienscout24.de/Suche/S-T/Wohnung-Kauf/Berlin/Berlin/-/1,50-?enteredFrom=one_step_search")
doc = BeautifulSoup(r.text, "html.parser")


for tempcont in doc.select(".grid .grid-flex"):
    for cont1 in tempcont.select(".grid-item .result-list-entry__data-container"):
        with open("test.txt", 'w') as x:
            x.write(tempcont.prettify())
        allVar = cont1.select(".grid-item .result-list-entry__primary-criterion .font-line-xs")
        if allVar[0].text.find("-") >= 0:
            #Preise  zurecht schneiden die mit Bindestrich getrennt sind
            print("IF")
            tempstr = allVar[0].text.replace(" ","")
            tempstr = tempstr.replace("€","")
            tempstr = tempstr.replace(".","")
            #Hier Werte in DB übergeben o.ä.
            price0 = int(tempstr[:tempstr.find("-")-1])
            price1 = int(tempstr[tempstr.find("-")+1:])
            print("Preis von: ", price0)
            print("Preis bis: ", price1)
        else:
            #Preis zurechtschneiden
            print("ELSE")
            tempstr = allVar[0].text.replace(" ","")
            tempstr = tempstr.replace("€","")
            tempstr = tempstr.replace(".","")
            #Hier Wert in DB übergeben o.ä.
            price0 = int(tempstr)
            print("Preis: ", int(tempstr))
        if allVar[1].text.find("-") >= 0:
            #Kannst du dir denken du Schwuchtel
            tempqm = allVar[1].text.replace(",",".")
            tempqm = tempqm.replace("m²","")
            qm0 = float(tempqm[:tempqm.find("-")-1])
            qm1 = float(tempqm[tempqm.find("-")+1:])
            print ("Flaeche von: ", qm0 ," m²")
            print ("Flaeche bis: ", qm1 ," m²")
        else:
            tempqm = allVar[1].text.replace(",",".")
            qm = float(tempqm.replace("m²",""))
            print ("Flaeche:", qm ," m²")
        break
    for cont2 in tempcont.select(".grid-item .result-list-entry__gallery-container"):
        templink = cont2.select_one("a")
        templink = templink.attrs["href"]
        if templink.find("/expose/") >= 0:
            link = ("https://www.immobilienscout24.de"+templink)
        else:
            link = templink
        print(link)
        break
    