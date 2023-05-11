#citim o gramatica si un numar n
f = open('input.txt')
N = f.readline().split() #neterminale
T = f.readline().split() #terminale
P = int(f.readline()) #numarul de productii
S = f.readline().strip() #simbolul de start

D = {} #construim un dictionar in care sa tinem productiile
for i in range(P):
    productie = f.readline()
    valori = []
    indiceS = productie.find('>') #cautam capatul sagetii
    indiceF = productie.find('|') #cautam inceputul unei alte productii
    
    while indiceF != -1:
        valori.append(productie[indiceS + 2 : indiceF - 1].strip()) #strip ca sa nu luam si \n
        indiceS = indiceF
        indiceF = productie.find('|', indiceS + 1) #cautam urmatoarea productie

    valori.append(productie[indiceS + 2 :].strip()) #indiceS + 2 fiindca avem un spatiu
    
    if productie[0] in D:
        D[productie[0]].extend(valori)
    else:
        D[productie[0]] = valori


#pastram valorile subproblemelor rezolvate intr-un dictionar in dictionar =)
R = {x : {} for x in N}


l = 0 #pornim de la lungimea = 0 si o tot crestem pana ajungem la n
for x in N:
    if '^' in D[x]:
        R[x] = {0 : ['']}
l += 1

vremSaContinuam = 1
lmax = 1 
#tinem minte pana unde am generat pana acum, ca sa nu generam valorile pt 1-n daca am mai facut-o

while vremSaContinuam:
    n = int(input("Dati n: ")) #citim n

    l = lmax #pornim de unde am ramas
    while l <= n:
        #calculam pt neterminale toate cuv de lungime l pe care le genereaza
        for x in N:
            for prod in D[x]:
                terminale = True #verificam daca avem doar terminale in productie
                if prod[len(prod) - 1] in N:
                    terminale = False
                if prod == '^':
                    prod = ''
                if terminale and len(prod) == l:
                    if l in R[x]:
                        R[x][l].append(prod)
                    else:
                        R[x][l] = [prod]
                elif terminale == False:
                    sim_term = prod[:len(prod) - 1]
                    simbol_urm = prod[len(prod) - 1]
                    lungime_ramasa = l - (len(prod) - 1) #minus neterminalul
                    if lungime_ramasa in R[simbol_urm]:
                        if l not in R[x]:
                            R[x][l] = []
                        for cuv in R[simbol_urm][lungime_ramasa]:
                            R[x][l].append(sim_term + cuv)
        l += 1

    lmax = n + 1

    #afisam doar cuvintele generate de simbolul de start
    if n not in R[S]:
        print("Nu putem genera cuvinte de lungimea data")
    else:
        if n != 0:
            print("Putem genera urmatoarele cuvinte de lungime", n)
            for cuv in R[S][n]:
                print(cuv, end = ' ')
        else:
            print("Putem genera cuvantul vid: \n^")

    vremSaContinuam = int(input("\nDoriti sa mai introduceti o lungime n? [0/1]: "))

