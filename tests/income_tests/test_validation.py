from . import IncomeTest


class TestValidateConcept(IncomeTest):

    def test_should_not_return_error_given_alphabetical_characters_and_spaces_in_concept(self):
        self.income.concept = "Valid Concept"
        error = self.income.validation.validate_concept()

        self.assertEqual(error, None)

    def test_should_return_error_given_non_alphabetic_characters_in_concept(self):
        self.income.concept = "1inval1d c0n(cept"
        error = self.income.validation.validate_concept()
        
        self.assertNotEqual(error, None)

    def test_should_return_error_given_empty_string_as_quantity(self):
        self.income.concept = ""
        error = self.income.validation.validate_concept()

        self.assertNotEqual(error, None)


class TestValidateMoney(IncomeTest):

    def test_should_not_return_error_given_integer_quantity(self):
        self.income.quantity = "111"
        error = self.income.validation.validate_quantity()

        self.assertEqual(error, None)

    def test_should_not_return_error_given_float_quantity(self):
        self.income.quantity = "20.5"
        error = self.income.validation.validate_quantity()

        self.assertEqual(error, None)

    def test_should_return_error_given_non_numerical_characters_in_quantity(self):
        self.income.quantity = "ll"
        error = self.income.validation.validate_quantity()

        self.assertNotEqual(error, None)

    def test_should_return_error_given_empty_string_as_quantity(self):
        self.income.quantity = ""
        error = self.income.validation.validate_quantity()

        self.assertNotEqual(error, None)
