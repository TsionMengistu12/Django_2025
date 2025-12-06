#### Question number 1
amount = int(input("How many items do you want to buy? "))
if amount > 3:
    print("Discount applied")
else:
    print("No discount")

#### Question number 2
prices = [120, 45, 300, 85, 150]
expensive = []
def get_expensive_products(li):
    for pro in li:
        if pro > 100:
            expensive.append(pro)
    return expensive

print(get_expensive_products(prices))

