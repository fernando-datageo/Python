# -*- coding: utf-8 -*-
"""
Programa que recebe como entrada dois arquivos:
O primeiro arquivo contém nomes de alunos
O segundo arquivo contém as notas dos alunos
E será gerado um terceiro arquivo contendo as médias.
"""
def acertarNotas(aluno,nota):
    f1 = open(aluno,"r") # Abre no modo leitura o arquivo com os nomes
    f2 = open(nota,"r") # Abre no modo leitura o arquivo com as notas
    listanota = [] # Cria uma lista a ser preenchida com as notas
    texto = f1.readlines() # Lê todas as linahs do arquivo nota
    for i in texto:
        notas = f2.readline().split() # separa as notas em linha em lista de strings
        valores = [float(val) for val in notas] # Transforma as notas em valores float
        media = sum(valores) / len(valores) # Soma os valores e cria uma média sobre eles
        todos= i+" "+str(notas)+" "+str(media)+"\n" # Cria uma lista  de nomes concatenados com suas médias
        listanota.append(todos) # Adiciona a lista de notas
    f1.close()
    f2.close()
    arquivo=open('listanotas','w') # Cria uma arquivo para salvar as execuções realizadas
    arquivo.writelines(listanota) # Transcreve as informações no arquivo
    arquivo.close()
    return
acertarNotas("aluno.csv","nota.csv") # Chama afunção criada com os arquivos externos