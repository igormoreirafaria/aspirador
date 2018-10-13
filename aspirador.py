from random import *
import random

def move(estado_atual, sala_anterior, possiveis_movimentos):
	
	lista_destino = possiveis_movimentos[estado_atual[0]].copy()

	lista_destino.remove(sala_anterior)

	sala_anterior = estado_atual[0]
	destino = random.choice(lista_destino)
	estado_atual[0] = destino
	return estado_atual, sala_anterior

def chama_busca(estado_atual, fila, sala_anterior, possiveis_movimentos):

		
	if( estado_atual[estado_atual[0]] == 's'):
		estado_atual[estado_atual[0]] = 'l'
		fila.append(estado_atual[0])
		
	elif(estado_atual[estado_atual[0]] == 'l'):
		estado_atual, sala_anterior = move(estado_atual, sala_anterior, possiveis_movimentos)

	return estado_atual,sala_anterior

def checar_objetivo(estado_atual, estados_objetivos):
	for x in range(9):
		if(estado_atual == estados_objetivos[x]):
			print('objetivo alcancado')
			return True

	print('nao alcancou o objetivo')			
	return False

def main():

	estado_atual = [randint(1,9), random.choice(['s', 'l']), 
								random.choice(['s', 'l']), 
								random.choice(['s', 'l']),
								random.choice(['s', 'l']),
								random.choice(['s', 'l']),
								random.choice(['s', 'l']),
								random.choice(['s', 'l']),
								random.choice(['s', 'l']),
								random.choice(['s', 'l'])]
	fila = []

	for x in range(0,10):
		if(estado_atual[x] == 'l'):
			fila.append(x)

	estados_objetivos = { 0:[1, 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l'], 
						1:[2, 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l'],
						2:[3, 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l'],
						3:[4, 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l'],
						4:[5, 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l'],
						5:[6, 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l'],
						6:[7, 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l'],
						7:[8, 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l'],
						8:[9, 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l', 'l'] }


	possiveis_movimentos = {1:[2,4], 2:[1,3,5], 3:[2,6], 4:[1,5,7], 
							5:[2,4,6,8], 6:[3,5,9], 7:[4,8], 8:[5,7,9], 
							9:[6,8]}

	print(estado_atual)

	sucesso = False
	
	i = 0

	sala_anterior = random.choice(possiveis_movimentos[estado_atual[0]])
	while(checar_objetivo(estado_atual, estados_objetivos) != True ):
		estado_atual,sala_anterior = chama_busca(estado_atual, fila, sala_anterior, possiveis_movimentos)
		print(estado_atual)
		i = i + 1
		if (i == 3):
			chance = randint(0,100)
			if (chance > 50):
				estado_atual[fila[0]] = 's'
				print(f'sujou sala {fila[0]}')
				del fila[0]
			elif (chance > 75):
				estado_atual[fila[1]] = 's'
				print(f'sujou sala {fila[0]}')
				del fila[1]
			elif (chance > 95):
				estado_atual[fila[2]] = 's'
				print(f'sujou sala {fila[0]}')
				del fila[2]	
			i = 0


if __name__ == '__main__':
	main()