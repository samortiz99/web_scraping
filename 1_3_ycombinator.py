################################################## Hacker News ################################################# 
################################################################################################################
import requests
from bs4 import BeautifulSoup

headers = {
    "user-agent" : "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
}

url = "https://news.ycombinator.com/"

# verify=false se usa para evadir error por falta de SSL
respuesta = requests.get(url, headers=headers, verify=False)

soup = BeautifulSoup(respuesta.text)
'Para escribir expresiones en Xpath, después de hacer click en inspeccionar elemento se presiona ctrl + f'

notes_list = soup.find_all('tr', class_='athing')


score = 0
comentarios = 0

for notes in notes_list:
    title = notes.find('span', class_='titleline').text
    url = notes.find('span', class_='titleline').find('a').get('href')
    
    metadata = notes.find_next_sibling()
    
    try:
        score = metadata.find('span', class_='score').text
    except:
        print("No hay score")
        
    #	84 points by chillax 2 hours ago | hide | 45 comments
    try:
        comentarios = metadata.find('span', attrs={'class': 'subline'}).text
    # split toma la cadena y la separa por el valor "|", posteriormente selecciona último valor
        comentarios = comentarios.split('|')[-1]
    except:
        print("No hay comments")
    
    print(f'{title}\n{url}\n{score}\n{comentarios.strip()}\n\n')
    
    