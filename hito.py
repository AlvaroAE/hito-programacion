class Cliente():
    def __init__(self) -> None:
        self.nombre = input("¿Cual es tu nombre? ")
        self.apellido = input("¿Cual es tu nombre? ")
        self.dni = input("¿Cual es tu dni? ")
        self.telefono = input("¿Cual es tu numero de telefono? ")
        self.email = input("¿Cual es tu email? ")
        self.localizacion = input("¿De donde eres? ")
    
    def registro(self):
        print(f"El cliente que se ha registrado se llama {self.nombre} {self.apellido} con DNI: {self.dni}, con numero de telefono: {self.telefono}, con correo electronico: {self.email} y procediente de {self.localizacion}")

nombre = []
apellido = []
dni = []
telefono = []
email = []
localizacion = []


class productos(Cliente):
    def __init__(self) -> None:
        super().__init__()

    def productos(self):
        print("Lista de compra")

        while True:
            print("Añadir producto: ")
            print("Eliminar producto: ")
            print("Mostrar lista de compra: ")
            print("Salir y pagar: ")
            print()
            opcion = input("--> ")
            print()

            if opcion == "1":
                producto = input("Ingresa el producto: ").capitalize()
                if producto in compra:
                    print("El producto ya esta en su lista de compra")
                else:
                    compra.appened(producto)

compra = []


menu = int(input("Elige una opcion \n 1 - Registrar cliente \n 2 - Seleccionar productos \n3 - Pagar productos \n4 - Seguimiento de mi pedido \n 5 - Salir \n"))
while menu !=5:
    if menu==1:
        print("Rellena lo siguiente")
        nombre (input("Dime tu nombre: "))
        apellido (input("Dime tus apellidos: "))
        dni (input("Dime tu DNI: "))
        telefono (input("Dime tu telefono: "))
        email (input("Dime tu email: "))
        localizacion (input("Dime donde vives: "))
    elif menu==2:
        elegir=int(input("Productos: \n 1 - camisetas \n 2 - pantalones \n3 - zapatillas \n4 - abrigos \n 5 - Salir \n"))
        while elegir!=5:
            if elegir ==1:
                camisetas=int(input("¿Cuantas camisetas desea? "))
            elif elegir ==2:
                pantalones=int(input("¿Cuantos pantalones desea? "))
            elif elegir ==3:
                zapatillas=int(input("¿Cuantas zapatillas desea? "))
            elif elegir ==4:
                abrigos=int(input("¿Cuantos abrigos desea? "))
            else:
                print("Ingrese un producto")
            elegir=int(input("Productos: \n 1 - camisetas \n 2 - pantalones \n3 - zapatillas \n4 - abrigos \n 5 - Salir \n"))
    elif menu==3:
        print(f"La factura fue enviada al {email}")
    elif menu==4:
        print(f"El seguimiento de la compra fue enviada al {telefono}")
    else:
        print("Ingrese un producto")
    elegir=int(input("Productos: \n 1 - camisetas \n 2 - pantalones \n3 - zapatillas \n4 - abrigos \n 5 - Salir \n"))

camisetas = []
pantalones = []
zapatillas = []
abrigos = []