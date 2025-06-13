cadena_concatenada = 'treinta' +' '+ 'dais' +' '+ ' '+ 'de' + ' ' + 'paython'
print(cadena_concatenada)
#2
cadena_con = 'codificacion' + ' ' + 'para' + ' ' + 'todos'
print(cadena_con)
#3
Empresa = "Codificacion para todos"
#4 
print(Empresa)
#5
print (len(Empresa))
#6
print(Empresa.upper())
#7
print (Empresa.lower())
#8
print("capitalize: ",Empresa.capitalize())
print('title: ', Empresa.title())
print("swapcase: ",Empresa.swapcase())
#9
primera_palabra = Empresa.split()[0]
print(primera_palabra)
#10
palabra = 'Codificacion' 
if palabra in Empresa:
    print(f'"{palabra} "esta en la cadena: ') 
else:
    print (f'"{palabra}) "no esta en la cadena: ')
#11
cadena_modificada = cadena_con.replace("codificacion", "Paython")
print(cadena_modificada)
#12
cadena_modificada2 = cadena_modificada.replace("todos", "siempre")
print (cadena_modificada2)
#13
print(Empresa.split())
resultado = cadena_con.split (' ') 
print (resultado)
#14
cadena_num1 = "Facebook Google Microsoft Apple IBM Oracle Amazon"
result = cadena_num1.split(' ')
print (result)
#15
cadena = 'codificacion para todos'
caracter = cadena [0]
print (caracter)
#16
ultimo_indice = len (cadena) - 1
print ('ultimo indice es: ', ultimo_indice)
#17
caracter = cadena [10]
print (caracter)
#18
acronimo = cadena_modificada2
print(cadena_modificada2[0],cadena_modificada2[7],cadena_modificada2[12])
#19
acronim = cadena
print(cadena[0], cadena[13], cadena[18])
#20
posicion = Empresa.find('C')
print(posicion)
#21
posicion = Empresa.find('f')
print(posicion)
#22
variable = 'codigo para toda la gente'
posicion1 = variable.find('l')
print(posicion1)
#23
frase = 'No se puede terminar una oración con "because" porque es una conjunción'
posicion2 = frase.find('because')
print(posicion2)
#24
posicion2 = frase.rindex('because')
print(posicion2)
#25
frase_modificada = frase.replace('"because"porque es una conjunción', " ")
print(frase_modificada)
#26
falla = 'No puedes terminar una oración con porque porque porque es una conjunción'
encontrada = falla.find('porque')
print(encontrada)
#27
falla2 = falla.replace('porque porque porque','')
print(falla2)

#28
resultado = Empresa.startswith('Codificacion')
print (resultado)
#29
resultado = Empresa.endswith('Codificacion')
print (resultado)
#30
frase3 = 'codificacion para todos'
result2 = frase3.strip()
print(result2)
#31
print("30daysOfPaython".isidentifier())
print('thirteen_days_of_python'.isidentifier())
#32
biblioteca = ['Django', 'Flask', 'Bottle', 'Pyramid', 'Falcon']
result3 = ' # '.join(biblioteca)
print(result3)
#33
print('I am enjoying this challenge.\nI just wonder what is next.')
#34
print("Nombre\t\tEdad\tPais\t\tCiudad")
print("Angel    \t19\tMexico\t\tAguascalientes")
#35
radio = 10
area = 3.14 * radio ** 2
mensaje = "El area de un circulo con radio de {} es {} metros cuadrados.".format(radio, int(area))
print(mensaje)
#36
a = 8
b = 6

print(f"{a} + {b} = {a + b}")
print(f"{a} - {b} = {a - b}")
print(f"{a} * {b} = {a * b}")
print(f"{a} / {b} = {a / b:.2f}")
print(f"{a} % {b} = {a % b}")
print(f"{a} // {b} = {a // b}")
print(f"{a} ** {b}={a**b}")