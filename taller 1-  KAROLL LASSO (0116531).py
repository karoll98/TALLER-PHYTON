#TALLER
#KAROLL DANIELA LASSO FERNANDEZ
#CODIGO:116531
#1121220561

#%% PUNTO 1
numero = float(input('favor ingresar un numero = '))

absolute_val = (numero ** 2) ** 0.5

print('valor absoluto del numero ingresado es :',absolute_val )

# float, para decimal y enteros, Se Pide el numero a calcular su valor abs
x = float(input("por favor ingrese un numero:")) 
# se imprime x si es positivo
if x >= 0 :
   print('su numero en valor absoluto es :',x)
# si es negativo se *-1, se imprime x
else:
   x=x*-1
   print('su numero en valor absoluto es :',x)

#%% PUNTO 2
import math #funcion math operaciones aritmeticas
numero = float(input('favor ingresar un numero = ')) # llamamos variables
numero2 = float(input('favor ingresar un numero = ')) # llamamos variables
dif=numero - numero2    
dif= int(math.sqrt(dif*dif))
print(dif) #imprimimos comando para la pperacion
contador = 0
for i in range(1,dif+1): # ciclo
    if (dif% i)==0:  # condicion
        contador = contador + 1 

if contador==2:  # segunda condicion
    print("el numero es primo")
else:
    print("el numero no es primo") #imprimir resultado
  
   
#%% PUNTO 3
def multiple(valor, multiple):
    """
    Funcion para calcular si el numero es multiplo
    utilizando el modulo de la division
    """
    resto = valor % multiple
    if resto == 0:
        return True
    else:
        return False
 
# lista que contendra los valores multiples
multiples_3=[]
multiples_4=[]
 
# bucle del 1 al 100
for i in range(1,101):
 
    if multiple(i,3) and len(multiples_3)<16:
        multiples_3.append(i)
        x =i

for j in range(x,101): #ciclo for para la condicion
    if multiple(j,4):  # realizamos condicion
        multiples_4.append(j)
    
 
print ("Los multiples de 3 son: " , multiples_3) #imprimimimos 

print ("Los multiples de 4 son: ", multiples_4) # imprimimos 


#%% PUNTO 4
import math # funcion math ejecutar operaciones aritmeticas 
print("digite las cordenadas de origen y el radio del circulo1")
numeros1=input() #creamos variables
arreglo1=numeros1.split() # variable 2 
print(arreglo1) # imprimimos 
print("digite las cordenadas de origen y el radio del circulo2") # imprimimos
numeros2=input() # segunda condicion de varibles
arreglo2=numeros2.split()
print(arreglo2)
print("digite las cordenadas del punto") #imprimimos para coordenadas 
numeros3=input() # tercera condicion de variables 
arreglo3=numeros3.split()
print(arreglo3)
print(arreglo3[1]) #imprimimos para coordenadas 
d1=math.sqrt(math.pow(((int)(arreglo3[0])-((int)(arreglo1[0]))),2)
+math.pow((((int)(arreglo3[1]))-((int)(arreglo1[1]))),2))
d2=math.sqrt(math.pow(((int)(arreglo3[0])-((int)(arreglo2[0]))),2)
+math.pow((((int)(arreglo3[1]))-((int)(arreglo2[1]))),2))
if(d1<(((int)(arreglo1[2])) and d2<((int)(arreglo2[2])))) : #secuencia circulos
       print("el punto está entre ambos circulos") # imprimimos funcion
else:
       if(d1<((int)(arreglo1[2]))):
          print("el punto está dentro del circulo 1")
       if(d2<((int)(arreglo2[2]))):
            print("el punto está dentro del circulo 1")
       else:
            print("el punto no está dentro de ningun circulo")
        

#%% CADENAS
# PUNTO 5
import keyword  #importamos biblioteca
texto= input("escriba una palabra") #creamos variable
M="AEIOUÁÉÍÓÚ" # variable
S1=[]
for i in range(0, len(texto)): # ciclo
   if texto[i] in M:  #condicion
       S1.append(texto[i])
print ("tiene", len(S1),"vocales mayusculas") #imprimimos

MT="ÁÉÍÓÚáéíóú" #variable
S2=[]
for i in range(0, len(texto)): #ciclo
   if texto[i] in MT: #condicion
       S2.append(texto[i])
print ("tiene", len(S2),"vocales con tilde") #imprimimos

num="0123456789" # variable 
S3=[]
for i in range(0, len(texto)): #ciclo
   if texto[i] in num: #condicion
       S3.append(texto[i])
print ("tiene", len(S3),"digitos") #imprimimos


espacio= " "
S4=[]
for i in range(0, len(texto)):
   if texto[i] in espacio: #condicion
       S4.append(texto[i])
print ("tiene", len(S4),"espacios")

S5=texto.split()
S6=[]
for i in range(0, len(S5)):
   if [i] in keyword.kwlist: #condicion
       S6.append(S5[i])
print (S6,"son keywords contenidas en la palabra digitada") #imprimir resultado
   
#%% PUNTO 6

print("digite la cadena") # imprimimos cadena
cadena=input() # variable de cadena 
cadena=cadena.replace(' ', '') #ejecutamos la cadena
lista=[]   # llamamos lista 
for i in cadena: # ciclo
    lista.append(i) # variables
    lista.sort()
cadena2=''   # llamamos variable a la segunda cadena
for i in lista: # ciclo
    cadena2 +=i # condicion aritmetica
print(cadena2) # imprimimos 

#%% LISTAS 
#PUNTO 7
   
print("digite el arreglo") # imprima un digito
cadena=input() # crea cadena
cadena=cadena.replace(' ', '')
lista=[] # crea lista 
for i in cadena: # condiciona
    lista.append(i)
    lista.sort()
cadena2=''
for i in lista:
    cadena2 +=i
if(cadena != cadena2):
    print("la lista no está ordenada")
else:
    print("digite el valor a ingresar a la lista")
    num=input()
    lista.append(num)
    lista.sort()
print(lista) # imprima la lista 


#%% PUNTO 8
print("digite el arreglo") # digite arreglo lo imprime
cadena=[]
cadena=input().split()
cadena1=[]
for i in cadena: # condicion 
    cadena1.append(int(i))
lista_nueva = [] # crea lista 
for i in cadena1:
    if i not in lista_nueva: # condicion 
        lista_nueva.append(i)
lista_nueva.remove(max(lista_nueva))
print(max(lista_nueva)) # imprimir la lista 
   
#%% PUNTO 9
   
numero = int(input("Ingresa un numero: ")) # crear variables 
pausa = int(input("Ingresa la cantidad de numeros: "))
nume=0
while numero != 1:
    nume=nume+1
    if numero % 2 == 0: # condicion 
        print("%d," % (numero), end = "") # imprimir 
        numero = numero / 2
    else:
        print("%d," % (numero), end = "") # imprimir 
        numero = (numero * 3) + 1

    if numero == 1: # condicion
        print("1") # imprimir si 
    if(nume == pausa):
        break   

#%% PUNTO 10
    
import random  # importa comando random
n = int(5) # variable
matriz=[None]*n # genera matriz 
for i in range(0,n): # condicion 
    matriz[i] = [None]*n
for i in range(0,n):
    for j in range(0,n):
        matriz[i][j] = (int)(random.randint(1,1001))
print(matriz) # imprima la matriz 
for i in range(n-1,-1,-1):
    if(i%2==0):
        for j in range(n-1,-1,-1):
            print (matriz[j][i])
    else:
        for j in range(0,n):
            print (matriz[j][i])  # imprima matriz en lista 


#%% PUNTO 11
def rectangulo(ancho, alto, letra): # definir condiciones
    for i in range(alto): # condicion altura
        for j in range(ancho): # condicion ancho
            print(letra, end=" ")
        print() # imprima condiciones 

anchura = int(input("Anchura del rectángulo: ")) # variables 
altura = int(input("Altura del rectángulo: "))
caracter = input("Carácter a utilizar: ")
rectangulo(anchura, altura, caracter)  
   

#%% PUNTO 12
def triangulo(altura): # definimos altura del triangulo
    for i in range(1, altura + 1): # condicion aritmetica
        for j in range(i):
            print("* ", end="") # imprimimos
        print()

tamano = int(input("Altura del triángulo: ")) # condicion de tamaño
triangulo(tamano)

#%% PUNTO 13
def evalua_int():                  #la función no tiene parametros de entrada
    while True:                    # mientras sea verdad el ciclo se va 
                                   #a repetir:  
        try:                       #1) evaluar la variable num
            num=int(input('--> ')) #2) si el valor ingresado es un int el ciclo
            break                  #se finalizara con un break
        except ValueError:         #3) sino muestra error
                                   #en este caso es el mensaje al usario
            print('no es un número entero, intentalo otra vez')
                                   # esto se repite hasta que se ingrese un int          
            
    return(num)                    #retorno valor de la variable num
    


def añosbisiesto():            # funcion sin parametros 
    print('Escriba un año')    # informacion dada por el usuario
    num1=evalua_int()          #verifca el número ingresado
    while True:                #ciclo de repeticion para garantizar que el num2
                               #sea mayor que el num1
         print('Por favor escriba otro año, posterior al año ',num1)
         num2=evalua_int()     #evalua y valida el num2 mediante la 
                               #función evalua_int 
         if num1>num2:         #compara los valores ingresados si num1>num2
                               #el programa arroja el mesaje al usuario para 
                               #que se modifique 
             print(num2, 'No es mayor que ',num1,'intentelo de nuevo --> ')
         else:                 #de lo contrario los valores ingresados son los 
             break             #solicitados y el ciclo se cierra con un break
            
    cont=0                       #inicialización del contador para años bisiestos 
    for i in range(num1,num2+1): #evaluación de todos los años en el rango 
        if i%4==0:               #si es múltiplo de 4 significa que es bisiesto
            cont+=1              #y se agrega una unidad al contador 
    
    #resultado listo para imprimir 
    R='Entre los años',num1,'y',num2,'hay',num2-num1+1,'años,',cont,
    'de ellos son bisiestos'
    return(R)    
    
                          
print(*añosbisiesto())               #se llama a la función añobisiesto

        
#%%PUNTO 14.
import random # importamos funcion random
aciertos=0 # damos restriccion
while(True):
    num1=random.randint(0, 100) #creamos variables 
    num2=random.randint(0, 100)
    print("adivine la suma de los numeros " + str(num1) + " y "+str(num2))
    respueta_in=int(input())
    respuesta_real=num1+num2
    if(respueta_in==respuesta_real):
        aciertos=aciertos+1  #condicion
    else:
        aciertos=0 
    if(aciertos==5):
        break
    print("sus aciertos son: " + str(aciertos))
print("usted acerto 5 veces :D")  # imprimimos 


#%% PUNTO 15
def main(): # definimos comando 
    while True:
        cadena = int(input ("Dime la longitud de la cadena: ")) # realizamos cadena
        if cadena<2 or cadena>9: # condiciones
            print('digite un numero entre 2 y 9')
        if cadena>=2 and cadena<=9:
            break       
    numeros= ('0','1','2','3','4','5','6','7','8','9') # variable numeros
    codigo=''
    for i in range(cadena): # ciclo
        elegido= random.choice(numeros)
        codigo= str(codigo + elegido)
    print(codigo) # imprimimos
    
    eleccion = input ("Intenta adivinar la cadena: ")
    while codigo != eleccion:
        aciertos =0

        for i in range(cadena-1):
            if eleccion[i]==codigo[i]:
                aciertos = aciertos+1
                print('tienes ',aciertos,' aciertos')
            else:
                print('no acertaste')
        eleccion = input ("Intenta adivinar la cadena otra vez: ")
    print('felicidades adivinaste el numero!')
main()



