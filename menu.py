class Producto:
    def __init__(self, nombre, cantidad, precio_unitario, ubicacion):
        self.nombre = nombre
        self.cantidad = int(cantidad)
        self.precio_unitario = float(precio_unitario)
        self.ubicacion = ubicacion

class Inventario:
    def __init__(self):
        self.productos = []

    def cargar_inventario(self, archivo):
        with open(archivo, 'r') as f:
            for line in f:
                datos = line.strip().split(';')
                if line.startswith('crear_producto'):
                        sincomando = line.replace('crear_producto',"")
                        cadena = sincomando.split(';')
                        if len(cadena) != 0:
                                print(cadena[0].strip())
                                nombre = cadena[0].strip()
                                cantidad = cadena[1].strip()
                                precio_unitario = cadena[2].strip()
                                ubicacion = cadena[3].strip()
                                producto = Producto(nombre,cantidad,precio_unitario,ubicacion)
                                self.productos.append(producto)
                                
        

    def agregar_stock(self, nombre, cantidad, ubicacion):
        for producto in self.productos:
            if producto.nombre == nombre and producto.ubicacion == ubicacion:
                producto.cantidad += int(cantidad)
                return
        print("Producto no encontrado en la ubicación especificada.")

    def vender_producto(self, nombre, cantidad, ubicacion):
        for producto in self.productos:
            if producto.nombre == nombre and producto.ubicacion == ubicacion:
                if producto.cantidad >= int(cantidad):
                    producto.cantidad -= int(cantidad)
                else:
                    print("Cantidad a vender es mayor que la existencia.")
                return
        print("Producto no encontrado en la ubicación especificada.")

    def crear_informe(self, archivo):
        with open(archivo, 'w') as f:
            f.write("Producto\tCantidad\tPrecio Unitario\tValor Total\tUbicación\n")
            for producto in self.productos:
                valor_total = producto.cantidad * producto.precio_unitario
                f.write(f"{producto.nombre}\t{producto.cantidad}\t{producto.precio_unitario}\t{valor_total}\t{producto.ubicacion}\n")

def main():
    inventario = Inventario()

    while True:
        print("1. Cargar inventario")
        print("2. Cargar instrucciones de movimiento")
        print("3. Crear informe de inventario")
        print("4. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            print('Ingrese el nombre del archivo inicial de inventario')
            archivo = input()
            inventario.cargar_inventario(archivo)
        elif opcion == '2':
            print('Ingrese el nombre del archivo de movimientos')
            archivo_mov = input()
            with open(archivo_mov, 'r') as f:
                for line in f:
                        if line.startswith('agregar_stock'):
                            sincomando = line.replace('agregar_stock', "")
                            cadena = sincomando.split(';')
                            if len(cadena) == 3:
                                nombre = cadena[0].strip()
                                cantidad = cadena[1].strip()
                                ubicacion = cadena[2].strip()
                                print(nombre, cantidad, ubicacion)
                                inventario.agregar_stock(nombre, cantidad, ubicacion)
                            else:
                                print("Instrucción no válida.")
                        elif line.startswith('vender_producto'):
                            sincomando2 = line.replace('vender_producto', "")
                            cadena2 = sincomando2.split(';')
                            if len(cadena2) == 3:
                                nombre = cadena2[0].strip()
                                cantidad = cadena2[1].strip()
                                ubicacion = cadena2[2].strip()
                                print(nombre, cantidad, ubicacion)
                                inventario.vender_producto(nombre, cantidad, ubicacion)
                            else:
                                print("Instrucción no válida.")
                        else:
                            print("Instrucción no válida.")
        elif opcion == '3':
            inventario.crear_informe("informe_inventario.txt")
            print("Informe de inventario creado exitosamente.")
        elif opcion == '4':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == "__main__":
    main()
