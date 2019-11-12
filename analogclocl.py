import time
import turtle

wn=turtle.Screen()
wn.bgcolor("black")
wn.setup(width=600, height=600)
wn.title("simple analog clock by @khalidfarooq")
wn.tracer(0) #traces the prog

pen=turtle.Turtle()
pen.hideturtle()
pen.speed(0)
pen.pensize(3)

def draw_clock(h,m,s,pen):

    #clock face
    pen.up()
    pen.goto(0,210)
    pen.setheading(180)
    pen.color("green")
    pen.pendown()
    pen.circle(210)

    #hours place
    pen.up()
    pen.goto(0,0)
    pen.setheading(90)
    for _ in range(12):
        pen.fd(190)
        pen.pendown()
        pen.fd(20)
        pen.penup()
        pen.goto(0,0)
        pen.rt(30)


    #hour hand

    pen.penup()
    pen.goto(0,0)
    pen.setheading(90)
    angle = (h / 12) * 360
    pen.rt(angle)
    pen.color("white")
    pen.pendown()
    pen.fd(100)


    #minute hand

    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    angle = (m / 60) * 360
    pen.rt(angle)
    pen.color("gold")
    pen.pendown()
    pen.fd(160)

    #second hand

    pen.penup()
    pen.goto(0, 0)
    pen.setheading(90)
    angle = (s / 60) * 360
    pen.rt(angle)
    pen.color("red")
    pen.pendown()
    pen.fd(180)

while True:
    h = int(time.strftime("%I"))
    m = int(time.strftime("%M"))
    s = int(time.strftime("%S"))

    draw_clock(h,m,s,pen)
    wn.update()

    time.sleep(1) #delays execution for some sec

    pen.clear() #after display of sec it will clear itself

wn.mainloop()
