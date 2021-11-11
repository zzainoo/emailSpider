#!/usr/bin/python3
import re
import bs4
import requests
import threading
from db import *
from ds import Queue
import time
import logging

email_regex = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
init()
data = Queue()
print("script is running .........")
print("By zzainoo !")
time.sleep(3)
logging.basicConfig(filename="/home/zano/emailSpider/app.log", level=logging.INFO)

def extractLinks():
    try:
        for x in data.get():
            req = requests.get(x)
            res = bs4.BeautifulSoup(req.text, "html.parser")
            extractEmail(req.text)
            for link in res.find_all('a', href=True):
                data.add(link['href'])
    except:
        extractLinks()

def extractEmail(res):
    res = re.findall(email_regex,res)
    for x in res:
        insertEmailDb(x)

def insertEmailDb(email):
    try:
        Email.create(Email=email)
        print(email + '-----------> EXTRACTED!!!')
        logging.info(email + '--------> EXTRACTED!!!')
    except peewee.IntegrityError:
        pass





threads = []


t1 = threading.Thread(target=extractLinks)
t2 = threading.Thread(target=extractLinks)
t3 = threading.Thread(target=extractLinks)
t4 = threading.Thread(target=extractLinks)

threads.append(t1)
threads.append(t2)
threads.append(t3)
threads.append(t4)

for x in threads:
    x.start()



