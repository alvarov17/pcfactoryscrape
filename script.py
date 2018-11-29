import bs4
from urllib.request import urlopen as uReq
from bs4 import BeautifulSoup as soup

my_url = 'https://www.pcfactory.cl/'
uClient = uReq(my_url)
page_html = uClient.read()
uClient.close()

page_soup = soup(page_html, 'html.parser')


containers = page_soup.find_all("div", {"class": "wrap-caluga-matrix"})

#contain = containers[0]

for contain in containers:
    links = contain.find_all("div", {"class": "center-caluga"})[0].find_all("a",{"class": "noselect"})[0]
    titulo = links.find_all("span", {"class": "nombre"})[0].text
    precio = links.find_all("div", {"class" : "caluga-txt"})[0].find_all("span", {"class" : "txt-precio"})[0].text.replace(" ", "")

    print("producto: " + titulo + " | precio: " + precio)
    
    

