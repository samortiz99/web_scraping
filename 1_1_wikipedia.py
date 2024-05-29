################################################### WIKIPEDIA ################################################## 
################################################################################################################
import requests
from lxml import html


# Pendiente por definir bien que es esto
encabezados = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

# Enlace página a scrapear
url = "https://www.wikipedia.org"

# Para traer árbol / estructura HTML <Response [200]> || para visualizar árbol se agrega .text
respuesta = requests.get(url, headers=encabezados)
respuesta
respuesta.text

# De la librería lxml, se exporta html, se guarda la estructura del html en la variable parser  
# Se accede solo al contenido del HTML con .text_content()
parser = html.fromstring(respuesta.text)
parser
parser.text_content()

# get_element_by_id es función de la librería lxml
ingles = parser.get_element_by_id("js-link-box-en")
print(ingles.text_content())

# Para buscar con xpath de la librería lxml
parser.xpath("//a[@id='js-link-box-en']/*[1]/text()")

# Devuelve lista y solo se puede acceder con un for
idioma = parser.find_class("central-featured-lang")
for i in idioma:
    print(i.text_content())

idiomas1 = parser.xpath("//a[contains(@id, 'js-link-box-')]/strong/text()")
idiomas1

idiomas2 = parser.xpath("//div[contains(@class, 'central-featured-lang')]//strong/text()")
idiomas2

for i in idiomas1:
    print(i)
