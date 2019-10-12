'''
Created on 11/10/2019

@author: Marín
'''
class Nodo: 
    def __init__(self, dato):
        self.siguiente = None
        self.info = dato
    def verNodo(self):
        return self.info
class Temperatura: 
    def __init__(self):
        self.primero = None
    def intertarTemperatura(self, dato):
        temporal=Nodo(dato)
        temporal.siguiente=self.primero
        self.primero = temporal
    def mostrarPromTemperaturas(self):
        temporal = self.primero
        while temporal != None:
            if( temporal.verNodo() <=10):
                print(temporal.verNodo(), end='[: Congelacion]-> ')
                temporal = temporal.siguiente
            elif(temporal.verNodo() <=20):
                print(temporal.verNodo(), end = '[: Frio]-> ')
                temporal = temporal.siguiente
            elif(temporal.verNodo() <=30):
                print(temporal.verNodo(), end = '[: Normal]-> ')
                temporal = temporal.siguiente
            elif(temporal.verNodo() >31):
                print(temporal.verNodo(), end = '[: Alta]-> ')
                temporal = temporal.siguiente
    def mostrarTemp(self):
        temporal = self.primero
        while temporal != None:
            print(temporal.verNodo(), end='[]-> ')
            temporal = temporal.siguiente
print("TEMPERATURAS ==========")
opc = int (input("1)Mostrar todas las Temperaturas\n2)Mostrar Promedios\n3)Ingresar Temperaturas"))
if(opc == 1):
    temp = Temperatura()
    temp.intertarTemperatura(10)
    temp.intertarTemperatura(20)
    temp.intertarTemperatura(31)
    temp.intertarTemperatura(50)
    temp.intertarTemperatura(4)
    temp.mostrarTemp()
elif(opc == 2):
    temp1 = Temperatura()
    temp1.intertarTemperatura(18)
    temp1.intertarTemperatura(23)
    temp1.intertarTemperatura(45)
    temp1.intertarTemperatura(5)
    temp1.mostrarPromTemperaturas()
elif(opc == 3):
    temp2 = Temperatura()
    t1 = int(input("Ingrese la Temperatura: "))
    t2 = int(input("Ingrese la Temperatura: "))
    t3 = int(input("Ingrese la Temperatura: "))
    t4 = int(input("Ingrese la Temperatura: "))
    t5 = int(input("Ingrese la Temperatura: "))
    temp2.intertarTemperatura(t1)
    temp2.intertarTemperatura(t2)
    temp2.intertarTemperatura(t3)
    temp2.intertarTemperatura(t4)
    temp2.intertarTemperatura(t5)
    temp2.mostrarTemp()
    print("PROMEDIO: " +temp2.mostrarPromTemperaturas())