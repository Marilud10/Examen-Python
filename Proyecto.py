from csv import *
import json
from datetime import datetime
import os

if not os.path.exists("reports"):
    os.makedirs("reports")

with open("Platillos.csv","a"):
    pass
with open ("Bebidas.csv", "a"):
    pass

platillos = [  
    {"id":"01", "Nombre": "Arroz de coco", "Precio": 20000},
    {"id":"02", "Nombre": "Alitas BBQ", "Precio": 24000},
    {"id":"03", "Nombre": "Carne Bistec", "Precio": 30000},
    {"id":"04", "Nombre": "Bandeja Paisa", "Precio": 25000},
    {"id":"05", "Nombre": "Pizza Napoletana", "Precio": 50000}
]

bebidas = [ 
    {"id":"01", "Nombre": "Gaseosa", "Precio": 20000},
    {"id":"02", "Nombre": "Limonada Cereza", "Precio": 24000},
    {"id":"03", "Nombre": "Cerveza", "Precio": 30000},
    {"id":"04", "Nombre": "Agua Mineral", "Precio": 25000},
    {"id":"05", "Nombre": "Mojito", "Precio": 50000}
]

mesas = [ 
    {"id":"m1", "Nombre": "Mesa Inicio", "sillas": 4},
    {"id":"m2", "Nombre": "Mesa izquierda", "sillas": 3},
    {"id":"m3", "Nombre": "Mesa Derecha", "sillas": 3},
    {"id":"m4", "Nombre": "Mesa Centro", "sillas": 5},
    {"id":"m5", "Nombre": "Mesa Rincon", "sillas": 2}
]

ventas = []
detalle_ventas = []
total = 0
Cliente_Actual = dict()
Mesa_Actual = None

def producto_mas_vendido(fecha_inicio, fecha_fin):
    inicio = datetime.strptime(fecha_inicio, "%Y-%m-%d")
    fin = datetime.strptime(fecha_fin, "%Y-%m-%d")

    conteo = {}

    for venta in detalle_ventas:
        fecha = datetime.strptime(venta["fecha"], "%Y-%m-%d")

        if inicio <= fecha <= fin:
            nombre = venta["producto"]

            if nombre in conteo:
                conteo[nombre] += 1
            else:
                conteo[nombre] = 1

    if len(conteo) == 0:
        print("No hay ventas en ese rango")
        return

    mas_vendido = max(conteo, key=conteo.get)

    print("\nProducto más vendido:")
    print("Nombre:", mas_vendido)
    print("Cantidad:", conteo[mas_vendido])

    data = {
        "fecha_consulta": datetime.now().strftime("%Y-%m-%d"),
        "producto": mas_vendido,
        "cantidad": conteo[mas_vendido]
    }

    with open("reports/reporte.json", "w") as f:
        json.dump(data, f, indent=4)

while True:
    print("\n----Bienvenido al restaurante Don Sebas----")
    print("1. Ingrese Datos del Cliente")
    print("2. Elegir Mesa")
    print("3. Elegir Platillo")
    print("4. Elegir Bebida")
    print("5. Facturación")
    print("6. Buscar Cliente")
    print("7. Registro de Ventas")
    print("8. Agregar Datos")
    print("9. Reporte producto más vendido")
    print("0. Salir")

    Opcion = int(input("Digite su opción: "))

    if Opcion == 1:
        Nombre = input("Nombre: ")
        idCliente = int(input("ID: "))
        Telefono = int(input("Teléfono: "))
        Email = input("Email: ")

        cliente = {"Identificacion":idCliente,"Nombre":Nombre,"Teléfono":Telefono,"Email":Email}
        Cliente_Actual = cliente

        with open("Clientes.csv","a",newline="",encoding="utf-8") as file:
            writerCSV = DictWriter(file,fieldnames=["Identificacion","Nombre","Teléfono","Email"])
            writerCSV.writeheader()
            writerCSV.writerows([cliente])

    elif Opcion == 2:
        for mesa in mesas:
            print(f"{mesa['id']} {mesa['Nombre']} ({mesa['sillas']} sillas)")

        Mesa_seleccionada = input("Seleccione mesa: ")

        for mesa in mesas:
            if mesa["id"] == Mesa_seleccionada:
                Mesa_Actual = mesa
                print("Mesa seleccionada:", mesa["Nombre"])

    elif Opcion == 3:
        try:
            with open("Platillos.csv", "r", newline="", encoding="utf-8") as file:
                platillos = list(DictReader(file))

            for plato in platillos:
                print(plato["Código"], plato["Nombre"], plato["Precio"])

            opcion_plato = input("Seleccione: ")

            for plato in platillos:
                if plato["Código"] == opcion_plato:
                    total += float(plato["Precio"])
                    detalle_ventas.append({
                        "producto": plato["Nombre"],
                        "fecha": datetime.now().strftime("%Y-%m-%d")
                    })
                    print("Agregado:", plato["Nombre"])

        except:
            print("Error en platillos")

    elif Opcion == 4:
        try:
            with open("Bebidas.csv", "r", newline="", encoding="utf-8") as file:
                bebidas = list(DictReader(file))

            for bebida in bebidas:
                print(bebida["Código"], bebida["Nombre"], bebida["Precio"])

            opcion_bebida = input("Seleccione: ")

            for bebida in bebidas:
                if bebida["Código"] == opcion_bebida:
                    total += float(bebida["Precio"])
                    detalle_ventas.append({
                        "producto": bebida["Nombre"],
                        "fecha": datetime.now().strftime("%Y-%m-%d")
                    })
                    print("Agregado:", bebida["Nombre"])

        except:
            print("Error en bebidas")

    elif Opcion == 5:
        if Cliente_Actual == dict() or Mesa_Actual is None:
            print("Debe seleccionar cliente y mesa")
        else:
            subtotal = total
            descuento = float(input("Ingrese descuento (0 a 50): "))

            if descuento < 0 or descuento > 50:
                print("Descuento inválido")
            else:
                descuento_valor = subtotal * (descuento / 100)
                subtotal_con_descuento = subtotal - descuento_valor
                iva = subtotal_con_descuento * 0.19
                total_pagar = subtotal_con_descuento + iva

                print("\n----- FACTURA -----")
                print("Cliente:", Cliente_Actual["Nombre"])
                print("Mesa:", Mesa_Actual["Nombre"])
                print("Subtotal:", subtotal)
                print("Descuento:", descuento)
                print("Total con descuento:", subtotal_con_descuento)
                print("IVA:", iva)
                print("Total:", total_pagar)

                ventas.append({
                    "cliente": Cliente_Actual["Nombre"],
                    "mesa": Mesa_Actual["Nombre"],
                    "total": total_pagar
                })

                total = 0

    elif Opcion == 6:
        id_cliente = int(input("Ingrese ID: "))

        if id_cliente == Cliente_Actual.get("Identificacion"):
            print("Cliente encontrado:")
            print(Cliente_Actual)
        else:
            print("No existe")

    elif Opcion == 7:
        for v in ventas:
            print(v)

    elif Opcion == 8:
        print("1.Platillos")
        print("2.Bebidas")
        tipo= input("Opción: ")

        if tipo == "1":
            Id_plato = input("Id: ")
            nombre = input("Nombre: ")
            precio = int(input("Precio: "))

            with open("Platillos.csv", "a", newline="", encoding="utf-8") as file:
                writerCSV = DictWriter(file, fieldnames=["Código","Nombre","Precio"])
                writerCSV.writeheader()
                writerCSV.writerow({"Código":Id_plato,"Nombre":nombre,"Precio":precio})

        elif tipo == "2":
            Id_bebida = input("Id: ")
            nombre = input("Nombre: ")
            precio = int(input("Precio: "))

            with open("Bebidas.csv", "a", newline="", encoding="utf-8") as file:
                writerCSV = DictWriter(file, fieldnames=["Código","Nombre","Precio"])
                writerCSV.writeheader()
                writerCSV.writerow({"Código":Id_bebida,"Nombre":nombre,"Precio":precio})

    elif Opcion == 9:
        fi = input("Fecha inicio (YYYY-MM-DD): ")
        ff = input("Fecha fin (YYYY-MM-DD): ")
        producto_mas_vendido(fi, ff)

    elif Opcion == 0:
        break

    else:
        print("Opción inválida")
