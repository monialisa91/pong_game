import turtle

t = turtle.Turtle() # tworzymy obiekt turtle
s = turtle.getscreen() # włączamy ekran
turtle.title("Moj żółw")
turtle.bgcolor("#33A5FF")

t.shape("turtle")
# t.shape("arrow")
# t.shape("circle")

t.pen(pencolor="white", fillcolor="orange", pensize=5, speed=5)

# zad.1

# i = 1
#
# while(i < 5):
#     t.circle(i*10)
#     i += 1
#
# turtle.mainloop() # funkcja podtrzymująca ciągłe wyświetlanie ekranu

# zad.2

for i in range(6):
    t.forward(100)
    t.left(60)
#
# turtle.mainloop() # funkcja podtrzymująca ciągłe wyświetlanie ekranu

# zad.3


for i in range(5):
    t.forward(100)
    t.right(144)

turtle.mainloop()
