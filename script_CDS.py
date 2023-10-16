#!/usr/bin/env python3

#Exercício 4

#Importar sys
import sys

#Receber os dados da linha de comando e transformá-los para string para serem testados
dna = str(sys.argv[1])
n1 = str(sys.argv[2])
n2 = str(sys.argv[3])
n3 = str(sys.argv[4])
n4 = str(sys.argv[5])
n5 = str(sys.argv[6])
n6 = str(sys.argv[7])

#Verificar se os tipos de dados estão corretos
if not dna.isalpha():
 print ("Atenção: A sequência de DNA deve apresentar apenas letras") #checa se a string tem somente letras em sua composição
 sys.exit() #para de rodar caso as condições não forem atendidas

if not (n1.isdigit() and n2.isdigit() and n3.isdigit() and n4.isdigit() and n5.isdigit() and n6.isdigit()):
 print ("Atenção: dados  n1, n2, n3, n4, n5 e n6 precisam ser números inteiros e positivos") #checa se a string tem somente números em sua composição
 sys.exit()

#Converter números para inteiros
n1 = int(n1)
n2 = int(n2)
n3 = int(n3)
n4 = int(n4)
n5 = int(n5)
n6 = int(n6)

if len(dna) < (n1 and n2 and n3 and n3 and n4 and n5 and n6):
 print ("Atenção: dados precisam ser menores que a sequência de DNA")
 sys.exit()

#Extrair CDS 1 da sequência de DNA e conferir se começa com ATG

CDS1 = dna [n1-1 : n2] #Subtrair 1 para igualar índice python (que se inicia em 0) com o número da base do DNA
if dna[n1-1 : n1+2] != "ATG" :
 print ("Atenção: CDS 1 deve iniciar com o códon ATG")
 sys.exit()

#Extrair CDS 2
CDS2 = dna [n3-1 : n4]

#Extrair CDS 3 e conferir se termina com TAG, TAA ou TGA. Caso sim, concatenar as três CDS.
CDS3 = dna [n5-1 : n6]
if dna[n6-3 : n6] == "TAG" or dna[n6-3 : n6] == "TAA" or dna[n6-3 : n6] == "TGA":
 print (CDS1 + CDS2 + CDS3)
else:
 print ("Atenção: CDS 3 deve terminar em TAG, TAA ou TGA")
