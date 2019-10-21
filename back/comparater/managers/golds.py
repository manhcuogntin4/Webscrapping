import requests
from comparater.models.gold import Gold
import csv
from json import JSONEncoder


def search_golds(query):
    query = query.lower()
    print(query)
    golds = Gold.select().where(Gold.name.contains(query))
    golds = [gold.get_small_data() for gold in golds]
    return golds


def search_gold(name):
    #Test
    return get_gold_by_name(name)


def get_gold_by_name(name):
    print(name)
    gold = Gold.get_or_none(Gold.name == name)
    gold_dic = {}
    if gold is not None:
        print(gold.name)
        gold_dic['name'] = gold.name
        gold_dic['url'] = gold.url
        gold_dic['prix'] = gold.prix
    return gold_dic

def get_gold(name):
    gold = Gold.get_or_none(Gold.name == name)
    return gold

def create_gold(name, url, prix):
    gold = Gold.get_or_none(name=name)
    if gold is None:
        gold = Gold.create(name=name, url=url, prix=prix)
    else:
        gold.update(name=name, url=url, prix=prix).execute()

    return gold


def delete_gold(name):
    gold = Gold.get_or_none(Gold.name == name)
    gold.delete_instance(recursive=True)
    return True


def edit_gold_prix(name, prix):
    gold = get_gold_by_name(name)
    gold.prix = prix
    gold.save()

    return gold


def load_gold_from_csv():
    with open('back/comparater/models/golds.csv', newline='') as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            create_gold(row['name'],row['url'],row['prix'])


def update_gold(name,stats):
    gold = get_gold(name)
    gold.update_stats(stats)
    n=gold.save()
    return gold
