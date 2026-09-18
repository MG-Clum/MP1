from turtle import *
from random import *
x_fenetre = 1920
y_fenetre = 1080
setup(x_fenetre, y_fenetre, 0 ,0)
speed(10)

door_color = [
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

#def etage(nombre_etage):



def etage(couleur_etage):
    down()
    fillcolor(couleur_etage)
    begin_fill()
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
    
    if 0-(y_fenetre/10) <= 0-(y_fenetre/10) + 60:
        """création de la porte et des fenetres du 1er etage"""
        up()
        chois_porte_location = randint(1,3)
        couleur_porte = choice(door_color)
        porte_type = randint(1,2)
        setheading(90)
        position_tortue_debut_etage = position()
        
        if chois_porte_location == 1:

            if porte_type == 1 :
                """fenetre position1 type 1"""
                goto(position_tortue_debut_etage)
                setheading(0)
                forward(12.5)
                setheading(90)
                down()
                fillcolor(couleur_porte)
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


            if porte_type == 2 :
                """fenetre position1 type 2"""
                goto(position_tortue_debut_etage)
                setheading(0)
                forward(12.5)
                setheading(90)
                down()
                fillcolor(couleur_porte)
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
                           

            """fenetre position 2"""
            goto(position_tortue_debut_etage)
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

            """fenetre position 3"""
            goto(position_tortue_debut_etage)
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

        if chois_porte_location == 2:

            if porte_type == 1 :
                """fenetre position 2 type 1"""
                goto(position_tortue_debut_etage)
                setheading(0)
                forward(55)
                setheading(90)
                down()
                fillcolor(couleur_porte)
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


            if porte_type == 2 :
                """fenetre position 2 type 2"""
                goto(position_tortue_debut_etage)
                setheading(0)
                forward(55)
                setheading(90)
                down()
                fillcolor(couleur_porte)
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
                           



            """fenetre position1"""
            goto(position_tortue_debut_etage)
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


            """fenetre position 3"""
            goto(position_tortue_debut_etage)
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

        if chois_porte_location == 3:

            if porte_type == 1 :
                """fenetre position 3 type 1"""
                goto(position_tortue_debut_etage)
                setheading(0)
                forward(97)
                setheading(90)
                down()
                fillcolor(couleur_porte)
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


            if porte_type == 2 :
                """fenetre position 3 type 2"""
                goto(position_tortue_debut_etage)
                setheading(0)
                forward(97)
                setheading(90)
                down()
                fillcolor(couleur_porte)
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
                           

            """fenetre position1"""
            goto(position_tortue_debut_etage)
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

            """fenetre position 2"""
            goto(position_tortue_debut_etage)
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

        
        





etage('blue')
#route(1)
done()

#git addd .
#git commit -m "commitn"
#git push -u origin main