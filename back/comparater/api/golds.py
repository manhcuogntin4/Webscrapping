from flask import request
from flask_restful import Resource
from json import JSONEncoder
from comparater.managers.golds import search_golds,search_gold,delete_gold
class Golds(Resource):
    def get(self):
        query = request.args['query']
        ors_matching = search_golds(query, type=None)
        return ors_matching


class Gold(Resource):
    def get(self,gold_name):
        return search_gold(gold_name)

    def delete(self, gold_name):
        result = delete_gold(gold_name)
        return result
