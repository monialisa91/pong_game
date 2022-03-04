import turtle

sc = turtle.Screen()
sc.title("Gra w ponga")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

lewa_paletka = turtle.Turtle()
lewa_paletka.speed(0)
lewa_paletka.shape("square")
lewa_paletka.color("blue")
lewa_paletka.shapesize(stretch_wid=6, stretch_len=2)
lewa_paletka.penup()
lewa_paletka.goto(-400, 0)

prawa_paletka = turtle.Turtle()
prawa_paletka.speed(0)
prawa_paletka.shape("square")
prawa_paletka.color("green")
prawa_paletka.shapesize(stretch_wid=6, stretch_len=2)
prawa_paletka.penup()
prawa_paletka.goto(400, 0)

pilka = turtle.Turtle()
pilka.speed(30)
pilka.shape("circle")
pilka.color("black")
pilka.penup()
pilka.goto(0, 0)
pilka.dx = 5 # krok żółwia
pilka.dy = -5

pierwszy_gracz = 0
drugi_gracz = 0

napis = turtle.Turtle()
napis.speed(0)
napis.color("blue")
napis.penup()
napis.hideturtle()
napis.goto(0, 260)
napis.write("Pierwszy gracz : 0    Drugi gracz: 0",
             align="center", font=("Courier", 24, "normal"))


def lewa_paletka_gora():
    y = lewa_paletka.ycor() # pobieramy wartość współrzędnej y
    y += 20 # dodajemy do niej 20
    lewa_paletka.sety(y) # ustawiamy nową wartość współrzędnej y

def lewa_paletka_dol():
    y = lewa_paletka.ycor()
    y -= 20
    lewa_paletka.sety(y)

def prawa_paletka_gora():
    y = prawa_paletka.ycor()
    y += 20
    prawa_paletka.sety(y)

def prawa_paletka_dol():
    y = prawa_paletka.ycor()
    y -= 20
    prawa_paletka.sety(y)



sc.listen()
sc.onkeypress(lewa_paletka_gora, "w")
sc.onkeypress(lewa_paletka_dol, "s")
sc.onkeypress(prawa_paletka_gora, "Up")
sc.onkeypress(prawa_paletka_dol, "Down")

while(True):

    sc.update()
    pilka.setx(pilka.xcor() + pilka.dx)
    pilka.sety(pilka.ycor() + pilka.dy)

    if pilka.ycor() > 280:
        pilka.sety(280)
        pilka.dy *= -1

    if pilka.ycor() < -280:
        pilka.sety(-280)
        pilka.dy *= -1

    # if pilka.xcor() > 480:
    #     pilka.setx(480)
    #     pilka.dx *= -1
    #
    # if pilka.xcor() < -480:
    #     pilka.setx(-480)
    #     pilka.dx *= -1

    if pilka.xcor() > 500:
        pilka.goto(0, 0)
        pierwszy_gracz += 1
        napis.clear()
        napis.write("Pierwszy gracz : {}    Drugi gracz: {}".format(
            pierwszy_gracz, drugi_gracz), align="center",
            font=("Courier", 24, "normal"))

    if pilka.xcor() < -500:
        pilka.goto(0, 0)
        pilka.dy *= -1
        drugi_gracz += 1
        napis.clear()
        napis.write("Pierwszy gracz : {}    Drugi gracz: {}".format(
            pierwszy_gracz, drugi_gracz), align="center",
            font=("Courier", 24, "normal"))

    if (pilka.xcor() > 360 and pilka.xcor() < 370 and abs(prawa_paletka.ycor() - pilka.ycor()) <50):
        pilka.setx(360)
        pilka.dx *= -1

    if (pilka.xcor() < -360 and pilka.xcor() > -370 and abs(lewa_paletka.ycor() - pilka.ycor()) <50):
        pilka.setx(-360)
        pilka.dx *= -1


# while True:
#     sc.update()
#
#     hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
#     hit_ball.sety(hit_ball.ycor() + hit_ball.dy)
#
#     # Checking borders
#     if hit_ball.ycor() > 280:
#         hit_ball.sety(280)
#         hit_ball.dy *= -1
#
#     if hit_ball.ycor() < -280:
#         hit_ball.sety(-280)
#         hit_ball.dy *= -1
#
#     if hit_ball.xcor() > 500:
#         hit_ball.goto(0, 0)
#         hit_ball.dy *= -1
#         left_player += 1
#         sketch.clear()
#         sketch.write("Left_player : {}    Right_player: {}".format(
#             left_player, right_player), align="center",
#             font=("Courier", 24, "normal"))
#
#     if hit_ball.xcor() < -500:
#         hit_ball.goto(0, 0)
#         hit_ball.dy *= -1
#         right_player += 1
#         sketch.clear()
#         sketch.write("Left_player : {}    Right_player: {}".format(
#             left_player, right_player), align="center",
#             font=("Courier", 24, "normal"))
#
#     # Paddle ball collision
#     if (hit_ball.xcor() > 360 and hit_ball.xcor() < 370) and (hit_ball.ycor() < right_pad.ycor() + 40 and hit_ball.ycor() > right_pad.ycor() - 40):
#         hit_ball.setx(360)
#         hit_ball.dx *= -1
#
#     if (hit_ball.xcor() < -360 and hit_ball.xcor() > -370) and (hit_ball.ycor() < left_pad.ycor() + 40 and hit_ball.ycor() > left_pad.ycor() - 40):
#         hit_ball.setx(-360)
#         hit_ball.dx *= -1



turtle.mainloop()