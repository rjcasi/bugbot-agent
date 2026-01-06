import requests
from bs4 import BeautifulSoup

def run_lab():
    print('Running Recon Expanded Lab...')
    url = 'https://example.com'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, 'html.parser')
    for link in soup.find_all('a'):
        print('Found link:', link.get('href'))