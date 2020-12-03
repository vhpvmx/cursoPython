import random
import mysql.connector
import dogs
import sys

try:
    op1 = int(sys.argv[1])
except Exception as e:
    op1 = 1000

try:
    op2 = int(sys.argv[2])
except Exception as e:
    op2 = 6

try:
    op3 = sys.argv[3]
except Exception as e:
    op3 = ""


print("op3:", op3)
print("Las opciones disponibles en el sistema son:")
print("op1 1 -- inicializar()")
print("op1 2 -- definir_personaje()")
print("op1 3 -- definir_actividad()")
print("op1 4 -- dados(op2)")

if op1 == 1000:
    print("")
    print('No has enviado los parametros iniciales, debes ejecutar el programa con dos parametros, el primero indica la funcion a realizar y el segundo el rango de los dados')

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

def definir_actividad(jugador):
    mycursor.execute("SELECT id, descripcion FROM asignacionPersonajes where jugador = %s", (jugador,))
    myresult = mycursor.fetchone()
    id = int(myresult[0])
    personaje = myresult[1]

    mycursor.execute("SELECT count(*) FROM asignacionPersonajes where estatus = 1")
    myresult = mycursor.fetchone()
    num_jugadores = int(myresult[0])

    opcion = random.randint(1, 5)
    print ("jugador:", jugador, "- personaje:", personaje, "- opcion:", opcion)

    if personaje == "Caballero":
        if opcion == 1:
            print("Vencer a un dragon")
        elif opcion == 2:
            print("Defender al rey")
        elif opcion == 3:
            print("A bailar")
        elif opcion == 4:
            print("Blandir espada")
        elif opcion == 5:
            try:
                id_jugador_l = random.randint(1, num_jugadores)
                if id_jugador_l == id:
                    if id_jugador_l > 1:
                        id_jugador_l = id_jugador_l - 1
                    else:
                        id_jugador_l = id_jugador_l + 1

                mycursor.execute("SELECT descripcion FROM asignacionPersonajes where id = %s", (id_jugador_l,))
                myresult = mycursor.fetchone()
                personaje_l = myresult[0]
                print(personaje_l, "define la actividad")
            except Exception as e:
                print('[1] msg original de error: ', )
                print('[' + type(e).__name__ + ']', str(e))
                print("jugador_l:", jugador_l)
                #Hacer este mensaje dinamico usando las variables opcion y personaje
                print('error ejecutando la actividad 5 para el caballero')

    elif personaje == "Mago":
        if opcion == 1:
            print("Derrotar a un ejercito de duendes")
        elif opcion == 2:
            print("se convierte en burro")
        elif opcion == 3:
            print("Hace truco de magia")
        elif opcion == 4:
            print("Ejecuta una bola de fuego")
        elif opcion == 5:
            jugador = random.randint(0,10)
            print("el jugador:",jugador,"define la actvidad")
    if personaje == "Demogorgon":
        if opcion == 1:
            print("Sacar los dientes")
        elif opcion == 2:
            print("Morder")
        elif opcion == 3:
            print("Escapar bajo tierra")
        elif opcion == 4:
            print("A cantar")
        elif opcion == 5:
            print("Tendras que responder una pregunta")
            print("el jugador:",jugador,"define la actvidad")
    if personaje == "Troll":
        if opcion == 1:
            print ("Golpeas con tu basto")
        elif opcion == 2:
            print ("Los demas jugadores te ponen una operacion matematica")
        elif opcion == 3:
            print ("Tendras que luchar con cazador de trolls")
        elif opcion == 4:
            print ("Podras aliarte con alguien,pero cuidate las espaldas porque te podria traicionar en cualquier momento")
        elif opcion == 5:
            print ("Sales a cazar")
        elif opcion == 6:
print ("Imita la voz de tu personaje")
elif opcion == 7:
print ("Peleas")
elif opcion == 8:
print ("Escapar")
elif opcion == 9:
print ("Cantar alguna cancion a votacion de los participantes")
elif opcion == 10:
jugador = random.randint(1, 10)
print("el jugador: ", jugador, "define la actividad")
elif personaje == "Dragon":
if opcion == 1:
print("Lanzas fuego")
elif opcion == 2:
print("Cuenta algo chistoso")
elif opcion == 3:
print("Emprendes el vuelo")
elif opcion == 4:
prin("Canta tusa")
elif opcion == 5:
rand = random.randint(1,5)
print("salta:",rand,"veces")
print("el jugador:",jugador,"define la actvidad")
elif personaje == "Atleta":
if opcion == 1:
rand = random.randint(1,10)
print("Haz:", rand, "30 sentadillas")
elif opcion == 2:
print("Corres")
elif opcion == 3:
print("baila la cancion de rocky")
elif opcion == 4:
rand = random.randint(1,5)
print("haz:", rand, "lagartijas")
elif opcion == 5:
print("Haz 20 crunch")
elif personaje == "Samurai":
if opcion == 1:
print("Sacar katana")
elif opcion == 2:
print("Pelear")
elif opcion == 3:
print("Defender Honor")
elif opcion == 4:
print("ayudar compañeros")
elif opcion == 5:
jugador = random.randint(0,10)
print("el jugador:",jugador,"define la actvidad")
elif personaje == "Ninja":
if opcion == 1:
print("Lanzar shurikens y kunai´s")
elif opcion == 2:
print("Escapar")
elif opcion == 3:
print("Movimiento especial")
elif opcion == 4:
print("Bailar el mariachi loco")
elif opcion == 5:
jugador = random.randint(0,10)
print("el jugador:",jugador,"define la actvidad")
elif personaje == "enano de lucha libre":
if opcion == 1:
print("haz una vuelta de panda")
if opcion == 2:
print("Ponte disfraz de keMonito")
elif personaje == "Cantante":
if opcion == 1:
print("Agredece que has ganado el grammy latino")
elif opcion == 2:
print("Pon a todo el equipo un ejercicio de vocalizacion")
elif opcion == 3:
print("Beatbox time!!")
elif opcion == 4:
rand = random.randint(1,5)
print("Cantanos una cumbia!")
elif opcion == 5:
print("Canta tu cancion favorita")


def dados(rango):
    print("")
if (rango == 6 or rango == 12 or rango == 18 or rango == 24) and rango != 0:
#if not ((rango % 6) and rango <=24) and rango != 0 :
print("El rango es correcto, el numero elegido fue:", rango)
num1 = random.randint(1, rango)
num2 = random.randint(1, rango)
print("El primer numero aleatorio es:", num1, "el segundo numero aleatorio es:", num2, "la suma de ambos es:", num1+num2)
else:
print("Debes elegir como rango superior uno de estos numeros: 6, 12, 18 o 24, el numero elegido fue:", rango)


def definir_personaje(jugador):
#PENDIENTE CONSULTAR A LA BD CUANTOS PERSONAJES EXISTEN
num_max_personajes = 4
opcion = random.randint(1, num_max_personajes)
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

if estatus == 0:
print(jugador, "tu personaje es:", descripcion)
mycursor.execute("UPDATE asignacionPersonajes SET estatus = 1, jugador = %s where id = %s", (jugador, opcion,))
mydb.commit()
else:
print("El personaje:", descripcion, "ya esta asignado")
mycursor.execute("SELECT count(*) FROM asignacionPersonajes where estatus = 0" )
myresult = mycursor.fetchone()
count_libre = int(myresult[0])
if count_libre > 0:
definir_personaje(jugador)
else:
print("Ya todos los personajes estan asignados")


def inicializar():
print("Los personajes han sido liberados")
mycursor.execute("UPDATE asignacionPersonajes SET estatus = 0, jugador = ''")
mydb.commit()

def ejecucionFunciones(op):
if op == 1:
print("a")
inicializar()
elif op == 2:
definir_personaje(op3)
elif op == 3:
definir_actividad(op3)
elif op == 4:
dados(op2)
elif op == 1000:
print('Ejecuta de nuevo el programa, recuerda enviar los parametros!!!')

#Ejecucion
ejecucionFunciones(op1)