from bs4 import BeautifulSoup
from requests_html import HTMLSession
import pandas as pd
import urllib3

#just so it doesn't annoy me
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
for row in soup.findAll("tr"):
    cells = row.findAll('td')
    states=row.findAll('th') #To store second column data
    if len(cells)==4: #Only extract table body not heading
        pets_name.append((cells[0].text).replace("\n", ""))
        pets_price.append(cells[1].text)
        pets_price25.append(cells[2].text)
        pets_source.append(cells[3].text)

df=pd.DataFrame(pets_name ,columns=['Name'])
df['Price']=pets_price
df['Price(25)']=pets_price25
df['Source'] = pets_source
df

print (df)
