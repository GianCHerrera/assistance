import json

with open("catalog.json") as file:
    catalog = json.load(file)


def get_product_info(product_name: str) -> str:
    product = next((item for item in catalog if item["Name"].lower() == product_name.lower()), None)
    if product:
        return f"The product is {product['Name']} with description: {product['Description']} and price: {product['Price']}."
    else:
        return "Product not found."


def get_product_stock(product_name: str) -> str:
    product = next((item for item in catalog if item["Name"].lower() == product_name.lower()), None)
    if product:
        return f"The product {product['Name']} is in stock with availability: {product['Stock_availability']}."
    else:
        return "Product not found."


def get_all_products() -> str:
    products = [product["Name"] for product in catalog]
    return f"The available products are: {', '.join(products)}."
