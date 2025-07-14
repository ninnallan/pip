import sqlite3

shopping_cart = [("apple", 5), ("banana", 4), ("orange", 1), 
                 ("sweets", 2), ("chocolate", 2), ("tomatoes", 5)]

reversed_cart = []
for item in shopping_cart[::-1]:
    reversed_cart.append(item)

conn = sqlite3.connect("shopping.db")
c = conn.cursor()

c.execute("DROP TABLE IF EXISTS shopping")
c.execute("""  
    CREATE TABLE shopping (
        Fruit TEXT,
        Number INTEGER
    )
""")

for item in reversed_cart:
    c.execute("INSERT INTO shopping (Fruit, Number) VALUES (?, ?)", item)

conn.commit()
conn.close()

print("მონაცემები შეინახა ბაზაში შებრუნებული თანმიმდევრობით.")
print(reversed_cart)
