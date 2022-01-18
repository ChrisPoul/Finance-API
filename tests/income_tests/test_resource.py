from . import IncomeTest
from Finance.models.income import Income


class TestValidateConcept(IncomeTest):

    def test_should_not_return_error_given_valid_concept(self):
        self.income.concept = "Valid Concept"
        error = self.income.validation.validate_concept()

        self.assertEqual(error, None)