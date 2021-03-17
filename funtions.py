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
