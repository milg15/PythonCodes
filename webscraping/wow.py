from bs4 import BeautifulSoup
import requests
import urllib3

urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)
#import lxml.html as lh
import pandas as pd
from requests_html import HTMLSession
 
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
#from selenium import webdriver
#from selenium.webdriver.chrome.options import Options

"""chrome_options = Options()  
chrome_options.add_argument("--headless")  
driver = webdriver.Chrome(chrome_options=chrome_options)
driver.get("https://www.wow-pets.com/realms/us/global")

for tr in driver.find_elements_by_tag_name("tr"):
    for td in tr.find_elements_by_tag_name("td"):
        print(td.get_attribute("innerText"))"""

#url = "https://www.wow-pets.com/realms/us/global"
#response = requests.get(url, timeout=5)
#content = BeautifulSoup(response.content, "html.parser")


#header_petprice =  content.find('table', attrs={"class": "pet-values"}).text;
#doc = lh.fromstring(response.content)
#tr_elements = doc.xpath('//table[@class="pet-values"]/tbody/tr')
"""file = open('Failed.txt', 'w')
file.write(str(content))
file.close()"""

print('done')


"""resp = requests.get("https://www.wow-pets.com/realms/us/global")
 
html = resp.content
soup = BeautifulSoup(html)
 
option_tags = soup.find_all("tr")"""
