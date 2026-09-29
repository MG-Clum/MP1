from turtle import *
from random import *
x_fenetre = 1920
y_fenetre = 1080
setup(x_fenetre, y_fenetre, 0 ,0)
speed(100)
up()

color = [
    "white", "black", "red", "green", "blue", "yellow",
    "orange", "purple", "pink", "brown", "gray", "cyan",
    "magenta", "violet", "gold", "silver", "navy", "maroon",
    "olive", "lime", "teal", "indigo", "coral", "salmon",
    "khaki", "turquoise", "orchid", "plum", "tan", "beige"
]

def route(type_route):
    if type_route == 1:
        up()
        goto(0-(x_fenetre/5),0-(y_fenetre/10))
        down()
        goto(0+x_fenetre/5, 0-(y_fenetre/10))
        goto(0+x_fenetre/5.2, 0-y_fenetre/6)
        goto(0-(x_fenetre/5.2),0-(y_fenetre/6))
        goto(0-(x_fenetre/5),0-(y_fenetre/10))
        up()
    return None


def porte_pose1(porte_type, position_tortue_debut_etage_x, position_tortue_debut_etage_y):
    if porte_type == 1 :
        """fenetre position1 type 1"""
        goto(position_tortue_debut_etage_x , position_tortue_debut_etage_y)
        setheading(0)
        forward(12.5)
        setheading(90)
        down()
        fillcolor(door_color)
        begin_fill()
        down()
        right(90)
        forward(30)
        left(90)
        forward(50)
        left(90)
        forward(30)
        left(90)
        forward(50)
        up()
        end_fill()
        return


    if porte_type == 2 :
        """fenetre position1 type 2"""
        goto(position_tortue_debut_etage_x , position_tortue_debut_etage_y)
        setheading(0)
        forward(12.5)
        setheading(90)
        down()
        fillcolor(door_color)
        begin_fill()
        down()
        right(90)
        forward(30)
        left(90)
        forward(35)
        circle(15,180)
        forward(35)
        up()
        end_fill()
        return
    
def porte_pose2(porte_type, position_tortue_debut_etage_x, position_tortue_debut_etage_y):
    if porte_type == 1 :
        """fenetre position2 type 1"""
        goto(position_tortue_debut_etage_x , position_tortue_debut_etage_y)
        setheading(0)
        forward(55)
        setheading(90)
        down()
        fillcolor(door_color)
        begin_fill()
        down()
        right(90)
        forward(30)
        left(90)
        forward(50)
        left(90)
        forward(30)
        left(90)
        forward(50)
        up()
        end_fill()
        return


    if porte_type == 2 :
        """fenetre position2 type 2"""
        goto(position_tortue_debut_etage_x , position_tortue_debut_etage_y)
        setheading(0)
        forward(55)
        setheading(90)
        down()
        fillcolor(door_color)
        begin_fill()
        down()
        right(90)
        forward(30)
        left(90)
        forward(35)
        circle(15,180)
        forward(35)
        up()
        end_fill()
        return
        
def porte_pose3(porte_type, position_tortue_debut_etage_x, position_tortue_debut_etage_y):
    if porte_type == 1 :
        """fenetre position3 type 1"""
        goto(position_tortue_debut_etage_x , position_tortue_debut_etage_y)
        setheading(0)
        forward(97)
        setheading(90)
        down()
        fillcolor(door_color)
        begin_fill()
        down()
        right(90)
        forward(30)
        left(90)
        forward(50)
        left(90)
        forward(30)
        left(90)
        forward(50)
        up()
        end_fill()
        return


    if porte_type == 2 :
        """fenetre position3 type 2"""
        goto(position_tortue_debut_etage_x , position_tortue_debut_etage_y)
        setheading(0)
        forward(97)
        setheading(90)
        down()
        fillcolor(door_color)
        begin_fill()
        down()
        right(90)
        forward(30)
        left(90)
        forward(35)
        circle(15,180)
        forward(35)
        up()
        end_fill()
        return

def fenetre_pose1(fenetre1_type, position_tortue_debut_etage_x, position_tortue_debut_etage_y):
    if fenetre1_type == 1 :
        goto(position_tortue_debut_etage_x , position_tortue_debut_etage_y)
        fillcolor('white')
        setheading(0)
        forward(12.5)
        setheading(90)
        forward(35)
        setheading(270)
        down()
        begin_fill()
        circle(15,360)
        up()
        end_fill()
        return

    else:
        """fenetre position 1"""
        goto(position_tortue_debut_etage_x , position_tortue_debut_etage_y)
        fillcolor('white')
        setheading(0)
        forward(12.5)
        setheading(90)
        forward(20)
        down()
        begin_fill()
        right(90)
        forward(30)
        lt(90)
        forward(30)
        lt(90)
        forward(30)
        lt(90)
        forward(30)
        up()
        end_fill()
        return

def fenetre_pose2(fenetre1_type, position_tortue_debut_etage_x, position_tortue_debut_etage_y):
    if fenetre1_type == 1 :
        goto(position_tortue_debut_etage_x , position_tortue_debut_etage_y)
        fillcolor('white')
        setheading(0)
        forward(55)
        setheading(90)
        forward(35)
        setheading(270)
        down()
        begin_fill()
        circle(15,360)
        up()
        end_fill()
        return

    else:
        """fenetre position 2"""
        goto(position_tortue_debut_etage_x , position_tortue_debut_etage_y)
        fillcolor('white')
        setheading(0)
        forward(55)
        setheading(90)
        forward(20)
        down()
        begin_fill()
        right(90)
        forward(30)
        lt(90)
        forward(30)
        lt(90)
        forward(30)
        lt(90)
        forward(30)
        up()
        end_fill()
        return

def fenetre_pose3(fenetre1_type, position_tortue_debut_etage_x, position_tortue_debut_etage_y):
    if fenetre1_type == 1 :
        goto(position_tortue_debut_etage_x , position_tortue_debut_etage_y)
        fillcolor('white')
        setheading(0)
        forward(97)
        setheading(90)
        forward(35)
        setheading(270)
        down()
        begin_fill()
        circle(15,360)
        up()
        end_fill()
        return

    else:
        """fenetre position 3"""
        goto(position_tortue_debut_etage_x , position_tortue_debut_etage_y)
        fillcolor('white')
        setheading(0)
        forward(97)
        setheading(90)
        forward(20)
        down()
        begin_fill()
        right(90)
        forward(30)
        lt(90)
        forward(30)
        lt(90)
        forward(30)
        lt(90)
        forward(30)
        up()
        end_fill()
        return

def premier_etage(porte_pose1, porte_pose2, porte_pose3, fenetre_pose1, fenetre_pose2, fenetre_pose3):
    global door_color

    couleur_etage = choice(color)
    door_color = choice(color)

    setheading(90)
    down()
    fillcolor(couleur_etage)
    begin_fill()
    position_tortue_debut_etage_x = xcor()
    position_tortue_debut_etage_y = ycor()
    setheading(90)
    forward(60)
    right(90)
    forward(140)
    right(90)
    forward(60)
    right(90)
    forward(140)
    end_fill()
    up()

    emplacement_porte = randint(1, 3)
    porte_type = randint(1, 2)

    if emplacement_porte == 1:
        porte_pose1(porte_type, position_tortue_debut_etage_x, position_tortue_debut_etage_y)

        fenetre2_type = randint(1, 3)
        fenetre_pose2(fenetre2_type, position_tortue_debut_etage_x, position_tortue_debut_etage_y)

        fenetre3_type = randint(1, 3)
        fenetre_pose3(fenetre3_type, position_tortue_debut_etage_x, position_tortue_debut_etage_y)

    elif emplacement_porte == 2:
        porte_pose2(porte_type, position_tortue_debut_etage_x, position_tortue_debut_etage_y)

        fenetre1_type = randint(1, 3)
        fenetre_pose1(fenetre1_type, position_tortue_debut_etage_x, position_tortue_debut_etage_y)

        fenetre3_type = randint(1, 3)
        fenetre_pose3(fenetre3_type, position_tortue_debut_etage_x, position_tortue_debut_etage_y)

    elif emplacement_porte == 3:
        porte_pose3(porte_type, position_tortue_debut_etage_x, position_tortue_debut_etage_y)

        fenetre1_type = randint(1, 3)
        fenetre_pose1(fenetre1_type, position_tortue_debut_etage_x, position_tortue_debut_etage_y)

        fenetre2_type = randint(1, 3)
        fenetre_pose2(fenetre2_type, position_tortue_debut_etage_x, position_tortue_debut_etage_y)

    return position_tortue_debut_etage_x, position_tortue_debut_etage_y

def premier_etage(couleur_immeuble, porte_pose1, porte_pose2, porte_pose3, fenetre_pose1, fenetre_pose2, fenetre_pose3):
    global door_color
    door_color = choice([c for c in color if c != couleur_immeuble])

    setheading(90)
    down()
    fillcolor(couleur_immeuble)
    begin_fill()
    position_tortue_debut_etage_x = xcor()
    position_tortue_debut_etage_y = ycor()
    setheading(90)
    forward(60)
    right(90)
    forward(140)
    right(90)
    forward(60)
    right(90)
    forward(140)
    end_fill()
    up()

    emplacement_porte = randint(1, 3)
    porte_type = randint(1, 2)

    if emplacement_porte == 1:
        porte_pose1(porte_type, position_tortue_debut_etage_x, position_tortue_debut_etage_y)
        fenetre_pose2(randint(1, 3), position_tortue_debut_etage_x, position_tortue_debut_etage_y)
        fenetre_pose3(randint(1, 3), position_tortue_debut_etage_x, position_tortue_debut_etage_y)

    elif emplacement_porte == 2:
        porte_pose2(porte_type, position_tortue_debut_etage_x, position_tortue_debut_etage_y)
        fenetre_pose1(randint(1, 3), position_tortue_debut_etage_x, position_tortue_debut_etage_y)
        fenetre_pose3(randint(1, 3), position_tortue_debut_etage_x, position_tortue_debut_etage_y)

    elif emplacement_porte == 3:
        porte_pose3(porte_type, position_tortue_debut_etage_x, position_tortue_debut_etage_y)
        fenetre_pose1(randint(1, 3), position_tortue_debut_etage_x, position_tortue_debut_etage_y)
        fenetre_pose2(randint(1, 3), position_tortue_debut_etage_x, position_tortue_debut_etage_y)

    return position_tortue_debut_etage_x, position_tortue_debut_etage_y

def balcon(x, y, emplacement):
    if emplacement == 1:
        x_emplacement = 12.5
    elif emplacement == 2:
        x_emplacement = 55
    elif emplacement == 3:
        x_emplacement = 97
    else:
        return

    largeur = 34
    debord = 6

    goto(x + x_emplacement - 2, y + 20)
    setheading(0)
    down()
    fillcolor("gray")
    begin_fill()
    forward(largeur)
    right(90)
    forward(debord)
    right(90)
    forward(largeur)
    right(90)
    forward(debord)
    end_fill()
    up()

    nb_barres = 6
    espace = largeur / (nb_barres - 1)
    pencolor("dimgray")
    for i in range(nb_barres):
        goto(x + x_emplacement - 2 + i * espace, y + 20)
        setheading(90)
        down()
        forward(15)
        up()

    goto(x + x_emplacement - 2, y + 35)
    setheading(0)
    down()
    forward(largeur)
    up()
    pencolor("black")

def etage(couleur_immeuble, position_tortue_debut_etage_x, position_tortue_debut_etage_y, fenetre_pose1, fenetre_pose2, fenetre_pose3):
    goto(position_tortue_debut_etage_x, position_tortue_debut_etage_y)
    setheading(90)
    down()
    fillcolor(couleur_immeuble)
    begin_fill()
    forward(60)
    right(90)
    forward(140)
    right(90)
    forward(60)
    right(90)
    forward(140)
    end_fill()
    up()

    fenetre_pose1(randint(1, 3), position_tortue_debut_etage_x, position_tortue_debut_etage_y)
    if randint(1, 4) == 1:
        balcon(position_tortue_debut_etage_x, position_tortue_debut_etage_y, 1)

    fenetre_pose2(randint(1, 3), position_tortue_debut_etage_x, position_tortue_debut_etage_y)
    if randint(1, 4) == 1:
        balcon(position_tortue_debut_etage_x, position_tortue_debut_etage_y, 2)

    fenetre_pose3(randint(1, 3), position_tortue_debut_etage_x, position_tortue_debut_etage_y)
    if randint(1, 4) == 1:
        balcon(position_tortue_debut_etage_x, position_tortue_debut_etage_y, 3)

    return position_tortue_debut_etage_x, position_tortue_debut_etage_y


def toit_pointu(x, y, couleur_toit):
    goto(x, y)
    setheading(0)
    down()
    fillcolor(couleur_toit)
    begin_fill()
    goto(x + 140, y)
    goto(x + 70, y + 50)
    goto(x, y)
    end_fill()
    up()

    return x, y

def toit_pointu_cheminer(x, y, couleur_toit):
    goto(x + 25, y + 18)
    setheading(90)
    down()
    fillcolor("dimgray")
    begin_fill()
    forward(40)
    right(90)
    forward(20)
    right(90)
    forward(40)
    right(90)
    forward(20)
    end_fill()
    up()


    goto(x, y)
    setheading(0)
    down()
    fillcolor(couleur_toit)
    begin_fill()
    goto(x + 140, y)
    goto(x + 70, y + 50)
    goto(x, y)
    end_fill()
    up()

    return x, y

def toit_arrondi(x, y, couleur_toit):
    goto(x, y)
    setheading(0)
    down()
    fillcolor(couleur_toit)
    begin_fill()
    forward(140)
    left(90)
    forward(5)
    circle(70, 180)
    forward(5)
    end_fill()
    up()

    return x, y

def immeuble(x_depart, y_depart, style_toit):
    goto(x_depart, y_depart)

    nb_etages = randint(0, 3)
    couleur_immeuble = choice(color)
    couleur_toit = choice(color)

    x, y = premier_etage(couleur_immeuble, porte_pose1, porte_pose2, porte_pose3, fenetre_pose1, fenetre_pose2, fenetre_pose3)

    for i in range(nb_etages):
        y += 60
        x, y = etage(couleur_immeuble, x, y, fenetre_pose1, fenetre_pose2, fenetre_pose3)

    y += 60

    if style_toit is None:
        style_toit = choice(["pointu", "arrondi", "pointu_cheminer"])

    if style_toit == "pointu":
        toit_pointu(x, y, couleur_toit)
    elif style_toit == "arrondi":
        toit_arrondi(x, y, couleur_toit)
    elif style_toit == "pointu_cheminer":
            toit_pointu_cheminer(x, y, couleur_toit)
    
def quartier(nb_immeubles, x_depart, y_depart, espace):
    x = x_depart

    for i in range(nb_immeubles):
        immeuble(x, y_depart, None)
        x += 140 + espace


def soleil():
    x, y = -500, 250  

    pensize(6)
    pencolor("orange")
    for i in range(12):
        up()
        goto(x, y)
        setheading(i * 30)
        forward(90)
        down()
        forward(40)
    up()

    pensize(3)
    goto(x, y - 70)
    setheading(0)
    fillcolor("yellow")
    down()
    begin_fill()
    circle(70)
    end_fill()
    up()


def lune():
    x, y = -600, 250

    pencolor("white")
    fillcolor("white")
    up()
    goto(x, y - 60)
    setheading(0)
    down()
    begin_fill()
    circle(60)
    end_fill()
    up()

    pencolor("midnightblue")
    fillcolor("midnightblue")
    goto(x + 30, y - 50)
    down()
    begin_fill()
    circle(55)
    end_fill()
    up()


def etoiles():
    for i in range(100):
        up()
        goto(randint(-960,960), randint(-540, 540))
        dot(randint(3, 6), "white")


def nuage(x, y, couleur="white"):
    pencolor(couleur)
    fillcolor(couleur)
    up()
    goto(x + 0, y)
    setheading(0)
    down()
    begin_fill()
    circle(40)
    end_fill()

    up()
    goto(x + 50, y)
    setheading(0)
    down()
    begin_fill()
    circle(40)
    end_fill()

    up()
    goto(x + 100, y)
    setheading(0)
    down()
    begin_fill()
    circle(40)
    end_fill()
    up()


def pluie():
    pencolor("blue")
    pensize(2)
    for i in range(150):
        up()
        goto(randint(-900, 900), randint(-280, 300))
        setheading(255)
        down()
        forward(15)
    up()


def meteo():
    type_meteo = choice(["soleil", "nuage", "pluie", "nuit"])

    if type_meteo == "soleil":
        bgcolor("lightskyblue")
        soleil()

    elif type_meteo == "nuage":
        bgcolor("lightsteelblue")
        nuage(-700, 300)
        nuage(-100, 280)
        nuage(400, 320)

    elif type_meteo == "pluie":
        bgcolor("slategray")
        nuage(-700, 320, "gray")
        nuage(-100, 300, "gray")
        nuage(400, 330, "gray")
        pluie()

    elif type_meteo == "nuit":
        bgcolor("midnightblue")
        etoiles()
        lune()

    
    pencolor("black")
    pensize(1)


meteo()
quartier(6, -400, -300, 20)

done()

#git addd .
#git commit -m "commitn"
#git push -u origin main
