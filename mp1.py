from turtle import *
x_fenetre = 1920
y_fenetre = 1080
setup(x_fenetre, y_fenetre, 0 ,0)

def route(type_route):
    if type_route == 1:
        up()
        goto(0-(x_fenetre/5),0-(y_fenetre/10))
        down()
        goto(0+x_fenetre/5, 0-(y_fenetre/10))

    return type_route



route(1)
done()

#git addd .
#git commit -m "commitn"
#git push -u origin main