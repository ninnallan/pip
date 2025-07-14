import pymongo
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["menu_db"]
collection = db["menu_items"]

menu = {
    "sprite": 1.70,
    "fries": 2.99,
    "burger": 1.99,
    "shake": 3.5,
    "cookie": 2.4,
    "beef": 3.9
}

collection.delete_many({})
for item, price in menu.items():
    collection.insert_one({"name": item, "price": price})
def make_order():
    order = []

    print("ასარჩევი პროდუქტები:")
    for product in menu:
        print("-", product)

    while True:
        product_name = input("\nრას ინებებთ? ").strip()

        if product_name not in menu:
            print("მარაგი ამოწურულია!")
            continue

        try:
            quantity = int(input("რამდენი ერთეული? "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        order.append([product_name, quantity])

        another = input("გსურთ თუ არა სხვა პროდუქტის დამატება? (კი/არა): ").strip()
        if another == "არა":
            break

    print("\nთქვენი შეკვეთა:")
    print(order)
    return order
make_order()
