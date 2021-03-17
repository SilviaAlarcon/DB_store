import pymysql

class DataBase:
    def __init__(self):
        self.connection = pymysql.connect(
            host="localhost",
            user="root",
            password="test1",
            database="store" 
        )

        self.cursor = self.connection.cursor()
        print('Funcionooo :D')

    #Generar información para la base de datos
    def insert_store(self, name, address, country):
        sql = "INSERT INTO store (name, address, country) VALUES ('{}', '{}', '{}')".format(name, address, country)
        self.cursor.execute(sql)
        self.connection.commit()

    def insert_category(self, name, id_store):
        sql = "INSERT INTO categories (name, id_store) VALUES ('{}', '{}')".format(name, id_store)
        self.cursor.execute(sql)
        self.connection.commit()
    
    def insert_product(self, name, value, country_of_origin, id_category):
        sql = "INSERT INTO products (name, value, country_of_origin, id_category) VALUES ('{}', '{}', '{}', '{}')".format(name, value, country_of_origin, id_category)
        self.cursor.execute(sql)
        self.connection.commit()

    #Mostrar todos los productos de acuerdo a un país
    def products_by_country(self, country_of_origin):
        sql = "SELECT * FROM products WHERE country_of_origin = '{}'".format(country_of_origin)
        self.cursor.execute(sql)
        datos = self.cursor.fetchall()
        print(datos)

    #mostrar el valor total de los productos
    def total_value(self):
        sql = "SELECT SUM(value) FROM products"
        self.cursor.execute(sql)
        datos = self.cursor.fetchall()
        print(datos)

    #Mostrar cantidad total de productos
    def total_products(self):
        sql = "SELECT COUNT(*) FROM products"
        self.cursor.execute(sql)
        datos = self.cursor.fetchall()
        print(datos)

    #Mostrar cantidad de productos ordenados por categoría
    def order_by_category(self):
        sql = "SELECT c.id_category, c.name AS nombre_categoria, COUNT(p.id_category) AS cantidad_productos FROM categories AS c LEFT JOIN products AS p ON p.id_category = c.id_category GROUP BY c.id_category ORDER BY cantidad_productos DESC;"
        self.cursor.execute(sql)
        datos = self.cursor.fetchall()
        print(datos)

    def close(self):
        self.connection.close()


database = DataBase()
#database.insert_category('Labios', 1)
#database.insert_product('Dekineador', 370.30, 'México', 3)
#database.products_by_country('México')
#database.total_products()
database.total_value()
#database.order_by_category()
database.close()