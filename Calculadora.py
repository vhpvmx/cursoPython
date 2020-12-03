import sys
try:
    op1 = int(sys.argv[1])
except Exception as e:
    #print('[' + type(e).__name__ + ']', str(e))
    print("Tienes que colocar un numero")

    op1=0
print("El parametro cero es:", sys.argv[0])
print("op1", op1)

try:
    op2 = int(sys.argv[2])
except Exception as e:
    #print('[' + type(e).__name__ + ']', str(e))
    print("Ingresa un numero para que este bien")

    op2=0
print("El parametro cero es:", sys.argv[0])
print("op2", op2)


#try:
    # op2 = int(sys.argv[2])
#except Exception as e:
    # op2 = 6

#try:
    # op3 = sys.argv[3]
#except Exception as e:
    # op3 = ""
