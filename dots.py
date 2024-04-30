from math import sin, cos, radians, sqrt
from sys import argv
import matplotlib.pyplot as plt
import numpy as np

# Modificações
angulo = 45 #graus
diametro = 2 #metros
maxZ = 0.5
minZ = -0.5

raio = 0.5*diametro

# Do gráfico
NGridX = 30
NGridY = 30
DeslXPos = 5
DeslXNeg = -3
DeslYPos = 3
DeslYNeg = -3

# Calculos
elementos = {
	"$radiusNeg"		: -raio,
	"$radiusBlock "		: 3*raio,
	"$radiusBlockNeg"	: -3*raio,
	"$aNeg"				: -raio*cos(radians(angulo)),
	"$a "				: raio*cos(radians(angulo)),
	"$b "				: raio*sin(radians(angulo)),
	"$bNeg"				: -raio*cos(radians(angulo)),
	"$L "				: 16*raio, 
	"$LNeg"				: -16*raio, 
	"$Lback"			: 3*16*raio,
	"$Lfront"			: -16*raio,
	"$radius "			: raio,
	"$c "				: 3*raio*cos(radians(angulo)),
	"$cNeg"				: -3*raio*cos(radians(angulo)),
	"$d "				: 3*raio*sin(radians(angulo)),
	"$dNeg"				: -3*raio*sin(radians(angulo)),
	"$minZ"				: minZ,
	"$maxZ"				: maxZ,
	"("					: "",
	")"					: ""
}

# Substitui cada item no dicionário elemento por seu respectivo valor
def substituir(string):
	for i, j in elementos.items():
		string = string.replace(i, str(j) + "  " )
		
	return string

def tratar():
	
	pontos = []
	
	# Abre o aquivo e faz o tratamento
	with open("ler", "r") as arquivo:
		for i in arquivo:
			pontos.append(substituir(i).split())
	
	# faz o parse de string para float
	pontos = list(map( (lambda x: list(map(lambda y : float(y), x)) ), pontos))
	
	if "-f" in argv:
		with open("pontos", "w") as arquivo:
			for i in pontos:	
				arquivo.write(str(i[0]) + "\t\t\t\t\t\t" + str(i[1]) + "\t\t\t\t\t\t" + str(i[2]) + "\n")
	
	return pontos


def main():
	
	pontos = tratar()
	x = []
	y = []
	for lista in pontos:
		if lista[2] == 0.5:
			x.append(lista[0])
			y.append(lista[1])
	
	# Unindo pontos
	
	# Linhas superiores
	plt.plot([min(x), max(x)], [min(y), min(y)], color="black")	
	plt.plot([min(x), max(x)], [max(y), max(y)], color="black")
	
	# Linhas laterais
	plt.plot([min(x), min(x)], [min(y), max(y)], color="black")	
	plt.plot([max(x), max(x)], [min(y), max(y)], color="black")
	
	# Separando os cilindros
	cilindro_interno = [];
	cilindro_externo = [];
	
	for i in range(len(x)):
		if sqrt( x[i]**2 + y[i]**2) == raio:
			cilindro_interno.append([x[i], y[i]])
		
		if sqrt( x[i]**2 + y[i]**2) == 3*raio:
			cilindro_externo.append([x[i], y[i]])
			
	# Unindo os pontos entre o cilindro externo e o dominio
	for i in range(len(cilindro_externo)):
		for j in range(len(x)):
			if x[j] == cilindro_externo[i][0] and abs(y[j] + cilindro_externo[i][1]) == abs(y[j]) + abs(cilindro_externo[i][1]) and [x[j],y[j]] not in cilindro_interno :
				plt.plot([ x[j], cilindro_externo[i][0]], [y[j], cilindro_externo[i][1]], color="black") 
				
			if y[j] == cilindro_externo[i][1] and abs(x[j] + cilindro_externo[i][0]) == abs(x[j]) + abs(cilindro_externo[i][0]) and [x[j],y[j]] not in cilindro_interno:
				plt.plot([ x[j], cilindro_externo[i][0]], [y[j], cilindro_externo[i][1]], color="black")
	
	# Conectando o cilindro externo com o interno
	for i in range(len(cilindro_interno)):
		plt.plot([cilindro_interno[i][0], 3*cilindro_interno[i][0]], [cilindro_interno[i][1], 3*cilindro_interno[i][1]], color="black")
		
	# Fechando o cilindro interno
	for i in range(len(cilindro_interno)):
		plt.plot([raio*cos(i*radians(angulo)), raio*cos((i+1)*radians(angulo))], [raio*sin(i*radians(angulo)), raio*sin((i+1)*radians(angulo))], color="black")
		
	# Fechando o cilindro externo
	for i in range(len(cilindro_externo)):
		plt.plot([3*raio*cos(i*radians(angulo)), 3*raio*cos((i+1)*radians(angulo))], [3*raio*sin(i*radians(angulo)), 3*raio*sin((i+1)*radians(angulo))], color="black")
	
	# Plotando os pontos
	for i in range(len(x)):
		plt.plot(x[i], y[i], marker="o", color="black")
		
	# Apenas estética
	#plt.grid(visible=True, color="grey", linestyle="-", linewidth=".2", animated=True)

	#plt.xticks( np.arange(min(x) + DeslXNeg, max(x) + DeslXPos, step=((abs(min(x))+abs(max(x))) / NGridX ) ), [])
	
	#plt.yticks( np.arange(min(y) + DeslYNeg, max(y) + DeslYPos, step=((abs(min(y))+abs(max(y))) / NGridY ) ), [])	
	
	plt.xticks([min(x), 0, max(x)])
	plt.yticks([min(y), 0, max(y)])	

	plt.show()

main()



