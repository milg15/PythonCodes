from bs4 import BeautifulSoup
from requests_html import HTMLSession
import pandas as pd
import urllib3

#just so it doesn't annoy me
print ("Pet Name")
pet_name = input()
urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
 
# create an HTML Session object
session = HTMLSession()
resp = session.get("https://www.wow-pets.com/realms/us/global", verify=False)
 
# Run JavaScript code on webpage
resp.html.render()
soup = BeautifulSoup(resp.html.html, "lxml")

pets_name = []
pets_price = []
pets_price25 = []
pets_source = []
pet_search = []
for row in soup.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==4: #Only extract table body not heading
        if pet_name.lower() == (cells[0].text).replace("\n", "").lower():
            pet_search = [(cells[0].text).replace("\n", ""), cells[1].text, cells[2].text]
        pets_name.append((cells[0].text).replace("\n", ""))
        pets_price.append(cells[1].text)
        pets_price25.append(cells[2].text)
        pets_source.append(cells[3].text)

dfGlobal=pd.DataFrame(pets_name ,columns=['Name'])
dfGlobal['Price']=pets_price
dfGlobal['Price(25)']=pets_price25
dfGlobal['Source'] = pets_source
dfGlobal

#now for velen
session = HTMLSession()
resp = session.get("https://www.wow-pets.com/realms/us/velen", verify=False)
 
# Run JavaScript code on webpage
resp.html.render()
soup = BeautifulSoup(resp.html.html, "lxml")

pets_name = []
pets_price = []
pets_price25 = []
pets_source = []
for row in soup.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==4: #Only extract table body not heading
        if pet_name.lower() == (cells[0].text).replace("\n", "").lower():
            pet_search.append(cells[1].text)
            pet_search.append(cells[2].text)
        pets_name.append((cells[0].text).replace("\n", ""))
        pets_price.append(cells[1].text)
        pets_price25.append(cells[2].text)
        pets_source.append(cells[3].text)

dfVelen=pd.DataFrame(pets_name ,columns=['Name'])
dfVelen['Price']=pets_price
dfVelen['Price(25)']=pets_price25
dfVelen['Source'] = pets_source
dfVelen 

if pet_search == []:
    print("Pet not found!")
else:
    print ("Pet-Name: ", pet_search[0])
    print ("Global: ", pet_search[1], pet_search[2])
    print ("Local: ", pet_search[3], pet_search[4])
