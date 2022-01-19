from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Model:

    def add(self):
        db.session.add(self)
        self.save()

    def modify(self, **kwargs):
        for attr, value in kwargs.items():
            setattr(self, attr, value)

    def save(self):
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        self.save()

    def validate(self):
        error = self.validation.validate()

        return error
