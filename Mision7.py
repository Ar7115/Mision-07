#Autor: Luis Armando Miranda Alcocer
# Menú con 2 programas: dividir y encontrar mayor

def dividir(dividendo, divisor):
    cociente = 1 #Inicia en 1 por ser acumulador.
    residuo = 0
    while dividendo-divisor >= residuo: #Se realizará la resta del dividendo menos el divisor mientras el resultado sea mayor o igual al residuo (positivo)
        cociente = cociente + 1 #Contador, aumenta hasta que finalice el while. Número de veces que se realiza la resta
        residuo = divisor * cociente #Para calcular el residuo, la cantidad a restar para obtener cuánto sobra
    residuo=dividendo-residuo #Se resta el dividendo inicial, menos el monto para obtener el residuo
    print(dividendo,"/",divisor,"=",cociente,", sobra", residuo)


def encontrarMayor():
    datos = []  # lista vacía
    print("Teclea una serie de números para encontrar el mayor. ")
    numero = int(input("Valor [-1 termina]: ")) #Se pide un número diferente a -1
    if numero == -1: #Si el número es -1, imprime que no hay valor mayor
        #datos.append(numero)
        print ("No hay valor mayor")

    else: #Si no es -1...
        while numero != -1:  #Y mientras no sea igual a -1, se repetirá una y otra vez
            datos.append(numero) #Se irán agregando números a una lista
            numero = int(input("Valor [-1 termina: "))
        print("El mayor es: ",max(datos)) #Imprime el número mayor


def main():
    opcion = -1 #Para que se cumpla la condición de while
    while opcion != 0: #Menú, mientras seleccion no sea 0, se repetirá el menú

        print("Misión 07. Ciclos while ")
        print("Autor: Luis Armando Miranda Alcocer")
        print("Matricula: A01377115 ")
        print("1. Calcular divisiones ")
        print("2. Encontrar el mayor ")
        print("3. Salir ")
        opcion = int(input("Teclea tu opción: ")) #Se escoge qué programa abrir, si se teclea 3, termina el programa
        print(" ")

        if opcion ==1: #Si se selecciona un 1, funciona el primer programa.
            print ("Calcula divisiones")
            dividendo = int(input("Dividendo: "))
            divisor = int(input("Divisor: "))
            dividir(dividendo, divisor) #Llama a la función
            print(" ")

        elif opcion ==2: #Si se selecciona un 2, funciona el segundo programa.
            encontrarMayor() #Llama a la función
            print(" ")

        elif opcion==3: #Si se selecciona un 3, termina el programa.
            print("Gracias por usar este programa, regresa pronto.")
            break

        else:
            print("ERROR, teclea 1, 2 o 3") #Si es un número diferente, dice que vuelva a intentarlo con números válidos
            print(" ")

main()