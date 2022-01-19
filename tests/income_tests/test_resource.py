from flask import url_for
from . import IncomeTest
from Finance.models.income import Income


class TestGetIncomes(IncomeTest):

    def test_should_return_list_of_incomes_given_get_request_without_id(self):
        response = self.client.get(
            url_for("incomes")
        )
        response_incomes = response.json
        db_incomes = Income.query.all()

        self.assertEqual(len(response_incomes), len(db_incomes))


class TestGetIncome(IncomeTest):

    def test_should_return_income_given_get_request_with_income_id(self):
        response = self.client.get(
            url_for("incomes", id=self.income.id)
        )
        income = response.json

        self.assertEqual(income["concept"], self.income.concept)
