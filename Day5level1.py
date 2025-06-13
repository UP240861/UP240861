#1.
lista_vacio=[]

#2.
fruts=['pitaya','ciruelas',"uvas","naranjas"]

#3.
print(len(fruts))

#4.

print(fruts[0])                
print(fruts[len(fruts)//2])   
print(fruts[-1])               

#5.
mixed_data_types=['Angel Roberto Alonso Guerrro', 19, 1.67, 'Soltero', 'Jardines de casa blanca']

#6.
Emprezas=['Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon']

#7.
print(Emprezas)

#8.
print(len(Emprezas))

#9.
print(Emprezas[0])                
print(Emprezas[len(Emprezas)//2]) 
print(Emprezas[-1])  

#10.
Emprezas[1]='Alfabeto'

#11.
Emprezas.append('Twitter')
print(Emprezas)

#12.
medio=len(Emprezas)//2
Emprezas.insert(medio,'intel')
print(Emprezas)

#13.
Emprezas[0]=Emprezas[0].upper()
print(Emprezas)

#14.
print('#;'.join(Emprezas))

#15
print('google' in Emprezas)

#16.
Emprezas.sort()
print(Emprezas)

#17
Emprezas.reverse()
print(Emprezas)

#18
print(Emprezas[:3])

#19
print(Emprezas[:-3])

#20
long = len(Emprezas)
if long % 2 == 1:
    print([Emprezas[long//2]])
else:
    print(Emprezas[long//2-1:long//2+1])

#21
Emprezas.pop(0)
print(Emprezas)

#22.
medio = len(Emprezas)//2
if len(Emprezas)%2==1:
    Emprezas.pop(medio)
else:
    Emprezas.pop(medio)
    Emprezas.pop(medio-1)
print(Emprezas)

#23
Emprezas.pop()
print(Emprezas)

#24
Emprezas.clear()
print(Emprezas)

#25
del Emprezas

#26.
front_end = ['HTML', 'CSS', 'JS', 'React', 'Redux']
back_end = ['Node', 'Express', 'MongoDB']
lleno = front_end + back_end
print(lleno)

#27
index_redux = lleno.index('Redux')
lleno.insert(index_redux + 1, 'Python')