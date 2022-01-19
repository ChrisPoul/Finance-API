from flask import url_for
from . import IncomeTest
from Finance.models.income import Income


class TestGetIncomes(IncomeTest):

    def test_should_return_list_of_incomes_given_get_request_without_income_id(self):
        response = self.client.get(
            url_for("incomes")
        )
        incomes = response.json

        self.assertEqual(len(incomes), Income.query.count())


class TestGetIncome(IncomeTest):

    def test_should_return_income_given_get_request_with_income_id(self):
        response = self.client.get(
            url_for("incomes", income_id=self.income.id)
        )
        income = response.json

        self.assertEqual(income["concept"], self.income.concept)


# class TestAddIncome(IncomeTest):

#     def test_should_add_income_given_post_request_and_valid_income_form_in_json_format(self):
#         income_form = dict(
#             concept="Valid Concept",
#             quantity="Valid Quantity"
#         )
#         self.client.post(
#             url_for("incomes"),
#             json=income_form
#         )
#         income = Income.query.all()[-1]

#         self.assertEqual(income.concept, income_form['concept'])
