from flask_restful import Resource


class IncomeResource(Resource):

    def get(self, id=None):
        return None