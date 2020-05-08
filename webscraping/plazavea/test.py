from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

from bs4 import BeautifulSoup
import time
import re

driver = webdriver.Chrome(ChromeDriverManager().install())
url = 'https://www.plazavea.com.pe/abarrotes/conservas'

"""for prod_elem in prod_elems:
    # Each prod_elem is a new BeautifulSoup object.
    # You can use the same methods on it as you did before.
    price_elem = prod_elem.find('div', class_='Showcase__salePrice')
    
    if price_elem:
        #driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
        link = prod_elem.find('a', class_='Showcase__name')['href']
        driver.get(link)    
        time.sleep(5)
        
        soup = BeautifulSoup(driver.page_source, "html.parser")
        price = price_elem.find('span', class_='price')['data-price']
        img_elem = soup.find(id='image-main')
        title_elem = soup.find('div', class_='productName')
        sku_elem = soup.find('div', class_='productReference')
        descripcion = soup.find(id='caracteristicas')
        print(descripcion.text)
        
        #print(prod_elem)
        f.write("SKU" + sku_elem.text + "  Title: " + title_elem.text+"\n")
        f.write("Price: " + price+"\n")
        f.write("link: " + img_elem['src'])
        f.write("Descripcion: " + descripcion.text)
        f.write("\n\n")
        #driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w') 
        #go into link """


#prod_elem = prod_elems[1]
#f=open("soup.txt","w+")

if True:
    #driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 't') 
    driver.get("https://www.plazavea.com.pe/yuca-amarilla-precocida-green-food-bolsa-400g/p")    
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    precio = soup.find('div', class_='ProductCard__price--online').find('div', class_="ProductCard__content__price")
    precio = precio.text.replace("s/ ", "")
    img_elem = soup.find(id='image-main')
    title_elem = soup.find('div', class_='productName')
    sku_elem = soup.find('div', class_='productReference')
        
    print("SKU" + sku_elem.text + "  Title: " + title_elem.text)
    print("Price: ")
    print(precio if float(precio) else "")
    print("link: " + img_elem['src'])
    #driver.find_element_by_tag_name('body').send_keys(Keys.CONTROL + 'w') 
    #go into link 

driver.close()
driver.quit()
