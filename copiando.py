import os
import sys

with open('prem1.tex', 'r') as f1:
 	linf1 = f1.readlines()

with open('prem2.tex', 'r') as f2:
	linf2 = f2.readlines()

with open('prem3.tex', 'r') as f3:
 	linf3 = f3.readlines()

with open('prem4.tex', 'r') as f4:
	linf4 = f4.readlines()


#tomo las longitudes de los tex y me quedo con el largo maximo
a=len(linf1)
b=len(linf2)
c=len(linf3)
d=len(linf4)

largo_maximo=max(a,b,c,d)


#creo una lista que va tener en sus entradas las lineas del nuevo tex
#la letra 'q' es para ver restos de la lista original
felicesLos4=['q\n']*largo_maximo

#copiamos las lineas de los 4 tex de '4 en 4' (multiplos de 4)
#sumarle 1, 2 o 3 hace que empecemos en lugares distintos
for i in range(largo_maximo):
	if 4*i+3 < largo_maximo:

		felicesLos4[4*i]=linf1[i]
		felicesLos4[4*i+1]=linf2[i]
		felicesLos4[4*i+2]=linf3[i]
		felicesLos4[4*i+3]=linf4[i]

#escribimos las lineas en un archivo nuevo
with open('mezcla.tex', 'w') as file:
	file.writelines(felicesLos4)



