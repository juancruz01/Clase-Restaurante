#escribe una clase python llamada restaurant
#Realiza las siguentes tareas ahora:
#añade items al menu
#Reserva mesas
#Toma pedidos
#Imprime el menu
#Imprime las reservas de mesa
#Imprime los pedidos de los clientes

#"TAREA" cuando se haga un pedido, que revise si los items estan en el menu

#Supuestos
#1) los items tiene nombre y precio { hamburguesa: 3.5}
#2) las mesas estaran numeradas, tendran un nombre de la persona que reserva, estado de la mesa (si esta reservada o no)
#3) las ordenes tendran el nombre del cliente, y los items deseados

class restaurant:
    def __init__(self):
        self.menu = {}
        #self.mesas = []
        self.mesas_reservadas = {}
        self.ordenes = {}


    def add_item(self, item, precio):
        self.menu[item] = precio

    def reserva_mesas(self,numero, nombre_cliente ):
        if numero not in self.mesas_reservadas:
            self.mesas_reservadas[numero] = nombre_cliente
        else:
            print(f"Lo siente la mesa {numero} ya esta reservada")

    def pedidos(self, numero, items):
        for item in items:
            if item not in self.menu:
                print(f"El item {item} no esta en el menu.")
                return
        
        if numero not in self.ordenes:
            self.ordenes[numero] = items
        else:
            self.ordenes[numero].extend(items)

    def imprimir_menu(self):
        print(f"el Menu es: {self.menu}")

    def imprimir_reservas(self):
        print(f"Las mesas reservadas son: {self.mesas_reservadas}")

    def imprimir_pedidos(self):
        print(f"Los pedidos hechos son: {self.ordenes}")
 
#almacenamos la clase restaurantre dentro de una variable objeto
restaurante = restaurant()

#mediante el metodo add_item añadimos items(comida) al menu
restaurante.add_item("Hamburguesa", 3.5)
restaurante.add_item("Pizza", 4.0)

#mediante el metodo reserva_mesas() añadimos un numero de mesa y el nombre del cliente con el que se reserva
restaurante.reserva_mesas(1,"juan cruz")
restaurante.reserva_mesas(2,"maite")

#restaurante.reserva_mesas(1,"rodolfo")

print("----------")
#mediante el metodo .pedidos() añadimos, priemro con el numero de mesa, y luego lo seleccionado en el menu
restaurante.pedidos(1,["Hamburguesa", "Pizza"])
restaurante.pedidos(1, ["Pizza"])
restaurante.pedidos(1,["Milanesa"])
print("-.----------")

#mostramos por pantalla con los metodos print
restaurante.imprimir_menu()
restaurante.imprimir_pedidos()
restaurante.imprimir_reservas()
