import sys

try:
    num1 = int(sys.argv[1])
except Exception as e:
    num1 = 0

print(num1)
try:
    num2 = int(sys.argv[2])
except Exception as e:
    num2 = 0
print("num2")

try:
    op3 = (sys.argv[3])
except Exception as e:
    op3 = ""
print("op3")
#aqui me da un error enfrente del signo de +
if op3 == "+"
print("num1 + num2 = num1 num2")
