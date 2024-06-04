################################################ STACK OVERFLOW ################################################ 
################################################################################################################
import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://www.stackoverflow.com/questions"

respuesta = requests.get(url, headers=headers)

# respuesta.text entrega la respuesta HTTP en cadena de texto || bs convierte el texto HTML en una estructura de Document Object Model (DOM). 
# soup almacenará todo lo que buscaré en la estructura HTML normalizada
soup = BeautifulSoup(respuesta.text)
soup

# .find relaciona el primer id "question" y trae todos sus descendientes <class 'bs4.element.Tag'>
contenedor_preguntas = soup.find(id="questions")
# .find_all relaciona una lista de tags con el mismo id y trae sus descendientes <class 'bs4.element.ResultSet'>
lista_preguntas = contenedor_preguntas.find_all('div', class_ = "s-post-summary")

#Al hacer .text en BeautifulSoup se traen todos los textos almacenados tanto en el tag llamado como en sus hijos

for preguntas in lista_preguntas:
    texto_pregunta = preguntas.find('h3', class_= "s-post-summary--content-title").text
    texto_pregunta = texto_pregunta.replace('\n', '').replace('\r', '').strip()
    descripcion_pregunta = preguntas.find('div', class_= 's-post-summary--content-excerpt').text
    descripcion_pregunta = descripcion_pregunta.replace('\n', '').replace('\r', '').strip()
    print(texto_pregunta)
    print(f'{descripcion_pregunta}, \n')
    
# En caso de no tener el id en las descripciones, se podrá acceder por medio de .find_next_sibling()
for i in lista_preguntas:
    text_element = i.find('h3', class_= 's-post-summary--content-title')
    text_ask = text_element.text.replace('\n', '').replace('\r', '').strip()
    
    descripcion_pregunta = text_element.find_next_sibling('div').text
    descripcion_pregunta = descripcion_pregunta.replace('\n', '').replace('\r', '').strip()
    
    print(text_ask)
    print(f'{descripcion_pregunta}, \n')
    
# Y así como se navega a los siblings también se puede navegar a hijos, etc