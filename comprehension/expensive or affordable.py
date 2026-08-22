products = {
    "Laptop": 65000,
    "Mouse": 500,
    "Keyboard": 1500,
    "Monitor": 12000
}
result = { product: "Expensive" if price > 10000 else "Affordable" for product, price in products.items() }
print(result)