################################################ STACK OVERFLOW ################################################ 
################################################################################################################
import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://www.stackoverflow.com/questions"

respuesta = requests.get(url, headers=headers)

soup = BeautifulSoup(respuesta.text)
soup

contenedor_preguntas = soup.find(id="questions")
contenedor_preguntas.find_all(class_ = "question-summary")
# contenedor_preguntas.

