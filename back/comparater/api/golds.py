

from flask import request
from flask_restful import Resource

class Golds(Resource):
    def get(self):
        query = request.args['query']
        ors_matching = search_golds(query, type=None)
        return ors_matching


class Gold(Resource):
    def get(self,gold_name):
        return search_gold(gold_name)
