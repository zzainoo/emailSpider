import validators
from db import *

class Queue:
    def __init__(self):
        init()
        self.data = []
        for x in Link.select():
            if x.valid == False:
                self.add(x.link)

    def add(self,link):
        if validators.url(link):
            self.insertDb(link)
            self.data.append(link)

    def get(self):
        for x in self.data:
            link = self.data.pop(0)
            self.updateDb(link)
            yield link

    def insertDb(self,link):
        try:
            Link.create(link=link)
        except peewee.IntegrityError:
            pass

    def updateDb(self,link):
        linkdb = Link.select().where(Link.link == link).get()
        if True:
            linkdb.valid = True
            linkdb.save()




