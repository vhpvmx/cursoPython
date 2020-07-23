import random
import mysql.connector
import dogs
import sys

#Define que funcion vamos a ejecutar
op1 = int(sys.argv[1])
#Define el rango de los dados
op2 = int(sys.argv[2])

print("las opciones recibidas como parametros son op1:", op1, "op2:", op2)
print("op1 1 -- inicializar()")
print("op1 2 -- definir_personaje()")
print('op1 3 -- definir_actividad("Caballero")')
print("op1 4 -- dados(op2)")


db = "calabozos"
try:
    mydb = mysql.connector.connect(
      host = "localhost",
      user = dogs.db_user,
      passwd = dogs.db_passwd,
      database = db
    )
    mycursor = mydb.cursor(buffered=True)

except Exception as e:
    print('[1] msg original de error: ', )
    print('[' + type(e).__name__ + ']', str(e))
    print('error conectandose a la BD')


def definir_actividad(personaje):
    opcion = random.randint(1, 5)
    print ("opcion:", opcion)

    if personaje == "Caballero":
        if opcion == 1:
            print("Vencer a un dragon")
        elif opcion == 2:
            print("Defender al rey")
        elif opcion == 3:
            print("A bailar")
        elif opcion == 4:
            print("Te toca ir por las pizzas")
        elif opcion == 5:
            jugador = random.randint(1, 10)
            print("el jugador: ", jugador, "define la actividad")

    if personaje == "Mago":
        if opcion == 1:
            print("Derrotar a un ejercito de duendes")
        elif opcion == 2:
            print("se convierte en burro")
        elif opcion == 3:
            print("baila el gallinazo")
        elif opcion == 4:
            print("tiene que ser el esclavo de alguien mas")
        elif opcion == 5:
            jugador = random.randint(0,10)
            print("el juagador:",jugador,"define la actvidad")

#definir_actividad("Caballero")

#Recibe el rango superior
#Imprime dos numeros aleatorios que no sobrepasen el rango superior
#el numero sup debe ser un 6 o 12, 18 o 24 si es distinto debe imprimir un msj que diga que numeros deben ser
def dados(rango):
    print("")
    #6, 12, 18, 24
    #pensar en otra forma de validarlo
    #if rango == 6 or rango == 12 or rango == 18 or rango == 24:
    if not (rango % 6) and rango <=24 :
        print("El rango es correcto, el numero elegido fue:", rango)
        num1 = random.randint(1, rango)
        num2 = random.randint(1, rango)
        print("El primer numero aleatorio es:", num1, "el segundo numero aleatorio es:", num2, "la suma de ambos es:", num1+num2)
    else:
        print("Debes elegir como rango superior uno de estos numeros: 6, 12, 18 o 24, el numero elegido fue:", rango)


#dados(24)
#dados(30)

def definir_personaje():
    #esta funcion asiganara un personaje de forma aleatoria a la persona que ejecute el programa
    #que pasa si el personaje ya se asigno
    opcion = random.randint(1, 4)
    print("opcion:", opcion)
    try:
        mycursor.execute("SELECT estatus, descripcion FROM asignacionPersonajes where id = %s", (opcion,))
        myresult = mycursor.fetchone()
        estatus = int(myresult[0])
        descripcion = myresult[1]
    except Exception as e:
        print('[2] msg original de error: ', )
        print('[' + type(e).__name__ + ']', str(e))
        print('error consultando la tabla de asignacion de personajes')

    if opcion == 1:
        if estatus == 0:
            print("Tu personaje es:", descripcion)
            mycursor.execute("UPDATE asignacionPersonajes SET estatus = 1 where id = %s", (opcion,))
            mydb.commit()
        else:
            print("El personaje:", descripcion, "ya esta asignado")
            mycursor.execute("SELECT count(*) FROM asignacionPersonajes where estatus = 0" )
            myresult = mycursor.fetchone()
            count_libre = int(myresult[0])
            if count_libre > 0:
                definir_personaje()
            else:
                print("Ya todos los personajes estan asignados")

    elif opcion == 2:
        if estatus == 0:
            print("Tu personaje es:", descripcion)
            mycursor.execute("UPDATE asignacionPersonajes SET estatus = 1 where id = %s", (opcion,))
            mydb.commit()
        else:
            print("El personaje:", descripcion, "ya esta asignado")
            mycursor.execute("SELECT count(*) FROM asignacionPersonajes where estatus = 0" )
            myresult = mycursor.fetchone()
            count_libre = int(myresult[0])
            if count_libre > 0:
                definir_personaje()
            else:
                print("Ya todos los personajes estan asignados")

    elif opcion == 3:
        if estatus == 0:
            print("Tu personaje es:", descripcion)
            mycursor.execute("UPDATE asignacionPersonajes SET estatus = 1 where id = %s", (opcion,))
            mydb.commit()
        else:
            print("El personaje:", descripcion, "ya esta asignado")
            mycursor.execute("SELECT count(*) FROM asignacionPersonajes where estatus = 0" )
            myresult = mycursor.fetchone()
            count_libre = int(myresult[0])
            if count_libre > 0:
                definir_personaje()
            else:
                print("Ya todos los personajes estan asignados")

    elif opcion == 4:
        if estatus == 0:
            print("Tu personaje es:", descripcion)
            mycursor.execute("UPDATE asignacionPersonajes SET estatus = 1 where id = %s", (opcion,))
            mydb.commit()
        else:
            print("El personaje:", descripcion, "ya esta asignado")
            mycursor.execute("SELECT count(*) FROM asignacionPersonajes where estatus = 0" )
            myresult = mycursor.fetchone()
            count_libre = int(myresult[0])
            if count_libre > 0:
                definir_personaje()
            else:
                print("Ya todos los personajes estan asignados")


#definir_personaje()

def inicializar():
    #Libera a los personajes en la BD
    print("Los personajes han sido liberados")
    mycursor.execute("UPDATE asignacionPersonajes SET estatus = 0")
    mydb.commit()


def ejecucionFunciones(op):
    print("op:", op)
    if op == 1:
        print("a")
        inicializar()
    elif op == 2:
        definir_personaje()
    elif op == 3:
        definir_actividad("Caballero")
    elif op == 4:
        dados(op2)

ejecucionFunciones(op1)
