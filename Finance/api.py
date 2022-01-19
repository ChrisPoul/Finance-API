from flask_restful import Api
from .resources.income import IncomeResource

api = Api(prefix="/finance")

api.add_resource(
    IncomeResource,
    '/incomes',
    '/incomes/<int:id>',
    endpoint="incomes"
)