import peewee


db = peewee.SqliteDatabase('people.db')

def init():
    db.create_tables([Link, Email])

class Link(peewee.Model):
    link = peewee.CharField(unique=True)
    valid = peewee.BooleanField(default=False)

    class Meta:
        database = db

class Email(peewee.Model):
    Email = peewee.CharField(unique=True)

    class Meta:
        database = db