#web scrap for the website https://www.freejobalert.com/police-defence-jobs/ and get the latest job details

import requests
from bs4 import BeautifulSoup
import smtplib
import time

URL = 'https://www.freejobalert.com/police-defence-jobs/'
if __name__ == '__main__':
    while True:
        headers = {"User-Agent": 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.116 Safari/537.36'}
        page = requests.get(URL, headers=headers)
        # print(page)
        soup = BeautifulSoup(page.content, 'html.parser')
        # print(soup)
        content = soup.find(class_="table")
        print(content)
    