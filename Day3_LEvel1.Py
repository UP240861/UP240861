edad= int(input("ingrese su edad:"))
altura= float(input("ingrese su altura:"))
x = (8j)
print()
base = float(input("ingrese la base:"))
Altura = float(input("ingrese altura:"))
total = base * Altura
print("El resultado es: ",total)
print()
a = float(input("ingresa lado A:"))
b = float(input("ingrese lado B:"))
c = float(input("ingrese lado C:"))
perimetro = a + b + c
print(perimetro)
print()
r = float(input('cual es el radio?:'))
pi = 3.1416
area = pi*r**2
circ = 2*pi * r
print("su area es: ",area)
print("su circunferencia es: ", circ)
print()
print("\n Pendiente e intersecciones de y = 2x - 2")
m = 2
b = -2
x_intercepcion = -b / m
print(f"Pendiente (m): {m}")
print(f"Intersección con Y (b): {b} → Punto (0, {b})")
print(f"Intersección con X: y=0 → x={x_intercepcion} → Punto ({x_intercepcion}, 0)")

print("\nPendiente y distancia entre (2,2) y (6,10)")
x1, y1 = 2, 2
x2, y2 = 6, 10
pendiente = (y2 - y1) / (x2 - x1)
distancia = ((x2 - x1)**2 + (y2 - y1)**2)**0.5
print(f"Pendiente: {pendiente}")
print(f"Distancia euclidiana: {distancia:.3f}")

print("\n Comparación de pendientes")
print(f"¿Las pendientes son iguales? {m == pendiente}")

print("\nRaíces de y = x² + 6x + 9")
def encontrar_raiz():
    for x in range(-10, 10):
        y = x2 + 6*x + 9
        if y == 0:
            return x
    return None

raiz = encontrar_raiz()
print(f"Cuando y=0, x={raiz}")

print("\nLongitud de palabras")
python_len = len("python")
dragon_len = len("perro")
print(f"Longitud 'python': {python_len}")
print(f"Longitud 'perro': {dragon_len}")
print(f"Comparación falsa: ¿Son diferentes? {python_len != dragon_len}")  # Falsa porque son iguales

print("\nVerificar 'on' en palabras")
print("¿'on' está en 'python' y 'dragon'?", "on" in "python" and "on" in "dragon")

print("\nDetección de jerga")
oracion = "Espero que este curso no esté lleno de jerga."
print("¿La oración contiene jerga?", "jerga" in oracion)

print("\nConversión de longitud")
longitud = len("Python")
print(f"Longitud como float: {float(longitud)}")
print(f"Longitud como string: '{str(longitud)}'")

print("Verificar número par ")
numero = 4
print(f"¿{numero} es par? {numero % 2 == 0}")

print("Comparaciones ")
print("¿7/3 == int(2.7)?", 7/3 == int(2.7))
print("¿type('10') == type(10)?", type('10') == type(10))
print("¿int(float('9.8')) == 10?", int(float('9.8')) == 10)
print("\nCalculadora de salario ")
horas = float(input("\nIngrese horas trabajadas: "))
tarifa = float(input("Ingrese tarifa por hora: "))
print(f"Salario: {horas * tarifa:.2f}")

print("\nCalculadora de tiempo de vida ")
años = int(input("\nIngrese años vividos: "))
segundos = años * 365 * 24 * 60 * 60
print(f"Segundos vividos: {segundos:,}")

print("\nTabla")
print("\n1\t1\t1\t1\t1")
print("2\t1\t2\t4\t8")
print("3\t1\t3\t9\t27")
print("4\t1\t4\t16\t64")
print("5\t1\t5\t25\t125")# ultimo
