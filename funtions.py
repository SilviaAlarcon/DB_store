def products_by_country(products):
    print('-' * 20 + ' Productos ' + '-' * 20)
    count = 1
    for i in products:
        data = '{0}. ID: {1} Nombre: {2} | Precio: {3} | Ciudad de origen: {4} | Categoría: {5}'
        print(data.format(count, i[0], i[1], i[2], i[3], i[4]))
        count += 1


def insert_product():
    name = input('Ingresa el nombre del producto: ')
    value = float(input('Ingresa el precio: '))
    country_of_origin = input('Ingresa el país de origen: ')
    id_category = int(input('Ingresa la categoría: '))

    product = (name, value, country_of_origin, id_category)
    return product


def insert_store():
    name = input('Ingresa el nombre de la tienda: ')
    address = input('Ingresa la dirección: ')
    country = input('Ingresa el país: ')

    store = (name, address, country)
    return store


def insert_category():
    name = input('Ingresa el nombre de la categoría: ')
    id_store = int(input('Ingresa el ID de la tienda: '))

    category = (name, id_store)
    return category

def total_value(total):
    print('-' * 40)
    for i in total:
        data = 'Precio total: {0}'
        print(data.format(i[0]))
    print('-' * 40)


def total_products(total):
    print('-' * 40)
    for i in total:
        data = 'Número total de productos: {0}'
        print(data.format(i[0]))
    print('-' * 40)


def order_by_category(total):
    print('-' * 20 + ' Registro por categoría ' + '-' * 20)
    for i in total:
        data = 'ID: {0} Nombre de la categoría: {1} | Número de productos: {2}'
        print(data.format(i[0], i[1], i[2]))
    print('-' * 40)
