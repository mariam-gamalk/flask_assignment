
"""
Product router.
"""
from flask import Blueprint, request, jsonify
from services.product_service import (
    get_all_products, get_product_by_id, get_products_by_category,
    create_product, update_product, delete_product
)

PRODUCT_NOT_FOUND_MSG = 'Product not found'
product_bp = Blueprint('product_bp', __name__)


@product_bp.route('/products', methods=['GET'])
def get_products():
    """
        Retrieve all products or filter by category.

        Returns:
        JSON response with a list of products. If 'categoryID' is provided as a
        query parameter, only products in that category are returned.
        Otherwise, all products are returned.
        """
    category_id = request.args.get('categoryID')
    if category_id:
        products = get_products_by_category(category_id)
    else:
        products = get_all_products()
    return jsonify({'success': True, 'results': products})


@product_bp.route('/products/<int:product_id>', methods=['GET'])
def get_product(product_id):
    """
        Retrieve a product by its ID.

        Args:
            product_id (int): The ID of the product to retrieve.

        Returns:
        JSON response with the product details if found,
        otherwise a 404 error.
        """
    product = get_product_by_id(product_id)
    if product:
        return jsonify({'success': True, 'results': product})
    return jsonify({'success': False,
                   'messages': [PRODUCT_NOT_FOUND_MSG]}), 404


@product_bp.route('/products', methods=['POST'])
def add_product():
    """
        Create a new product.

        Expects:
            JSON body with 'name', 'price', 'quantity', and 'category_id'.

        Returns:
        JSON response with the new product ID if successful,
        otherwise a 400 error for missing fields.
        """
    data = request.json
    required = ['name', 'price', 'quantity', 'category_id']
    if not all(k in data for k in required):
        return jsonify({
            'success': False,
            'messages': ['Missing required fields']
        }), 400
    product_id = create_product(data)
    return jsonify({'success': True, 'results': {'id': product_id}}), 201


@product_bp.route('/products/<int:product_id>', methods=['PUT'])
def edit_product(product_id):
    """
        Update an existing product by its ID.

        Args:
            product_id (int): The ID of the product to update.

        Expects:
            JSON body with 'name', 'price', 'quantity', and 'category_id'.

        Returns:
        JSON response indicating success, or a 400 error for missing fields,
        or 404 if not found.
        """
    data = request.json
    required = ['name', 'price', 'quantity', 'category_id']
    if not all(k in data for k in required):
        return jsonify({
            'success': False,
            'messages': ['Missing required fields']
        }), 400
    success = update_product(product_id, data)
    if not success:
        return jsonify({'success': False,
                       'messages': [PRODUCT_NOT_FOUND_MSG]}), 404
    return jsonify({'success': True})


@product_bp.route('/products/<int:product_id>', methods=['DELETE'])
def delete_product_route(product_id):
    """
        Delete a product by its ID.

        Args:
            product_id (int): The ID of the product to delete.

        Returns:
            204 No Content on success, or 404 if the product is not found.
        """
    success = delete_product(product_id)
    if success:
        return jsonify({'success': True}), 204
    return jsonify({'success': False,
                   'messages': [PRODUCT_NOT_FOUND_MSG]}), 404
