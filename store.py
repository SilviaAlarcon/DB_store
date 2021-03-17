from DB.connection import DataBase
import funtions

def menu():
    print('-' * 20 + ' MENU ' + '-' * 20)
    print('1 - Registrar nueva tienda')
    print('2 - Crear nueva categoría')
    print('3 - Agregar producto')
    print('4 - Mostrar todos los productos por país')
    print('5 - Mostrar el valor total de los productos')
    print('6 - Mostrar la cantidad total de productos')
    print('7 - Mostrar cantidad de productos ordenados por categoría')
    print('8 - Salir')
    print('-' * 50)
    option = int(input('Selecciona una opción: '))

    if option < 1 or option > 8:
        print('Opción inválida')
    elif option == 8:
        print('Adiosin')
    else:
        run_option(option)

def run_option(option):
    db = DataBase()
    if option == 1:
        store = funtions.insert_store()
        try:
            db.insert_store(store)
            print('\nTienda registrada')
        except: 
            print('Ocurrió un error') 
    elif option == 2:
        category = funtions.insert_category()
        try:
            db.insert_category(category)
            print('\nCategoría agregada')
        except: 
            print('Ocurrió un error') 
    elif option == 3:
        product = funtions.insert_product()
        try:
            db.insert_product(product)
            print('\nProducto agregado')
        except: 
            print('Ocurrió un error') 
    elif option == 4:
        country = input('Ingresa un país: ')
        try:
            products = db.products_by_country(country)
            if len(products) > 0:
                funtions.products_by_country(products)
            else: 
                print('No se encontraron productos')
        except:
            print('Ocurrió un error')    
    elif option == 5:
        try:
            total = db.total_value()
            if len(total) > 0:
                funtions.total_value(total)
            else: 
                print('No se encontraron productos')
        except:
            print('Ocurrió un error') 
    elif option == 6:
        try:
            total = db.total_products()
            if len(total) > 0:
                funtions.total_products(total)
            else: 
                print('No se encontraron productos')
        except:
            print('Ocurrió un error') 
    elif option == 7:
        try:
            total = db.order_by_category()
            if len(total) > 0:
                funtions.order_by_category(total)
            else: 
                print('No se encontraron categorías')
        except:
            print('Ocurrió un error') 
    else:
        print('Opción inválida')
    

if __name__ == '__main__':
    menu()