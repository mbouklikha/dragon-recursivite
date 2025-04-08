from tkinter import *
from random import *
from math import *


# Interface graphique:
fenetre = Tk()
fenetre.config(background='lavender', width=800, height=600)

canevas = Canvas(fenetre, background='black', width=400, height=400)
canevas.place(x=300, y=10)


# Class:
class coord:
    def __init__(self, i, j):
        self.x = i
        self.y = j

    def __add__(self, other):
        return coord(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return coord(self.x - other.x, self.y - other.y)

    def __mul__(self, other: int):
        return coord(self.x * other, self.y * other)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __str__(self):
        return "( " + str(self.x) + " ; " + str(self.y) + " )"


class crayon:
    def __init__(self, xx, yy, couleur):
        self.pos = coord(xx, yy)
        self.couleur = couleur
        self.ang = 0
        self.dir = coord(1, 0)

    def tourne(self, angle):
        self.ang = self.ang + angle
        self.dir = coord(cos((self.ang / 180) * pi), sin((self.ang / 180) * pi))

    def avance(self, distance):
        p = self.pos
        self.pos = self.pos + self.dir * distance
        return canevas.create_line(p.x, p.y, self.pos.x, self.pos.y, fill=self.couleur)


class Pile:
    def __init__(self):
        self.valeurs = []

    def est_vide(self):
        return self.valeurs == []

    def empile(self, valeur):
        self.valeurs.append(valeur)

    def depile(self):
        if self.valeurs:
            return self.valeurs.pop()

    def __str__(self):
        ch = ''
        for x in self.valeurs:
            ch = "| " + str(x) + " |" + "\n" + ch
        return ch + "-----\n"


class File:
    def __init__(self):
        self.valeurs = []

    def enfile(self, valeur):
        self.valeurs.append(valeur)

    def defile(self):
        if self.valeurs:
            return self.valeurs.pop(0)

    def est_vide(self):
        return self.valeurs == []

    def longueur(self):
        return len(self.valeurs)

    def __str__(self):
        ch = ""
        for x in self.valeurs:
            ch = ch + " <- " + str(x)
        return ch

    def __iter__(self):
        return iter(self.valeurs)

###################################################################################################

# Variables pour le choix du mode et du sous-mode
mode_selectionne = ""
sous_mode_selectionne = ""
iterations = 0

# Fonctions pour choisir le mode
def choisir_mode_r():
    '''Cette fonction est appelée lorsqu'on clique sur le bouton "1 - Récursivité".'''
    global mode_selectionne
    mode_selectionne = "1 - Récursivité"


def choisir_mode_l():
    '''Cette fonction est appelée lorsqu'on clique sur le bouton "2 - L-Systèmes".'''
    global mode_selectionne
    mode_selectionne = "2 - L-Systèmes"


def choisir_mode_p():
    '''Description : Cette fonction est appelée lorsqu'on clique sur le bouton "3 - Pliages".'''
    global mode_selectionne
    mode_selectionne = "3 - Pliages"


# Fonctions pour choisir le sous-mode
def choisir_sous_mode_tri():
    '''Cette fonction est appelée lorsqu'on clique sur le bouton "▶ Triangle de Sierpinski" dans le
     mode "1 - Récursivité". '''
    global sous_mode_selectionne
    sous_mode_selectionne = "Triangle de Sierpinski"


def choisir_sous_mode_emp():
    ''' Cette fonction est appelée lorsqu'on clique sur le bouton "▶ Éponge de Menger" dans le
    mode "1 - Récursivité". '''
    global sous_mode_selectionne
    sous_mode_selectionne = "Éponge de Menger"

def choisir_sous_mode_koch():
    '''Cette fonction est appelée lorsqu'on clique sur le bouton "▶ Koch" dans le
    mode "2 - L-Systèmes".'''
    global sous_mode_selectionne
    sous_mode_selectionne = "Koch"

def choisir_sous_mode_gosper():
    '''Cette fonction est appelée lorsqu'on clique sur le bouton "▶ Gosper" dans le
    mode "2 - L-Systèmes". '''
    global sous_mode_selectionne
    sous_mode_selectionne = "Gosper"

def choisir_sous_mode_dragon():
    '''Cette fonction est appelée lorsqu'on clique sur le bouton "▶ Dragon" dans le
    mode "3 - Pliages". '''
    global sous_mode_selectionne
    sous_mode_selectionne = "Dragon"

def choisir_sous_mode_fractal_libre():
    ''' Cette fonction est appelée lorsqu'on clique sur le bouton "▶ Fractal Libre" dans le
    mode "3 - Pliages". '''
    global sous_mode_selectionne
    sous_mode_selectionne = "Fractal_Libre"

#########################################################################################

# Fonction pour dessiner la figure
def dessiner_figure():
    '''Cette fonction est appelée lorsqu'on clique sur le bouton "Dessiner" et récupère le nombre d'itérations,
    choisit une couleur aléatoire, puis en fonction du mode et du sous-mode
    sélectionnés, elle appelle la fonction appropriée pour dessiner la figure correspondante.'''
    global iterations
    iterations = int(entre_nombre_iteration.get())
    couleur = choice(['red', 'blue', 'green', 'yellow', 'purple'])
    if mode_selectionne == "1 - Récursivité":
        if sous_mode_selectionne == "Triangle de Sierpinski":
            dessiner_triangle_sierpinski({'x': 5, 'y': 395}, {'x': 250, 'y': 5}, {'x': 495, 'y': 395}, iterations, couleur)
        elif sous_mode_selectionne == "Éponge de Menger":
            dessiner_eponge_menger({'x': 5, 'y': 5}, 400, iterations, couleur)
    elif mode_selectionne == "2 - L-Systèmes":
        if sous_mode_selectionne == "Koch":
            dessiner_koch_iteratif(iterations)
        elif sous_mode_selectionne == "Gosper":
            dessiner_gosper_iteratif(iterations)
    elif mode_selectionne == "3 - Pliages":
        if sous_mode_selectionne == "Dragon":
            dessiner_dragon_pliage(iterations)
        elif sous_mode_selectionne == "Fractal_Libre":
            dessiner_triangle_plie(iterations)


##########################################################################################

def dessiner_triangle_sierpinski(A, B, C, n, couleur):
    ''' Appelle la fonction sierpinski pour dessiner le Triangle de Sierpinski récursivement à partir des
     points A, B, et C, avec un certain nombre d'itérations et une couleur donnée.'''
    canevas.delete('all')
    sierpinski(A, B, C, n, couleur)


def sierpinski(A, B, C, n, couleur):
    '''Cette fonction récursive dessine le Triangle de Sierpinski à partir des points A, B, et C, avec un certain
    nombre d'itérations et une couleur donnée.'''
    if n == 0:
        canevas.create_polygon(A['x'], A['y'], B['x'], B['y'], C['x'], C['y'], fill=couleur)
    else:
        M1 = {'x': (A['x'] + B['x']) // 2, 'y': (A['y'] + B['y']) // 2}
        M2 = {'x': (B['x'] + C['x']) // 2, 'y': (B['y'] + C['y']) // 2}
        M3 = {'x': (C['x'] + A['x']) // 2, 'y': (C['y'] + A['y']) // 2}

        sierpinski(A, M1, M3, n - 1, couleur)
        sierpinski(B, M1, M2, n - 1, couleur)
        sierpinski(C, M2, M3, n - 1, couleur)


def dessiner_eponge_menger(A, taille, n, couleur):
    '''Appelle la fonction eponge_menger pour dessiner l'Éponge de Menger récursivement à partir du
    point A, avec une certaine taille initiale, un nombre d'itérations et une couleur donnée.'''
    canevas.delete('all')
    eponge_menger(A, taille, n, couleur)


def eponge_menger(A, taille, n, couleur):
    '''Cette fonction récursive dessine l'Éponge de Menger à partir du point A, avec une certaine
    taille initiale, un nombre d'itérations et une couleur donnée.'''
    if n == 0:
        canevas.create_rectangle(A['x'], A['y'], A['x'] + taille, A['y'] + taille, fill=couleur)
    else:
        taille = taille // 3
        E = {'x': A['x'], 'y': A['y'] + taille}
        F = {'x': A['x'] + taille, 'y': A['y']}
        G = {'x': A['x'] + 2 * taille, 'y': A['y'] + taille}
        H = {'x': A['x'] + taille, 'y': A['y'] + 2 * taille}
        eponge_menger(E, taille, n - 1, couleur)
        eponge_menger(F, taille, n - 1, couleur)
        eponge_menger(G, taille, n - 1, couleur)
        eponge_menger(H, taille, n - 1, couleur)


##############################################################################################

def iter_L_systeme(F1, regle,n):
    '''effectue l'itération d'un système L en utilisant une file F1, une règle regle et un nombre d'itérations.
     Elle retourne la file résultante après les itérations.'''
    if n == 0: return F1
    F2 = File()
    while not F1.est_vide():
        alpha = F1.defile()
        for c in regle[alpha]: F2.enfile(c)
    return iter_L_systeme(F2,regle,n-1)


def dessiner_koch_iteratif(iterations):
    '''Dessine le flocon de Koch de manière itérative en utilisant un système L. Elle efface le canevas,
    initialise un crayon,définit la règle pour le flocon de Koch, itère le système L et dessine le fameux résultat.'''
    canevas.delete('all')
    couleur = choice(['red', 'blue', 'green', 'yellow', 'purple'])
    # Initialisation du crayon
    mon_crayon = crayon(100, 250, couleur)

    # Définition de la règle pour le flocon de Koch
    regle_koch = {"A": "AGADADAGA", "G": "G", "D": "D"}

    # Initialisation du schéma de départ
    schema_koch = File()
    for c in regle_koch['A']:
        schema_koch.enfile(c)

    # Itération du flocon de Koch
    schema_final = iter_L_systeme(schema_koch, regle_koch, iterations)

    # Dessin du flocon de Koch
    for instruction in schema_final:
        if instruction == 'A':
            mon_crayon.avance(1)  # A : avancer de 1 cm en traçant
        elif instruction == 'G':
            mon_crayon.tourne(-90)  # G : pivoter de 90° à gauche
        elif instruction == 'D':
            mon_crayon.tourne(90)  # D : pivoter de 90° à droite

def dessiner_gosper_iteratif(iterations):
    '''Dessine la courbe de Gosper de manière itérative en utilisant un système L. Elle efface le canevas,
    initialise un crayon, définit la règle pour la courbe de Gosper, itère le système L et dessine le fameux résultat.'''
    canevas.delete('all')
    couleur = choice(['red', 'blue', 'green', 'yellow', 'purple'])
    # Initialisation du crayon
    mon_crayon = crayon(200, 100, couleur)

    # Définition de la règle pour la courbe de Gosper
    regle_gosper = {"A": "ADBDDBGAGGAAGBD", "B": "GADBBDDBDAGGAGB", "D": "D", "G": "G"}

    # Initialisation du schéma de départ
    schema_gosper = File()
    for c in regle_gosper['A']:
        schema_gosper.enfile(c)

    # Itération de la courbe de Gosper
    schema_final = iter_L_systeme(schema_gosper, regle_gosper, iterations)

    # Dessin de la courbe de Gosper
    for instruction in schema_final:
        if instruction == 'A' or instruction == 'B':
            mon_crayon.avance(10)  # Avancer de 1 cm en traçant
        elif instruction == 'D':
            mon_crayon.tourne(60)  # Pivoter de 60° à droite
        elif instruction == 'G':
            mon_crayon.tourne(-60)  # Pivoter de 60° à gauche

#################################################################################

def dessiner_dragon_pliage(iterations):
    '''Dessine le fractal Dragon de manière itérative en utilisant un système L. Elle efface le canevas, initialise
    un crayon, génère les instructions du système L pour le fractal Dragon, itère le système L et dessine
    le fameux résultat.'''
    canevas.delete('all')
    couleur = choice(['red', 'blue', 'green', 'yellow', 'purple'])

    # Initialisation du crayon
    mon_crayon = crayon(150, 200, couleur)

    # Appel de la fonction auxiliaire pour dessiner le fractal Dragon
    dragon_pliage(mon_crayon, iterations)


def dragon_pliage(crayon, n):
    '''Génère les instructions du système L pour le fractal Dragon en utilisant une pile. Elle utilise une
    chaîne de caractères comme instruction de départ et itère pour produire les instructions finales.'''
    pile = Pile()
    instruction = "FX"

    for _ in range(n):
        nouvelle_instruction = ""

        for i in range(len(instruction)):
            if instruction[i] == "X":
                nouvelle_instruction = nouvelle_instruction  + "X+YF+"
            elif instruction[i] == "Y":
                nouvelle_instruction = nouvelle_instruction + "-FX-Y"
            else:
                nouvelle_instruction = nouvelle_instruction + instruction[i]

        instruction = nouvelle_instruction

    for i in range(len(instruction)):
        if instruction[i] == "F":
            crayon.avance(5)
        elif instruction[i] == "+":
            crayon.tourne(90)
        elif instruction[i] == "-":
            crayon.tourne(-90)
        elif instruction[i] == "[":
            pile.empile((crayon.pos, crayon.ang, crayon.dir))
        elif instruction[i] == "]":
            pos, ang, direction = pile.depile()
            crayon.pos = pos
            crayon.ang = ang
            crayon.dir = direction


def dessiner_triangle_plie(iterations):
    '''Dessine un triangle plié de manière récursive. Elle efface le canevas, initialise un crayon, génère les
    instructions pour le triangle plié, itère la récursion et dessine le fameux résultat.'''
    canevas.delete('all')
    couleur = choice(['blue', 'green', 'purple', 'dark orange'])

    # Initialisation du crayon
    mon_crayon = crayon(140, 120, couleur)

    # Appel de la fonction auxiliaire pour dessiner le triangle plié
    triangle_plie(mon_crayon, iterations, 200)

def triangle_plie(crayon, n, longueur):
    '''Génère les instructions pour dessiner un triangle plié de manière récursive. Elle utilise la récursivité
    pour générer les instructions et dessiner le triangle plié.'''
    if n == 0:
        return
    else:
        # Dessiner le triangle initial
        for _ in range(3):
            crayon.avance(longueur)
            crayon.tourne(120)

        # Sauvegarder la position et l'angle
        position_sauvegardee = crayon.pos
        angle_sauvegarde = crayon.ang

        # Plier vers l'intérieur du triangle
        crayon.tourne(60)

        # Dessiner le triangle plié
        for _ in range(3):
            crayon.avance(longueur / 2)
            triangle_plie(crayon, n-1, longueur / 2)
            crayon.avance(longueur / 2)
            crayon.tourne(-120)

        # Retourner à la position sauvegardée
        crayon.pos, crayon.ang = position_sauvegardee, angle_sauvegarde

################################################################################################

#Label
label_regle = Label(fenetre, text="CHOISSISEZ UN MODE PARMI LES 3 PROPOSER, UN DES 2 FRACTALS, UNE ITÉRATIONS ET DESSINEZ !",font=('arial',11,'bold'), bg='lavender',fg='black')
label_regle.place(x=10, y=500)

label_sierpinski = Label(fenetre, text="( Itérations conseillé : 5 )", bg='lavender',fg='blue')
label_sierpinski.place(x=160, y=62)

label_menger = Label(fenetre, text="( Itérations conseillé : 4 )", bg='lavender',fg='blue')
label_menger.place(x=145, y=103)

label_koch = Label(fenetre, text="( Itérations conseillé : 4 )", bg='lavender',fg='red')
label_koch.place(x=80, y=202)

label_gosper = Label(fenetre, text="( Itérations conseillé : 2 )", bg='lavender',fg='red')
label_gosper.place(x=100, y=242)

label_dragon = Label(fenetre, text="( Itérations conseillé : 9 )", bg='lavender',fg='orange')
label_dragon.place(x=90, y=342)

label_libre = Label(fenetre, text="( Itérations conseillé : 6 )", bg='lavender',fg='orange')
label_libre.place(x=120, y=382)

#######################################################################################

# Entry pour le nombre d'itérations
entre_nombre_iteration = Entry(fenetre, width=10)
entre_nombre_iteration.place(x=470, y=431)

label_nombre_iteration = Label(fenetre, text="Nombre d'itérations:", bg='grey')
label_nombre_iteration.place(x=340, y=430)

# Boutons pour choisir le mode
button_mode_r = Button(fenetre, text="1 - Récursivité",font=('arial',12,'bold'),bg='blue', width=15, command=choisir_mode_r)
button_mode_r.place(x=10, y=10)

button_mode_l = Button(fenetre, text="2 - L-Systèmes",font=('arial',12,'bold'),bg='red', width=15, command=choisir_mode_l)
button_mode_l.place(x=10, y=150)

button_mode_p = Button(fenetre, text="3 - Pliages",font=('arial',12,'bold'),bg='orange', width=15, command=choisir_mode_p)
button_mode_p.place(x=10, y=290)

# Boutons pour choisir le sous-mode
button_mode_r_tri = Button(fenetre, text=" ▶ Triangle de Sierpinski",bg='blue', command=choisir_sous_mode_tri)
button_mode_r_tri.place(x=10, y=60)

button_mode_r_emp = Button(fenetre, text=" ▶ Éponge de Menger",bg='blue', command=choisir_sous_mode_emp)
button_mode_r_emp.place(x=10, y=100)

button_mode_l_koch = Button(fenetre, text=" ▶ Koch",bg='red', command=choisir_sous_mode_koch)
button_mode_l_koch.place(x=10, y=200)

button_mode_l_gosper = Button(fenetre, text=" ▶ Gosper",bg='red', command=choisir_sous_mode_gosper)
button_mode_l_gosper.place(x=10, y=240)

button_mode_p_dragon = Button(fenetre, text=" ▶ Dragon",bg='orange', command=choisir_sous_mode_dragon)
button_mode_p_dragon.place(x=10, y=340)

button_mode_p_dragon = Button(fenetre, text=" ▶ Fractal Libre",bg='orange', command=choisir_sous_mode_fractal_libre)
button_mode_p_dragon.place(x=10, y=380)

# Bouton pour dessiner la figure
bouton_dessiner = Button(text='Dessiner',font=('arial',15,'bold'),bg= 'green', command=dessiner_figure)
bouton_dessiner.place(x=570, y=423)

fenetre.mainloop()
