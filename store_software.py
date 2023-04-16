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

# Función para realizar una compra
def hacer_compra():
    nombre = input("\nIngrese el nombre del producto que desea comprar: ")
    clear_nombre = unidecode(nombre.lower())
    cantidad = int(input("\nIngrese la cantidad que desea comprar\nEj: 1, 2, 3, 4, 5, 6... : "))

    # Verificar si el producto está disponible
    if clear_nombre in productos and productos[clear_nombre]["cantidad"] >= cantidad:
        precio_total = float(productos[clear_nombre]["precio"]) * cantidad
        print("El precio total de su compra es: ${:.2f}".format(float(precio_total)))

        productos[clear_nombre]["cantidad"] -= cantidad
    else:
        print("Lo siento, el producto no está disponible o no hay suficiente cantidad en existencia.")

# Función para listar los productos
def listar_productos():
    print("\nProductos disponibles en la tienda:\n")
    for producto, info in productos.items():
        print(f"- {producto}: precio Q {info['precio']}, cantidad en existencia: {info['cantidad']}")

    input("\nPresione 'Enter' para continuar")

# Función para listar los productos
def exportar_productos(productos):
    with open("productos.txt", "w") as f:
        for producto in productos:
            f.write(f"{producto['nombre']},{producto['precio']},{producto['stock']}\n")
    print("\nLos productos se han exportado correctamente.\n")

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
    print("1. Agregar un producto")
    print("2. Hacer una compra")
    print("3. Listar productos")
    print("4. Salir")


    opción = int(input("Ingrese una opción: "))

    # Llamado de las funciones
    if opción == 1:
        exportar_productos()
    #elif opción == 2:
    #    importar_productos()
    elif opción == 3:
        agregar_producto()
    elif opción == 4:
        hacer_compra()
    elif opción == 5:
        listar_productos()
    elif opción == 6:
        # Romper el loop principal del programa y cerrarlo
        break
    else:
        print("Opción inválida.")
