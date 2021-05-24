'''
    Função que lê um arquivo texto contendo uma lista de endereços IP 
    Separa em 2 arquivos, IP válidos e não válidos 
    O formato de um endereço IP é numn.num.num.num (num = 0 a 255).
'''

ip = open("ip.txt","r") #abrir arquivo contendo lista de IPs
lista = ip.readlines() #cria uma lista e lê o arquivo linha a linha
ip.close() #fechar arquivo

ipvalido = "" #criar lista de IP válido
ipnaovalido = "" #criar lista de IP não válido

for i in range (len(lista)): #percorrer a lista de acordo com o numero de IPs
    lista2 = lista[i].rsplit(".") #criar uma 2º lista contendo o IPs da 1º lista separados por "."
    #confere todas as posições dos IPs e ve se estaão dentro do padrão de 0 à 255
    if (int(lista2[0])<=255 and int(lista2[1])<=255 and int(lista2[2])<=255 and int(lista2[3])<=255):
        ipvalido += lista[i] + "\n" #se for válido vai para listade Ips válidos
    else:
        ipnaovalido += lista[i] + "\n" #senão vai para a lista dos não válidos
 
ip = open("ipvalido.txt","w") #cria um arquivo txt com os IPs válidos
ip.write(ipvalido)
ip.close()
 
ip = open("ipnaovalido.txt","w") #cria um arquivo txt com os IPs não válidos
ip.write(ipnaovalido)
ip.close()
 
print ("arquivos gerados com sucesso!")