import turtle
import random


# s = turtle.getscreen()


gracz1 = turtle.Turtle()
gracz1.getscreen()
gracz1.shape("turtle")
gracz1.pen(pencolor="green", fillcolor="green", pensize=5, speed=9)
gracz1.penup()
gracz1.goto(-200, 100)

gracz2 = gracz1.clone()
gracz2.color("blue")
gracz2.penup()
gracz2.goto(-200, -100)

gracz1.goto(300, 60)
gracz1.pendown()
gracz1.circle(40)
gracz1.penup()
gracz1.goto(-200, 100)

gracz2.goto(300, -140)
gracz2.pendown()
gracz2.circle(40)
gracz2.penup()
gracz2.goto(-200, -100)

kostka = [1, 2, 3, 4, 5, 6]

for i in range(20):
    if gracz1.pos() >= (300, 100):
        print("Wygrywa gracz pierwszy!")
        break
    elif gracz2.pos() >= (300, -100):
        print("Wygrywa gracz drugi!")
        break
    else:
        gracz1_ruch = input("Graczu 1 naciśnij Enter")
        wynik_kostki = random.choice(kostka)
        gracz1.forward(20 * wynik_kostki)
        gracz2_ruch = input("Graczu 2 naciśnij Enter")
        wynik_kostki = random.choice(kostka)
        gracz2.forward(20 * wynik_kostki)

turtle.mainloop()