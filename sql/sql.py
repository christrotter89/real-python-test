import sqlite3, csv

with sqlite3.connect("inventory.db") as connection:
	c = connection.cursor()
	#c.execute("""CREATE TABLE regions (city TEXT, region TEXT)""")

	#modelmake = [
	#("Ford","Quarz"),
	#("Ford", "Fiesta"),
	#("Ford", "Mondeo")
	#]

	#for car in modelmake:
		#print car[0], car[1]
	car_make = [
	('Ford','Mondeo'),
	('Ford','Quarz'),
	('Ford', 'Fiesta'),
	('Honda', 'Civic'),
	('Honda', 'Ober')
	]

	for car in car_make:
		c.execute("SELECT orders.Quantity FROM orders WHERE orders.Make = (?) AND orders.Model = (?)", (car[0],car[1]))
		rows = c.fetchall()
		c.execute("SELECT cars.Quantity FROM cars WHERE cars.Make = (?) AND cars.Model = (?)", (car[0],car[1]))
		rows_2 = c.fetchall()
		print "Make: ", car[0]
		print "Model: ", car[1]
		print "Order Quantity: ", rows[0][0]
		print "Quantity in stock: ", rows_2[0][0]
		print "-"*10


	c.close()

