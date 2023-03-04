products={}
prices={}
pricesPerUnit={}

while True:
    product=input("Enter product name: ")
    if product.lower() == "end":
        break
    else:
        price=input("Enter product price")
        products.append(product)
        prices.append(price)


print("----Inventory----")

for product in product:
    print(product)
