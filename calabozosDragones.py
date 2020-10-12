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

#Conexion a la BD
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

#Esta funcion asigna la actividad que va a realizar el jugador
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
            #PENDIENTE: regresarte un numero aleatorio donde el rango superior sea el numero de jugadores
            jugador = random.randint(1, 10)
            print("el jugador: ", jugador, "define la actividad")
    elif personaje == "Mago":
        if opcion == 1:
            print("Derrotar a un ejercito de duendes")
        elif opcion == 2:
            print("se convierte en burro")
        elif opcion == 3:
            print("baila el gallinazo")
        elif opcion == 4:
            print("tiene que ser el esclavo de alguien mas")
        elif opcion == 5:
            jugador = random.randint(1,10)
            print("el jugador:",jugador,"define la actvidad")
    elif personaje == "Dragon":
        if opcion == 1:
            print("Inventa un producto para el mal aliento e intenta venderlo, tienes 30 secs para prepararte y 2 mins para venderlo")
        elif opcion == 2:
            print("cuentanos como venciste al ultimo principe")
        elif opcion == 3:
            print("describe una receta de cocina que lleve principes y caballeros")
        elif opcion == 4:
            print("baila la peluza")
        elif opcion == 5:
            rand = random.randint(1,5)
            print("salta:",rand,"veces")
    elif personaje == "Atleta":
        if opcion == 1:
            rand = random.randint(1,10)
            print("Haz:", rand, "sentadillas")
        elif opcion == 2:
            print("Narra como ganaste la final mundial de 100 metros libres")
        elif opcion == 3:
            print("baila la cancion de rocky")
        elif opcion == 4:
            rand = random.randint(1,5)
            print("haz:", rand, "lagartijas")
        elif opcion == 5:
            print("Vendenos un producto imaginario para convertirse en atleta, tienes 30 secs para prepararte y 2 minutos para vendernos el producto")
    #PENDIENTE: Definir mas personajes
    #PENDIENTE: agregar las actividades para el ninja, del demogorgon



#ejemplo de una llamada a la funcion
#definir_actividad("Caballero")

#La funcion dados recibe el rango superior
#Imprime dos numeros aleatorios que no sobrepasen el rango superior
#el rango sup debe ser un 6 o 12, 18 o 24 si es distinto debe imprimir un msj que diga que numeros deben ser
def dados(rango):
    print("")
    #pensar en otra forma de validarlo
    #if rango == 6 or rango == 12 or rango == 18 or rango == 24:
    if not (rango % 6) and rango <=24 :
        print("El rango es correcto, el numero elegido fue:", rango)
        num1 = random.randint(1, rango)
        num2 = random.randint(1, rango)
        print("El primer numero aleatorio es:", num1, "el segundo numero aleatorio es:", num2, "la suma de ambos es:", num1+num2)
    else:
        print("Debes elegir como rango superior uno de estos numeros: 6, 12, 18 o 24, el numero elegido fue:", rango)

#Ejemplo de la llamada a la funcion dados
#dados(24)
#dados(30)

#Esta funcion asiganara un personaje de forma aleatoria a la persona que ejecute el programa
def definir_personaje():
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

#Ejemplo de la llamada a la funcion
#definir_personaje()

#Libera a los personajes en la BD
def inicializar():
    print("Los personajes han sido liberados")
    mycursor.execute("UPDATE asignacionPersonajes SET estatus = 0")
    mydb.commit()

#Salvar que personaje te quedo asignado
#en la bd deber guardarse el id de jugador asignado en la partida actual y el personaje asignado en esta partida
#instalar mysql - BD
#aprender como pasar los cambios del master al branch personal desde atom
#crear una funcion que se ejecute cada 15 mins con un reto para todo el equipo
#Ejecutar el programa de forma local

def ejecucionFunciones(op):
    print("op:", op)
    if op == 1:
        print("a")
        inicializar()
    elif op == 2:
        definir_personaje()
    elif op == 3:
        #PENDIENTE: Mandar como parametro el personaje que ejecuta la funcion
        definir_actividad("Caballero")
    elif op == 4:
        dados(op2)

ejecucionFunciones(op1)
