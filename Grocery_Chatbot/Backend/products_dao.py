import mysql.connector

cnx = mysql.connector.connect(user='root', password='010992@Auk',
                              host='127.0.0.1',
                              database='grocery_store')

cursor = cnx.cursor()

query = "SELECT * FROM grocery_store.products"

cursor.execute(query)

for (product_id, name, uom_id, price_per_unit) in cursor:
    print(product_id, name, uom_id, price_per_unit)

cnx.close()


