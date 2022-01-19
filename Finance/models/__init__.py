from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Model:

    def add(self):
        db.session.add(self)
        self.save()

    def save(self, **kwargs):
        for key, value in kwargs.items():
            setattr(self, attr, value)
        db.session.commit()

    def delete(self):
        db.session.remove(self)

    def validate(self):
        error = self.validation.validate()

        return error
