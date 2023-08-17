import turtle as t

t.setup(400, 400)
t.bgcolor("white")

def draw_circle(radius, color): 
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()


# Daireleri ve yüzeyi çizme
t.penup()
t.goto(0, -120)
draw_circle(150, "#FFD700")  

# Gözler
t.goto(-40, 50)
draw_circle(30, "white")     
t.goto(-40, 50)
draw_circle(20, "black")    

t.goto(40, 50)
draw_circle(30, "white")     
t.goto(40, 50)
draw_circle(20, "black")    

# Ağız
t.goto(-50, -50)
t.setheading(-60)
t.pendown()
t.pensize(5)
t.circle(50, 120)

x = input("")
