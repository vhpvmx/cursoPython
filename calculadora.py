import sys
#print('[' + type(e).__name__ + ']', str(e))
if len(sys.argv) != 4:
    print('Tienes que colocar dos numeros mas algun signo para hacer alguna operacion ejemplo:python calculadora.py 2 + 2 o puedes poner signo de resta si es lo que quieres o algun otro signo')
    print("Puedes poner sumas, restas, divisiones, y multiplicaciones")
else:

    signo = sys.argv[2]
    print("signo", signo)

    try:
        num1 = float(sys.argv[1])
        print("num1", num1)
    except Exception as e:
        print("El primer numero no es valido")
        num1 = 0

    try:
        num2 = float(sys.argv[3])
        print("num2", num2)
    except Exception as e:
        print("El segundo numero no es valido")
        num2 = 0

    if signo == "+":
        resultado = num1 + num2
        print ("resultado", resultado)
    elif signo == "-":
        resultado = num1 - num2
        print ("resultado", resultado)
    elif signo == "/":
        resultado = num1 / num2
        print ("resultado", resultado)
    elif signo == "*":
        resultado = num1 * num2
        print("resultado",resultado)
    else:
        print("Las operaciones disponibles son suma, resta, multiplicacion y division")
#try:
    # op2 = int(sys.argv[2])
#except Exception as e:
    # op2 = 6

#try:
    # op3 = sys.argv[3]
#except Exception as e:
    # op3 = ""
