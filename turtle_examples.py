import turtle # improtujemy bibliotekę

# 1. INICJOWANIE OBIEKTU TURTLE

# t = turtle.Turtle() # tworzymy obiekt turtle
# s = turtle.getscreen() # włączamy ekran
#
# # 2. Wybranie koloru ekranu i wygladu żółwia
#
# turtle.title("Moj żółw")
# turtle.bgcolor("#33A5FF")
#
# t.shape("turtle")
# # t.shape("arrow")
# # t.shape("circle")
#
# t.pen(pencolor="white", fillcolor="orange", pensize=5, speed=9)

# 3. PRZYKŁADOWE RUCHY ŻÓŁWIA

# t.forward(200) # turtle pokonuje prosto 200 kroków
# t.left(120) # turtle zmienia kierunek o 120 stopni w lewo
# t.backward(100) # turtle pokonuje do tyłu 100 kroków
# t.right(90) # turtle zmienia kierunek ruchu o 90 stopni w prawo
# t.forward(100) # turtle pokonuje prosto 100 kroków
# t.goto(100, 100) # turtle idzie prosto do punktu o wspolrzednej (100, 100)
# t.home() # turtle wraca do punktu początkowego

# 4. INNE RUCHY ŻÓŁWIA

# t.forward(200)
# t.stamp()
# t.forward(100)
#
# c = t.clone()
# c.color("magenta")
# c.begin_fill()
# c.circle(60)
# c.end_fill()
#
# # 5. PĘTLA LOOP
#
# for i in range(4):
#     t.fd(100)
#     t.rt(90)
#
# turtle.mainloop() # funkcja podtrzymująca ciągłe wyświetlanie ekranu

# 6. INSTRUKCJA IF

def kwadrat(t):
    for i in range(4):
        t.fd(100)
        t.rt(90)

def gwiazdka(t):
    for i in range(5):
        t.forward(100)
        t.right(144)

ksztalt = input("Co chcesz narysować?")

t = turtle.Turtle()
s = turtle.getscreen()
#
#
turtle.title("Moj żółw")
turtle.bgcolor("#33A5FF")

t.shape("turtle")
# t.shape("arrow")
# t.shape("circle")

t.pen(pencolor="white", fillcolor="orange", pensize=5, speed=9)

if(ksztalt == "kolko"):
    t.circle(10)
elif(ksztalt == 'kwadrat'):
    kwadrat(t)
elif(ksztalt == 'gwiazdka'):
    gwiazdka(t)
else:
    print("Nic nie narysuje:)")


