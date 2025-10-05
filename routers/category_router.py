"""
Category router.
"""
from flask import Blueprint, jsonify
from services.category_service import get_all_categories

category_bp = Blueprint('category_bp', __name__)


@category_bp.route('/categories', methods=['GET'])
def get_categories():
    """
    Get all categories.
    Returns:
        Response: JSON response with success and results.
    """
    categories = get_all_categories()
    return jsonify({
        'success': True,
        'results': categories
    })