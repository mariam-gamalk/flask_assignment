"""
Category model using SQLAlchemy ORM.
"""
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Category(db.Model):
    __tablename__ = 'category'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    products = db.relationship('Product', backref='category', lazy=True)

    def as_dict(self):
        """Return category instance as dictionary."""
        return {
            'id': self.id,
            'name': self.name
        }
