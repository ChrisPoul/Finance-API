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


class TestAddIncome(IncomeTest):

    def test_should_add_income_given_post_request_and_valid_income_form_in_json_format(self):
        income_form = dict(
            concept="Valid Concept",
            quantity="10"
        )
        self.client.post(
            url_for("incomes"),
            json=income_form
        )

        self.assertEqual(Income.query.count(), 2)

    def test_should_not_add_income_given_post_request_and_invalid_income_form_in_json_format(self):
        income_form = dict(
            concept="1nv@lid (0ncept",
            quantity=""
        )
        self.client.post(
            url_for("incomes"),
            json=income_form
        )

        self.assertEqual(Income.query.count(), 1)


class TestModifyIncome(IncomeTest):

    def test_should_modify_income_given_valid_changes_and_valid_income_form_in_json_format(self):
        income_form = dict(
            concept="New Valid Concept"
        )
        self.client.put(
            url_for("incomes", income_id=self.income.id),
            json=income_form
        )
        self.db.session.rollback()

        self.assertEqual(self.income.concept, income_form["concept"])

    def test_should_not_modify_income_given_invalid_changes_in_json_format(self):
        income_form = dict(
            quantity="invalid quantity"
        )
        prev_quantity = self.income.quantity
        self.client.put(
            url_for("incomes", income_id=self.income.id),
            json=income_form
        )
        self.db.session.rollback()

        self.assertEqual(self.income.quantity, prev_quantity)


class TestDeleteIncome(IncomeTest):

    def test_should_delete_income_given_delete_request_and_valid_income_id(self):
        self.client.delete(
            url_for("incomes", income_id=self.income.id)
        )

        self.assertNotIn(self.income, self.db.session)

    def test_should_return_not_delete_income_given_delete_request_and_invalid_id(self):
        response = self.client.delete(
            url_for("incomes", income_id=0)
        )

        self.assertIn(self.income, self.db.session)
