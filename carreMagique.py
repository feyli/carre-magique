from math import sqrt

# Question n°1
"M6 = (6*(6**2+1))/2"
"M6 = (6*37)/2"
"M6 = 222/2"
"M6 = 111"
"La constante magique pour n = 6 est égale à 111."
"A = 22"
"B = 36"
"C = 35"

# Question n°2

from math import sqrt

def afficheCarre(tab):
    width = sqrt(len(tab))
    assert (len(tab) % width == 0), "Il ne s'agit pas d'un carré"
    width = int(width)
    for i in range(0, len(tab), width):
        print(*tab[i:i+width])
    
afficheCarre([8, 1, 6, 3, 5, 7, 4, 9, 2])
 
#Question n°3

"""
a) La liste du carré magique complémentaire de l'exemple est :

[-2,-9,-4,-7,-5,-3,-6,-1,-8]

b) La liste du carré magique complémentaire du carré de 6x6 est :

[-2, -36, -31, -11, -18, -13, -34, -5, -30, -16, -14, -12, -6, -28, -35, -15, -10, -17, -29, -9, -4, -20, -27, -22, -7, -32, -3, -25, -23, -21, -33, -1, -8, -24, -19, -26]

"""

# Question n°4


def calculCarreMagiqueComplementaire(listeCarre):
    listeCarreComplementaire = []
    Longueur = sqrt(len(listeCarre))
    
    if len(listeCarre) % Longueur == 0 :
        
        for element in listeCarre:
            listeCarreComplementaire.append(element-((Longueur**2)+1))
        
        return listeCarreComplementaire

    else :

        print("Le tableau indiqué n'est pas à dimentiion carré")
        return None

assert calculCarreMagiqueComplementaire([8,1,6,3,5,7,4,9,2]) == [-2,-9,-4,-7,-5,-3,-6,-1,-8]

# Question n°5

#S = “ La somme des ´eléments de L est egale a n x Mn”
#C = "La liste L correspond à un carré magique"

# S => C
# Si S est vraie

# Pour que la liste L soit reconnu comme un carré magique il faut que 
# la somme des lignes soit égale a Mn et que la somme totale des éléments
# de la liste L(n x n) soit aussi égale a n x Mn.

# Si S est vrai, donc que la somme des élements de L est bien égale a
# n x Mn, ca ne veut pas forcement dire que la somme (diagonal, lignes, colonnes)
# soit forcément égale a Mn.
#On peut donc dire que l'implication S => C est fausse

[5, 5, 5]
[5, 10, 0]
[5, 0, 10]

# La somme de chaques lignes est bien égale a 15 mais la diagonal non = 20
# La somme de tout les élements de L est 5+5+5+5+10+0+5+0+10=45



# La somme est égale 



# C => S
# Si C est vraie

# La définition d'un carré magiqe nous dit que la somme magique est égale a n x Mn donc
# par logique, si tout la sommes des éle

# Question 6






# Question 7

def isCarreMagique_neuf():
    listCarre = []
    nombreElementListe = 9

    for _ in range(nombreElementListe):
        element = float(input("Choisir un nombre :"))
        listCarre.append(element)
        
    print(listCarre)
    
    # Check if the list has exactly 9 elements
    if len(listCarre) != 9:
        return False
    
    # Calculate the magic constant for a 3x3 magic square
    constanteMagique = sum(listCarre) / 3
    
    # Check rows
    for i in range(0, 9, 3):
        if sum(listCarre[i:i+3]) != constanteMagique:
            return False
    
    # Check columns
    for i in range(3):
        if sum(listCarre[i::3]) != constanteMagique:
            return False
    
    # Check diagonals
    if (listCarre[0] + listCarre[4] + listCarre[8] != constanteMagique or
        listCarre[2] + listCarre[4] + listCarre[6] != constanteMagique):
        return False
    
    return True

print(isCarreMagique_neuf())
    
# Question 8

def isCarreMagique_seize():
    listCarre = []
    nombreElementListe = 16

    for _ in range(nombreElementListe):
        element = float(input("Choisir un nombre :"))
        listCarre.append(element)
        
    print(listCarre)
    
    # Vérification si la ligne a 16 éléments
    if len(listCarre) != 16:
        return False
    
    # Consttante magique pour un carré de 4x4
    constanteMagique = sum(listCarre) / 4
    
    # Vérification des lignes
    for i in range(0, 16, 4):
        if sum(listCarre[i:i+4]) != constanteMagique:
            return False
    
    # Vérification des colonnes
    for i in range(4):
        if sum(listCarre[i::4]) != constanteMagique:
            return False
    
        if (listCarre[0] + listCarre[5] + listCarre[10] + listCarre[15] != constanteMagique or
        listCarre[3] + listCarre[6] + listCarre[9] + listCarre[12] != constanteMagique):
            return False
    
    return True
            
            







            
# Question 9

"""          
En utilisant la programme de la question 7 :
La deuxiéme liste n'est pas un carré magique.
La premiére liste n'est pas un carré magique.



# Question 10
"""

def isCarreMagique_n(tab):
    taille = len(tab)
    largeur = sqrt(taille)
        
    print(tab)
    
    # Constante magique pour un carré de largeurxlargeur
    constanteMagique = sum(tab) / largeur
    
    # Vérification des lignes
    for i in range(0, taille, largeur):
        if sum(tab[i:i+largeur]) != constanteMagique:
            return False
    
    # Vérification des colonnes
    for i in range(largeur):
        if sum(tab[i::largeur]) != constanteMagique:
            return False
    
        if (tab[0] + tab[(i*largeur)+1] + tab[(i*largeur)+1] + tab[(i*largeur)+1] != constanteMagique or
        tab[(i*largeur)-1] + tab[(i*largeur)-1] + tab[(i*largeur)-1] + tab[(i*largeur)-1] != constanteMagique):
            return False
    
    return True

