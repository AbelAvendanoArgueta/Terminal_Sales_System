
# Terminal_Sales_System
## Parcial: Programa de gestión de tienda
Este programa fue desarrollado como parte del parcial del curso de Programación I. Su objetivo es permitir la gestión de una tienda, permitiendo la adición de nuevos productos, la realización de compras y la visualización de los productos disponibles en la tienda.

### Características
Interfaz de usuario intuitiva y fácil de usar.
Uso de funciones para modularizar el código y hacerlo más mantenible y eficiente.
Validación de entradas de usuario para reducir la posibilidad de errores en el programa.
Uso de la librería unidecode para manejar correctamente los caracteres con acentos y reducir posibles errores.
Se pueden agregar nuevos productos a la tienda especificando su nombre, precio y cantidad disponible.
Se pueden hacer compras especificando el nombre del producto y la cantidad deseada. El programa verifica que el producto esté disponible y que haya suficiente cantidad en existencia antes de realizar la compra.
Se pueden listar los productos disponibles en la tienda.

### Funciones principales del software
La razón por la que se colocan funciones en el script es para modularizar el código y hacerlo más fácil de mantener y entender. Las funciones dividen el código en bloques lógicos, lo que hace que sea más fácil de leer y modificar. Además, al utilizar funciones, se evita repetir el mismo código varias veces en diferentes partes del script, lo que reduce la posibilidad de errores y hace que el código sea más eficiente.

**print_header(text):** Función para imprimir encabezados centrados.
**agregar_producto():** Función para agregar un nuevo producto.
**hacer_compra():** Función para realizar una compra.
**listar_productos():** Función para listar los productos.

### Ejecución del programa
El programa tiene un loop principal que muestra un menú de opciones al usuario y espera a que el usuario ingrese una opción. Dependiendo de la opción seleccionada, se llama a una de las funciones principales para agregar un producto, hacer una compra o listar los productos disponibles en la tienda.

***¡Disfrute usando el programa!***