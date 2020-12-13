import sys
try:
    op1 = int(sys.argv[1])
    op2 = sys.argv[2]
    op3 = int(sys.argv[3])
except Exception as e:
    #print('[' + type(e).__name__ + ']', str(e))
    print('Tienes que colocar dos numeros mas algun signo para hacer alguna operacion ejemplo:python calculadora.py 2 + 2 o puedes poner signo de resta si es lo que quieres o algun otro signo')
    print("Puedes poner sumas, restas, divisiones, y multiplicaciones")
    op3 = "+,*,/"
    op1=-1
    op2=-1

print("op1", op1)
print("op2", op2)
print("op3",op3)

#try:
    # op2 = int(sys.argv[2])
#except Exception as e:
    # op2 = 6

#try:
    # op3 = sys.argv[3]
#except Exception as e:
    # op3 = ""
