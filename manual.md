                                    Manual de Usuario - Sistema de Inventario
Bienvenido al Sistema de Inventario. Este programa te permite gestionar y realizar seguimiento de los productos en tu inventario. Aquí tienes una guía paso a paso sobre cómo usar el programa.
Pasos Iniciales:
    1.	Cargar Inventario:
        •	Selecciona la opción 1 para cargar el inventario desde un archivo .inv.
        •	Asegúrate de que el archivo .inv contenga las líneas de productos en el formato correcto: 
            ‘crear_producto Nombre;Cantidad;Precio_Unitario;Ubicación’.
    2.	Cargar Instrucciones de Movimiento:
        •	Selecciona la opción 2 para cargar las instrucciones de movimiento desde un archivo .mov.
        •	Asegúrate de que el archivo .mov contenga las instrucciones en el formato correcto: ‘agregar_stock Nombre;Cantidad;       
            Ubicación o vender_producto Nombre;Cantidad;Ubicación’.
    3.	Crear Informe de Inventario:
        •	Selecciona la opción 3 para crear un informe de inventario en un archivo informe_inventario.txt.
        •	El informe contendrá detalles sobre los productos en el inventario, incluyendo Nombre, Cantidad, Precio Unitario, Valor     
            Total y Ubicación.
Gestión de Inventario:
    1.	Agregar Stock:
        •	Selecciona la opción 2 y carga las instrucciones de movimiento para agregar stock.
        •	Ingresa el nombre del producto, la cantidad que deseas agregar y la ubicación.
        •	El programa verificará si el producto existe en la ubicación especificada y aumentará la cantidad si es posible.
    2.	Vender Producto:
        •	Selecciona la opción 2 y carga las instrucciones de movimiento para vender un producto.
        •	Ingresa el nombre del producto, la cantidad que deseas vender y la ubicación.
        •	El programa verificará si el producto existe en la ubicación y si hay suficiente cantidad para vender. Realizará la venta 
            si es posible.
