#TP13 Tableaux 2 dim

A= [[ 2,1],
    [-1,3],
    [ 1,2]]

B= [[ 3,-1],
    [-2, 4],
    [ 5, 0]]

def affiche(M):
    for i in range(len(M)):
        print (M[i])

def prod(k,M):
    nblignes = len(M)
    nbcolonnes = len(M[0])
    resu=[ [0 for j in range (nbcolonnes)] for i in range (nblignes)]

    for i in range(nblignes):
    # pour chaque indice de ligne
        for j in range(nbcolonnes):
        # pour chaque indice de colonne
            resu[i][j] = k * M[i][j]
    return resu

def somme(M,N):
    nblignes = len(M)
    nbcolonnes = len(M[0])
    resu=[ [0 for j in range (nbcolonnes)] for i in range (nblignes)]
    for i in range(len(M)):
        for j in range(len(M[i])):
            resu[i][j]=(M[i][j] + N[i][j])
    return resu

print ("C = A + B")
affiche(somme(A,B))
print()
print ("D = A - B")
affiche(somme(A,prod(-1,B)))
print()
print ("E = 2A + 3B")
affiche(somme(prod(2,A),prod(3,B)))
print()
print ("F = 3A + 3B")
affiche(somme(prod(3,A),prod(3,B)))
