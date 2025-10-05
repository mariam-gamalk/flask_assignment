"""
Product model using SQLAlchemy ORM.
"""
from models.category import db


class Product(db.Model):
    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    price = db.Column(db.Float, nullable=False)
    quantity = db.Column(db.Integer, nullable=False)
    img_url = db.Column(db.String(255))
    category_id = db.Column(db.Integer, db.ForeignKey('category.id'))

    def as_dict(self):
        """Return product instance as dictionary."""
        return {
            'id': self.id,
            'name': self.name,
            'price': self.price,
            'quantity': self.quantity,
            'img_url': self.img_url,
            'category_id': self.category_id
        }