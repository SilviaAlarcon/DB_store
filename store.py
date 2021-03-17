from DB.connection import DataBase

def menu():
    print('-' * 20 + ' MENU ' + '-' * 20)
    print('1 - Registrar nueva tienda')
    print('2 - Agregar producto')
    print('3 - Crear nueva categoría')
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
        pass
    elif option == 2:
        pass
    elif option == 3:
        pass
    elif option == 4:
        try:
            products = db.total_products()
            if len(products) > 0:
                pass
            else: 
                print('No se encontraron productos')
        except:
            pass    
    elif option == 5:
        pass
    elif option == 6:
        pass
    elif option == 7:
        pass
    elif option == 8:
        pass
    else:
        print('Opción inválida')
    

if __name__ == '__main__':
    menu()