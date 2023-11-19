import pandas as pd

import re
import time
import os
from urllib.parse import urlparse

import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By


def fix_url(curr, target):
    if target[0] == '/':
        return 'https://' + urlparse(curr).netloc + target
    else:
        return target

def try_download(url, path):
    # print(url)
    response = requests.get(url, allow_redirects=True)

    if response.headers.get('content-type') in ['application/pdf', 'application/pdf;charset=UTF-8']:
        path = os.path.join(path, url.rsplit('/', 1)[-1])
        # print(path)
        open(path, 'wb').write(response.content)
        print('OK', url.rsplit('/', 1)[-1])
        return True
    else:
        print(':(', url)
        return False
    
if __name__ == "__main__":

    df = pd.read_csv('banki.csv')
    search_result = []
    bank_name = 'Bank Handlowy w Warszawie SA'

    for index, row in df[df['Bank'] == bank_name].iterrows():
        response = requests.get(row['Link'])
        soup = BeautifulSoup(response.text, 'html.parser')
        links = soup.find_all('a', href=True)
        search_result.append([row['Bank'], []])
        for link in links:
            try:
                href = link['href']
                html = str(link)
                if re.search('lokat', link['title'], re.IGNORECASE) and re.search('konto', link['title'], re.IGNORECASE):
                    url = fix_url(row['Link'], href)
                    if try_download(url, f'../downloads/{bank_name}'):
                        search_result[-1][1].append(href)
            except:
                pass