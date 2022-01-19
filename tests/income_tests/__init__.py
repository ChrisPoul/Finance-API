from tests import Test
from Finance.models.income import Income


class IncomeTest(Test):

    def setUp(self):
        Test.setUp(self)
        self.income = Income(
            concept="Test Income",
            quantity=1000
        )
        self.income.add()
