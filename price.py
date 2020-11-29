def format_price(price):
    price = int(price)
    x = "Цена: "
    y = str(price)
    z = " руб"
    return x + y + z
price = 56.24
print(format_price(price))
