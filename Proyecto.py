from csv import *
import json
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


ventas = list()
total = 0
Cliente_Actual = dict()
Mesa_Actual = None


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
    print("0. Salir")

    Opcion = int(input("Digite su opción: "))



    if Opcion == 1:
        Nombre = input("Nombre: ")
        idCliente = int(input("ID: "))
        Telefono = int(input("Teléfono: "))
        Email = input("Email: ")

        cliente = {"Identificacion":idCliente,"Nombre":Nombre,"Teléfono":Telefono,"Email":Email}

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

            if len(platillos) == 0:
                print("No hay platillos registrados")
            else:
                for plato in platillos:
                    print(plato["Código"], plato["Nombre"], plato["Precio"])

                opcion_plato = input("Seleccione: ")

                encontrado = False
                for plato in platillos:
                    if plato["Código"] == opcion_plato:
                        total += float(plato["Precio"])
                        print("Agregado:", plato["Nombre"])
                        encontrado = True

                if not encontrado:
                    print("Platillo no encontrado")
        except FileNotFoundError:
            print("El archivo Platillos.csv no existe")



    elif Opcion == 4:
        try:
            with open("Bebidas.csv", "r", newline="", encoding="utf-8") as file:
                bebidas = list(DictReader(file))

            if len(bebidas) == 0:
                print("No hay bebidas registradas")
            else:
                for bebida in bebidas:
                    print(bebida["Código"], bebida["Nombre"], bebida["Precio"])

            opcion_bebida = input("Seleccione: ")

            encontrado = False
            for bebida in bebidas:
                if bebida["Código"] == opcion_bebida:
                    total += float(bebida["Precio"])
                    print("Agregado:", bebida["Nombre"])
                    encontrado = True

            if not encontrado:
                print("Bebida no encontrada")

        except FileNotFoundError:
            print("El archivo Bebidas.csv no existe")



    elif Opcion == 5:
        if Cliente_Actual == dict() or Mesa_Actual is None:
            print("Debe seleccionar cliente y mesa")
        else:
            subtotal = total
            iva = subtotal * 0.19
            total_pagar = subtotal + iva
        def facturar_con_descuento():
           
            mesa = input("Ingrese código de mesa: ")
        cliente = input("Ingrese nombre del cliente: ")
    
        total = float(input("Ingrese total de la cuenta: "))
    
    
        while True:
            descuento = float(input("Ingrese porcentaje de descuento (0-50): "))
            if 0 <= descuento <= 50:
                 break
        else:
             print("Descuento invalido. Debe de estar entre 0% y 50%")

    monto_descuento = total * (descuento / 100)
    total_final = total - monto_descuento

    
    monto_descuento = total * (descuento / 100)
    total_final = total - monto_descuento
    print("\n--- FACTURA ---")
    print(f"Mesa: {mesa}")
    print(f"Cliente: {cliente}")
    print(f"Total sin descuento: ${total:.2f}")
    print(f"Descuento aplicado: {descuento}% (-${monto_descuento:.2f})")
    print(f"Total con descuento: ${total_final:.2f}")

    factura = {
        "mesa": mesa,
        "cliente": cliente,
        "total_original": total,
        "descuento_porcentaje": descuento,
        "descuento_monto": monto_descuento,
        "total_final": total_final
    }

    
    with open("factura_descuento.json", "w") as archivo:
        json.dump(factura, archivo, indent=4)

    print("\nFactura guardada en 'factura_descuento.json'")
    print("\n----- FACTURA -----")
    print("Cliente:", Cliente_Actual["nombre"])
    print("Mesa:", Mesa_Actual["Nombre"])
    print("Subtotal:", subtotal)
    print("IVA:", iva)
    print("Total:", total_pagar)
    print(f"Total sin descuento: ${total:.2f}")
    print(f"Descuento aplicado: {descuento}% (-${monto_descuento:.2f})")
    print(f"Total con descuento: ${total_final:.2f}")
    ventas.append({
                "cliente": Cliente_Actual["nombre"],
                "mesa": Mesa_Actual["Nombre"],
                "total": total_pagar
                })
    elif Opcion == 6:
    id_cliente = int(input("Ingrese ID: "))

    if id_cliente in cliente:
            print("Cliente encontrado:")
            print(cliente[id_cliente])
        else:
            print("No existe") 
    elif Opcion == "7":
        if len(ventas) == 0:
           print("No hay ventas")
        else:
            total_general = 0

            for v in ventas:
                print(v)
                total_general += v["total"]

            print("TOTAL GENERAL:", total_general)
    elif Opcion == "8":
    print("Agregar Datos")
    print("1.Platillos")
    print("2.bebidas")
    print("3.Mesas")
    tipo= input("Su Opcion elegida es: ")
    if tipo == "1": 
            Id_plato = input("Id Del Platillo: ")
            nombre = input("Ingrese el platillo: ")
            precio = int(input("Precio: "))

            platillo = {"Código": Id_plato, "Nombre": nombre, "Precio": precio}
            campos = ["Código", "Nombre", "Precio"]

            with open("Platillos.csv", "a", newline="", encoding="utf-8") as file:
                writerCSV = DictWriter(file, fieldnames=campos)
                writerCSV.writeheader()
                writerCSV.writerow(platillo)
    elif tipo == "2": 
            Id_bebida = input("Id De la Bebida: ")
            nombre = input("Ingrese la bebida: ")
            precio = int(input("Precio: "))

            bebida = {"Código": Id_bebida, "Nombre": nombre, "Precio": precio}
            campos = ["Código", "Nombre", "Precio"]

            with open("Bebidas.csv", "a", newline="", encoding="utf-8") as file:
                writerCSV = DictWriter(file, fieldnames=campos)
                writerCSV.writeheader()
                writerCSV.writerow(bebida)
    elif tipo == "3": 
            Id_mesa = input("ID de la nueva mesa: ")
            nombrem= input("Nombre de la mesa: ")
            mesas.append({"ID": Id_mesa, "Nombre": nombrem})
            print("¡Mesa agregada correctamente!")
    else:
            print("Opcion Invalida")