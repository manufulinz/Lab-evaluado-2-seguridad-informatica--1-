import sys
import random

def AP():
    alpha =0
    while(alpha<=0):
        numeros = []
        for j in range (0,1000):
            numeros.append(j)
    
        cont = 0
        prime =[]
        for i in range(2, 1000+ 1):
            primos = True
            for j in range(2,11):
                if i == j:
                   break
                elif i%j == 0:
                   primos = False
                else:
                   continue
            if primos == True:
                prime.append(i)
                cont += 1

        p = random.choice(prime)
    
        alpha = p-random.choice(numeros)

    return ([p,alpha])
