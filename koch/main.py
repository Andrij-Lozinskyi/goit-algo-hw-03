import turtle

def koch_snowflake(t, order, size):
    if order == 0: 
        t.forward(size)
    else:
        for angle in [60, -120, 60, 0]:
            koch_snowflake(t, order-1, size/3) 
            t.left(angle)

window = turtle.Screen()
window.bgcolor("white")

t = turtle.Turtle()
t.color("blue")
t.speed(0) 

recursion_level = int(window.textinput("Recursion level", "Enter recursion level:"))

t.penup()
t.goto(-150, 90)
t.pendown()

for i in range(3):
    koch_snowflake(t, recursion_level, 300)
    t.right(120)

window.mainloop()
