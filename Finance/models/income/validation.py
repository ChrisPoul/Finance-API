class IncomeValidation:

    def __init__(self, income):
        self.income = income
        self.error = None

    def validate_concept(self):
        concept = self.income.concept.replace(" ", "")
        if concept.isalpha() is False:
            self.error = "El concepto solo puede contener letras"

        return self.error

    def validate_quantity(self):
        try:
            float(self.income.quantity)
        except ValueError:
            self.error = "El dinero tiene que ser un número valido"

        return self.error
