import os
from unidecode import unidecode
"""
Unidecode es una librería que estoy usando en caso
el usuario inserte un dato con acento y para reducir
la posibilidad de errores en el código
"""
## Funciones principales del software

"""
La razón por la que se colocan funciones en el script es para modularizar 
el código y hacerlo más fácil de mantener y entender. Las funciones dividen el
código en bloques lógicos, lo que hace que sea más fácil de leer y modificar.
Además, al utilizar funciones, se evita repetir el mismo código varias veces 
en diferentes partes del script, lo que reduce la posibilidad de errores y hace
que el código sea más eficiente.
"""
# Inicializar el diccionario de productos vacío
productos = {}

# Función para imprimir encabezados centrados
def print_header(text):

    # La función get_terminal_size() devuelve un objeto 
    # os.terminal_size que contiene el tamaño actual de la terminal.
    terminal_size = os.get_terminal_size().columns
    header = text.center(terminal_size)
    print(header)

# Función para agregar un nuevo producto
def agregar_producto():
    global productos
    nombre = input("\nIngrese el nombre del producto\nEj: Leche, Huevos, Queso... : ")
    clear_nombre = unidecode(nombre.lower())
    precio = float(input("\nIngrese el precio del producto\nEj: 10.00, 5.75, 3.50... : "))
    precio_str = "{:.2f}".format(precio) # Convertir el precio a string con dos decimales
    cantidad = int(input("\nIngrese la cantidad disponible del producto\nEj: 1, 2, 3, 4, 5, 6... : "))
    productos[clear_nombre] = {"precio": precio_str, "cantidad": cantidad}
    exportar_productos(productos)

# Función para actualizar un nuevo producto
def actualizar_producto():
    global productos
    nombre = input("\nIngrese el nombre del producto que desea actualizar\nEj: Leche, Huevos, Queso... : ")
    clear_nombre = unidecode(nombre.lower())
    precio = float(input("\nIngrese  nuevo precio del producto\nEj: 10.00, 5.75, 3.50... : "))
    precio_str = "{:.2f}".format(precio) # Convertir el precio a string con dos decimales
    cantidad = int(input("\nIngrese la nueva cantidad disponible del producto\nEj: 1, 2, 3, 4, 5, 6... : "))
    productos[clear_nombre] = {"precio": precio_str, "cantidad": cantidad}
    exportar_productos(productos)

# Función para realizar una compra
def hacer_compra():
    nombre = input("\nIngrese el nombre del producto que desea comprar: ")
    clear_nombre = unidecode(nombre.lower())
    cantidad = int(input("\nIngrese la cantidad que desea comprar\nEj: 1, 2, 3, 4, 5, 6... : "))

    # Verificar si el producto está disponible
    if clear_nombre in productos and productos[clear_nombre]["cantidad"] >= cantidad:
        precio_total = float(productos[clear_nombre]["precio"]) * cantidad
        print("\nEl precio total de su compra es: ${:.2f}\n".format(float(precio_total)))

        productos[clear_nombre]["cantidad"] -= cantidad
        # Aquí se llama a la función exportar productos
        # para actualizar automáticamente el archivo de
        # "productos.txt" automáticamente
        exportar_productos(productos)
    else:
        print("\nLo siento, el producto no está disponible o no hay suficiente cantidad en existencia.\n")

# Función para listar los productos
def listar_productos():
    print("\nProductos disponibles en la tienda:\n")
    for producto, info in productos.items():
        print(f"- {producto}: precio Q {info['precio']}, cantidad en existencia: {info['cantidad']}")

    input("\nPresione 'Enter' para continuar\n")

# Función para exportar los productos aun archivo *.txt
def exportar_productos(productos):
    with open("productos.txt", "w") as f:
        for producto, info in productos.items():
            f.write(f"{producto},{info['precio']},{info['cantidad']}\n")
    print("\nLos productos se han exportado correctamente.\n")

# Función para importar la información del archivo *.txt
# y asignarlos a la variable global 'productos'  
def importar_productos():
    global productos
    try:
        with open("productos.txt", "r") as f:
            for line in f:
                nombre, precio, cantidad = line.strip().split(",")
                productos[nombre] = {"precio": float(precio), "cantidad": int(cantidad)}
        print("\nLos productos se han importado correctamente.\n")
    except FileNotFoundError:
        print("\nEl archivo de productos no existe.\n")
    return productos

## Ejecución del programa
# Loop principal del programa
while True:
    ## Imprimir encabezados
    print_header("UNIVERSIDAD PANAMERICANA DE GUATEMALA")
    print_header("Campus de Cobán Alta Verapaz")
    print_header("Facultad de Ingeniería y Ciencias Aplicadas")
    print_header("Carrera de Ingeniería en Sistemas y Tecnologías de la Información y Comunicación")
    print_header("Abel Fernando Avendaño Argueta 000127599")

    # Saludo
    print("\n\n         Bienvenido a este programa! \n\n")

    # Advertencias
    print("Se le recomienda que su primera acción usando este software")
    print("sea el de Importar/Actualizar la lista de productos para")
    print("evitar perdida de datos \n\n")

    # Menu Principal
    print("1. Exportar lista de productos")
    print("2. Importar/Actualizar lista de productos")
    print("3. Agregar un producto")
    print("4. Actualizar un producto")
    print("5. Hacer una compra")
    print("6. Listar productos")
    print("7. Salir")

    opción = int(input("Ingrese una opción: "))

    # Llamado de las funciones
    if opción == 1:
        exportar_productos(productos)
    elif opción == 2:
        importar_productos()
    elif opción == 3:
        agregar_producto()
    elif opción == 4:
        actualizar_producto()
    elif opción == 5:
        hacer_compra()
    elif opción == 6:
        listar_productos()
    elif opción == 7:
        # Aquí se llama a la función exportar productos
        # para actualizar automáticamente el archivo de
        # "productos.txt" automáticamente
        exportar_productos(productos)
        # Romper el loop principal del programa y cerrarlo
        break
    else:
        print("Opción inválida.")
