from peewee import *

from .database import db


class Gold(Model):
    id = PrimaryKeyField()
    name = CharField()
    url = CharField()
    prix=FloatField()
    class Meta:
        database = db
        schema = 'public'

    def get_small_data(self):
        return {'name': self.name, 'url': self.url, 'prix': self.prix}


with db:
    Gold.create_table(fail_silently=True)

class Shop(Model):
    id=PrimaryKeyField()
    url=CharField()
    name=CharField()
    class Meta:
        database=db
        schema='public'
    def get_small_data(self):
        return {'name': self.name, 'url': self.url}

with db:
    Shop.create_table(fail_silently=True)