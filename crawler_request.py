import requests
import time
from bs4 import BeautifulSoup

session = requests.Session()

dados = {'Username':'Olivia','Password':'123'}
req = requests.post('http://201.6.1.17/net2/login.asp',data = dados)


#soup = BeautifulSoup(req.text, 'html.parser')
#print(soup.prettify)