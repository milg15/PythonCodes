from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import pandas as pd
import time
import re

def scroll(driver, timeout):
    scroll_pause_time = timeout
    last_height = driver.execute_script("return document.body.scrollHeight")

    while True:
        # Scroll down to bottom
        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        # Wait to load page
        time.sleep(scroll_pause_time)
        # Calculate new scroll height and compare with last scroll height
        new_height = driver.execute_script("return document.body.scrollHeight")
        if new_height == last_height:
            # If heights are the same it will exit the function
            break
        last_height = new_height

def get_links_to_categories(home_url, driver):
    driver.find_element_by_xpath("//div[@class='Header__dropdown__text'][text()='Supermercado']").click()
    time.sleep(2)

    soup = BeautifulSoup(driver.page_source, "html.parser")
    table = soup.find_all('li', class_='MainMenu__category__item')
    urls = []

    import unidecode
    for t in table:
        t = unidecode.unidecode(t.text.replace(",", "").replace(" ", "-"))
        url = home_url + t
        urls.append(url)
    return urls

def get_item(soup):
    item = {}
    sku = soup.find('div', class_='productReference')
    if not sku:
        return item

    item['SKU'] = sku.text
    precio = precio = soup.find('div', class_='ProductCard__price--online').find('div', class_="ProductCard__content__price")
    precio = precio.text.replace("s/ ", "")
    item['Precio'] = precio if float(precio) else ""
    item['Titulo'] = soup.find('span', class_='ProductCard__brand').text
    item['Imagen'] = soup.find(id='image-main')['src']
    item['Descripcion'] =   soup.find('div', class_='productName').text

    cat_headers = ['Categoria', 'Subcategoria']
    cat_elem = soup.find('div', class_='ProductCard__breadCrumb').find_all('li')[1:]

    for i, cat in enumerate(cat_elem):
        c = 0 if not i else 1
        header = cat_headers[c] + " " + (str(i) if i else "")

        item[header] = cat.text

    return item

def agregar_productos(prod_elems, driver, products):
    items = []
    for prod_elem in prod_elems:
        # Each prod_elem is a new BeautifulSoup object.

        url = prod_elem.find('a', class_='Showcase__name')['href']
        driver.get(url)    

        soup = BeautifulSoup(driver.page_source, "html.parser")

        items.append(get_item(soup))

    return items

def go_through_category(url, driver):
    regex = re.compile('pagecount_([0-9]*)')

    driver.get(url)
    scroll(driver, 4)
    time.sleep(5)
    
    soup = BeautifulSoup(driver.page_source, "html.parser")
    ids = regex.findall(str(soup))[0]
    page_id = 'ResultItems_' + ids

    product_container = soup.find(id=page_id)
    prod_elems = product_container.find_all('div', class_='g-producto')
    
    print(url, len(prod_elems))

    return prod_elems
 
    
def main():
    driver = webdriver.Chrome(ChromeDriverManager().install())
    home_url = 'https://www.plazavea.com.pe/'
    driver.get(home_url)
    driver.implicitly_wait(100)

    categories_url = get_links_to_categories(home_url, driver)[1:]
    
    products = []
    for c_url in categories_url:
        prod_elems = go_through_category(c_url, driver)
        category_products = agregar_productos(prod_elems, driver, products)
        products.extend(category_products)

        #testing
        df = pd.DataFrame(category_products)
        print(df)
        path = c_url.replace(home_url, "") + '.xlsx'
        df.to_excel (r'C:\Users\Diego\Desktop\\' + path, index = False, header=True)

    df = pd.DataFrame(products)
    df.to_excel (r'C:\Users\Diego\Desktop\products.xlsx', index = False, header=True)

    driver.close()
    driver.quit()

if __name__ == "__main__":
    main()
