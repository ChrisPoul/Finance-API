from flask import request
from flask_restful import (
    Resource, marshal_with, fields
)
from Finance.models.income import Income

income_fields = dict(
    id=fields.Integer,
    concept=fields.String,
    quantity=fields.Integer,
    datetime=fields.DateTime
)


class IncomeResource(Resource):

    @marshal_with(income_fields)
    def get(self, income_id=None):
        if income_id:
            return Income.query.get(income_id)
        else:
            return Income.query.all()

    def post(self):
        income_form = request.get_json()
        income = Income(**income_form)
        error = income.validate()
        if not error:
            income.add()

        return error

    def put(self, income_id: int):
        form = request.get_json()
        income = Income.query.get(income_id)
        income.modify(**form)
        error = income.validate()
        if not error:
            income.save()
        
        return error

    def delete(self, income_id: int):
        income = Income.query.get(income_id)
        if income:
            income.delete()
