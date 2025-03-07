from utils import get_product_info, get_product_stock, get_all_products


def test_get_all_products():
    """ Verify that the product list is correct."""
    products = get_all_products()
    assert isinstance(products, str)
    assert products.startswith("The available products are:")
    assert 'MacBook Pro' in products
    assert 'AirPods' in products


def test_get_product_info():
    """ Verify that the function returns the proper product info."""
    laptop_info = get_product_info("Apple MacBook Pro")
    assert isinstance(laptop_info, str)
    assert "16GB RAM" in laptop_info
    assert "description" in laptop_info.lower()
    assert "price" in laptop_info.lower()

    unknown_product = get_product_info("TabletXYZ")
    assert unknown_product == "Product not found."


def test_get_product_stock():
    """ Verify that the stock function returns a correct message. """
    phone_stock = get_product_stock("Samsung Galaxy S21")
    assert isinstance(phone_stock, str)
    assert "Samsung Galaxy S21" in phone_stock
    assert "30." in phone_stock.lower()

    unknown_stock = get_product_stock("TabletXYZ")
    assert unknown_stock == "Product not found."

