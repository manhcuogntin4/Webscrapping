
from models.gold import Gold

def search_golds(query):
    query = query.lower()
    print(query)
    golds = Gold.select().where(Gold.name.contains(query))
    print(golds)
    return golds
def search_gold(name):
    return  get_gold_by_name(name)


def get_gold_by_name(name):
    gold = Gold.get(name=name)
    gold_dic={}
    gold_dic['name']=gold.name
    gold_dic['url']=gold.url
    gold_dic['prix']=gold.prix
    #gold_dic['category']=gold.category
    return gold_dic

def create_gold(name, url, prix):
    gold = Gold.get_or_none(name=name)
    if gold is None:
        gold = Gold.create(name=name,url=url,prix=prix)
    else:
        gold.update(name=name,url=url,prix=prix).execute()

    return gold
