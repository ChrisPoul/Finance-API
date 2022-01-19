from Finance.models import db, Model
from sqlalchemy import (
    Column, Integer, String, DateTime
)
from sqlalchemy.sql import func


class Income(db.Model, Model):
    id = Column(Integer, primary_key=True)
    concept = Column(String(100), nullable=False)
    quantity = Column(Integer, nullable=False)
    datetime = Column(DateTime, server_default=func.now())

    @property
    def validation(self):
        from .validation import IncomeValidation
        return IncomeValidation(self)