"""
Service for category operations using SQLAlchemy ORM.
"""
from models.category import Category


def get_all_categories():
    """Return all categories."""
    categories = Category.query.all()
    return [c.as_dict() for c in categories]