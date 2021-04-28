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

    






