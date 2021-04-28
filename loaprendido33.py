a="Formulario de acceso al sistema" #título del formulario
a_may=a.upper() #utilizando la función upper
print(a_may) #imprime el título con la nueva función, poniéndolo en mayúscula

print("") #salto de línea(debo buscar otra manera de hacerlo)

print("Empezaremos con unas preguntas básicas para saber si cumples con los requisitos de ingreso \n")

nombre=(input("¿Cuál es tu nombre? \n\n"))
print("")
print(str(nombre) + "," +" es un placer conocerte")

edad=int(input("Indicanos tu edad: ")) #para ingresar por teclado un valor, en este caso, edad
intentos=0
while edad<18 or edad>100: #bucle para poner condición en un intervalo de edad
	print("No está permitido tu ingreso")

	if intentos==1: #limitar el bucle
	    print("Has ingresado demasiadas veces un valor que no corresponde a una edad permitida")
	    break #corta el bucle cuando el número de intentos llega a 2

	edad=int(input("Indicanos tu edad: ")) #vuelve y pregunta por edad en caso de que la condición del while sea V
	if edad<18 or edad>100:
		intentos=intentos+1 #actua de contador para limitar el bucle

#MODULO UNO
#Operaciones básicas

print("")
print("PRUEBA UNO")
print("En este módulo vamos a evaluar la capacidad que tiene nuestro sistema de hacer operaciones matemáticas")

def suma(numero1,numero2): #se declaran funciones que van a ser utilizadas más adelante
	return numero1+numero2
def resta(numero1,numero2):
	return numero1-numero2
def producto(numero1,numero2):
    return numero1*numero2
def cociente(numero1,numero2):
	
    #excepción para evitar que se interrumpa la operación del programa cuando ingresa el número
    #cero que no está definido en un cociente

    try:
	    return numero1/numero2  
	
    except ZeroDivisionError:
        print("La división por cero no está definida")


print("Para ello, vamos a necesitar que ingreses dos números y solicites cualquiera de las operaciones que se te ofrece")
print("")

#excepción para evitar que se frene la ejecución del programa cuando el usuario ingrese una letra 
#en vez de un número

while True: 
    try: 
        num1=int(input("Ingrese el primer número: "))
        num2=int(input("Ingrese el segundo número: "))
        break

    except ValueError:
    	print("Los caracteres ingresados no son de tipo numérico")

opcion=input("¿Qué operación deseas realizar? : (suma, resta, producto o cociente) \n")
opcion_m=opcion.lower() #convierte en minúscula todo, para poder llamarlo en un solo caracter

if opcion_m=="suma":
	print("El valor de la suma de los dos números ingresados es: ", suma(num1,num2))
elif opcion_m=="resta":
	print("El valor de la resta entre los dos números ingresados es: ", resta(num1,num2))
elif opcion_m=="producto":
	print("El valor del producto entre los dos números ingresados es: ", producto(num1,num2))
elif opcion_m=="cociente":
	print("El valor del cociente entre los dos números ingresados es: ", cociente(num1,num2))

print("")
print("Ha finalizado con éxito el módulo uno, para continuar con el segundo módulo, necesitamos saber otros datos")
print("")
correoe=input("Ingrese su correo electrónico: ")
print("")

intento=0
while True: 
    
    intento=intento+1

    if "@" in correoe:
	    print("Bienvenido al módulo dos")
	    break
    
    else:
        print("El correo ingresado no es válido")
        correoe=input("Ingrese su correo electrónico: ")
	
    if intento==2:
        print("Haz ingresado demasiadas veces un correo que no es válido")
        break
		
#MODULO DOS
#Algunas cosas de estadística básica

#print("")
#print("PRUEBA DOS")
#("")


#for i in range(10):
    #numeros=input("Ingrese un número: ")

#numeros_mios=list(numeros)
#print(numeros_mios)

#MODULO TRES
#Programación orientada a objetos

print("")
print("PRUEBA TRES")
print("En este módulo vamos a indicarte cuánto debes pagar de impuestos en un país lleno de corruptos")
print("")

class declaracionI():

    def __init__(self):
        
        self.__nombre=input("Ingrese su nombre: ")
        self.__identificacion=input("Ingrese su número de identificación (sin comas, ni puntos): ")
        self.__contrato=input("Ingrese el número de su contrato laboral: ")
        self.__salario=int(input("Ingrese su salario básico: "))

    def confirmacionDatos(self):
        
        print("Los datos ingresados son: \n")
        print("Nombre: ", self.__nombre)
        print("Ideantificación: ", self.__identificacion)
        print("Número de contrato: ", self.__contrato)
        print("Salario: ")
        print("")
        
            
    def impuestos(self):
        
        if self.__salario<900000:
            self.impuestos=self.__salario*0.10
            print("Los impuestos que usted debe pagar corresponden a ", self.impuestos, " que son el 10% de su salario" )
        elif 900000<=self.__salario<1500000:
            self.impuestos=self.__salario*0.15
            print("Los impuestos que usted debe pagar corresponden a ", self.impuestos, " que son el 15% de su salario" )
        elif 1500000<=self.__salario<3000000:
            self.impuestos=self.__salario*0.18
            print("Los impuestos que usted debe pagar corresponden a ", self.impuestos, " que son el 18% de su salario" )
        elif self.__salario>=3000000:
            self.impuestos=self.__salario*0.20
            print("Los impuestos que usted debe pagar corresponden a ", self.impuestos, " que son el 20% de su salario" )


persona1=declaracionI()
print(persona1.impuestos())




















