import random
import string 
col1 = []
col2 = []
col3 = []
col4 = []

ingrese = int(input("Ingrese la cantidad de lineas: "))
for i in range(ingrese):
    col1.append(random.randint(0,5000))
    col2.append(random.choice(string.ascii_letters))
    col3.append(random.randint(0,5000))
    col4.append(random.randint(0,5000))
name = input("Ingrese el nombre del archivo: ")
doc = open(name,'w')
for j in range(ingrese):
    doc.write('{}, {}, {}, {}\n'.format(col1[j],col2[j],col3[j], col4[j]))
doc.close()
