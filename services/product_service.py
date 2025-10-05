"""
Service for product operations using SQLAlchemy ORM.
"""
from models.product import Product, db


def get_all_products():
    """Return all products."""
    products = Product.query.all()
    return [p.as_dict() for p in products]


def get_product_by_id(product_id):
    """Return product by ID."""
    product = Product.query.get(product_id)
    return product.as_dict() if product else None


def get_products_by_category(category_id):
    """Return products by category ID."""
    products = Product.query.filter_by(category_id=category_id).all()
    return [p.as_dict() for p in products]


def create_product(data):
    """Create a new product."""
    product = Product(
        name=data['name'],
        price=data['price'],
        quantity=data['quantity'],
        img_url=data.get('img_url'),
        category_id=data['category_id']
    )
    db.session.add(product)
    db.session.commit()
    return product.id


def update_product(product_id, data):
    """Update product by ID."""
    product = Product.query.get(product_id)
    if not product:
        return False
    product.name = data['name']
    product.price = data['price']
    product.quantity = data['quantity']
    product.img_url = data.get('img_url')
    product.category_id = data['category_id']
    db.session.commit()
    return True


def delete_product(product_id):
    """Delete product by ID."""
    product = Product.query.get(product_id)
    if not product:
        return False
    db.session.delete(product)
    db.session.commit()
    return True