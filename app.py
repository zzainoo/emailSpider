import re
import bs4
import requests
import threading
from db import *
from ds import Queue
import time

email_regex = '[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}'
init()
data = Queue()
print("script is running .........")
print("By zzainoo !")
time.sleep(3)

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
    except peewee.IntegrityError:
        pass


class Thread (threading.Thread):
   def __init__(self):
      threading.Thread.__init__(self)
   def run(self):
      extractLinks()

t1 = Thread()
t2 = Thread()
t3 = Thread()
t4 = Thread()

t1.start()
print("thread 1 started")
t2.start()
print("thread 2 started")
t3.start()
print("thread 3 started")
t4.start()
print("thread 4 started")
