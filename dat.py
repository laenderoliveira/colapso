import os
import re

print('[+]Coloque os arquivos originais *.dat na pasta dat/ .')
print('[+]Os arquivos gerados ficaram na raiz do programa.\n')
	

#Lista os arquivos da pasta dat/
files = os.listdir('dat')

if len(files) ==  0:
	print('[-]Coloque os arquivos na pasta dat/ e tente novamente')

for arq in files:
	#Regex captura o valor de L =  no nome do arquivo
	regex = re.compile('wDARL=(\d+)mol=')
	l = regex.search(arq)
	l = int(l.group(1))

	#Abre o arquivo em modo de leitura e faz a leitura dos dados
	dat = open('dat/' + arq, 'r')
	text = dat.readlines()
	dat.close() #Fecha o arqivo

	#Abre um novo arquivo em modo de escrita para gravar os novos dados
	dat = open('colapsado_' +arq, 'w')

	print(arq)
	print('L = {}'.format(l))
	try:
		print('[+]Prisione [ENTER] para continuar, ou CTRL + C para sair')
		input()
		#Pede os dados para fazer o calculo da primeira e segunda coluna
		divfirst = float(input('Valor para calcular a primeira coluna: '))
		divsecond = float(input('Valor para calcular a segunda coluna: '))
	except KeyboardInterrupt: #Entra na exeção se CTRL + C for precionado
		print('[-]Programa fechado')
		dat.close()
		os.remove('colapsado_' + arq) #Remove o arquivo incompleto
		break

	for line in text:
		line = line.strip() #Remove os espaços das laterais
		line = line.split('   ') #Divide os dois dados em uma lista
		first = str(int(line[0]) / l ** divfirst).rjust(21) #Divide o dados a primeira coluna e posiciona 
		second = str(float(line[1]) / l ** divsecond).ljust(21) #Divide o dados a segunda coluna e posiciona
		dat.write('{}   {}\n'.format(first, second))  #Escreve os dados no arquivo
	print('[+] {} Concluído!'.format(arq))
	print('=========================================================\n')

	dat.close() #Fecha o arquivo
	