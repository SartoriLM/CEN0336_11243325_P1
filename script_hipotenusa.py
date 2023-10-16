#!/usr/bin/env python3

#Exercício 3

#Importar sys
import sys

#Receber os dados do usuário da linha de comando
a = (sys.argv[1])
b = (sys.argv[2])

#Transformar dados em string para rodar o comando isdigit
a = str (a)
b = str (b)

#Verificar se os dados reebidos do usuário são do tipo adequado (número interio positivo)
if not (a.isdigit() and b.isdigit()):
 print ("Os dados inseridos precisam ser números inteiros e positivos")
 sys.exit() #parar de rodar caso as condições ideas não forem atendidas

#Transformar dados em inteiros
a = int(a)
b = int(b)

#Verificar se dados são menor que 500, como estabelecido pelo exercício
if a <= 0 or a >= 500 or b <= 0 or b >= 500:
 print ("Os dados devem ser menores que 500")
 sys.exit()

#Calcular quadrado da hipotenusa
q_hipotenusa = a*a + b*b

#Imprimir resultado
print ("O quadrado da hipotenusa para o triângulo retângulo com lados a=" , a , "e b=" , b, "é", q_hipotenusa)



