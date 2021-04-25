print("Formulario básico de acceso al sistema \n")
print("¿Cuál es tú nombre? \n")
nombre=str(input())
print("")
print(nombre,",","Bienvenido a nuestra plataforma")
print("Para empezar, queremos saber cuál es tú edad: \n")
edad=int(input())
print("")
restriccion="Nuestro requisito principal es ser mayor de edad"
if edad<18:
	print("No cumples con las características para continuar en el sistema \n")
else:    
    print("Podemos empezar con mostrarte lo siguiente: \n")
    capitales={"Francia":"París", "Colombia":"Bogotá", "Alemania":"Berlín", "Reino Unido":"Londres", "España":"Madrid", "Ecuador":"Quito"}
    print("Pregúntanos por la capital de cualquier país \n")
    pregunta1usuario=input()

    print("")
    print("La capital de ", pregunta1usuario, "es", capitales[pregunta1usuario])
    print("")
    print("También podemos realizar operaciones matemáticas")
    print("Por ejemplo: vamos a sumar los primeros números enteros hasta el valor que nos indiques")
    N=int(input("Ingresa un número: \n"))
    suma=0
    for i in range(1,N+1):
    	suma = suma+i
    print("El valor de la suma es ", suma)
    print("")
    print("Ahora vamos a hacerte una serie de preguntas para validar tu identidad \n")
    respuesta1=input("¿Estarías dispuesto a realizar un préstamo con nosotros? SI/NO \n")
    if respuesta1=="SI":
        valorprestar=int(input("Ingrese el monto a solicitar: \n"))
        if valorprestar>=1000000:
            valorprestar=valorprestar*0.5
            print("El monto solicitado es de categoría A y tiene una tasa de interés anual del 50%")
            print("El total de su pago sería de: ",valorprestar)
        if valorprestar<1000000:
            valorprestar=valorprestar*0.1
            print("El monto solicitado es de categoría B y tiene una tasa de interés anual del 10%")
            print("El total de su pago sería de: ",valorprestar)
    else:
    	print("Váyase a la mierda")

 
    
#print("Podemos empezar con mostrarte lo siguiente: \n")
#capitales={"Francia":"París", "Colombia":"Bogotá", "Alemania":"Berlín", "Reino Unido":"Londres", "España":"Madrid", "Ecuador":"Quito"}
#print("Pregúntanos por la capital de cualquier país \n")
#pregunta1usuario=input()

