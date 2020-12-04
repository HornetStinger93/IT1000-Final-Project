import turtle 

hurricane = turtle.Turtle()

hurricane.speed(30)
# So this makes a sorta eye looking thing which I like.
#It makes me think of the song 1000 Eyes by Death. Terrific song btw.
#Also for some reason reminds me of sketches of the globe on the internet from the 1990s.
#I do not know where I get that idea from but it reminds me of it.
#This was a fun project.
for i in range(50):
    hurricane.pencolor("red")
    hurricane.circle(10)
    hurricane.left(45)
    
    hurricane.pencolor("green")
    hurricane.circle(20)
    hurricane.right(150)

    hurricane.pencolor("yellow")
    hurricane.circle(30)
    hurricane.right(100)

    hurricane.pencolor("blue")
    hurricane.circle(40)
    hurricane.degrees(180)

    hurricane.pencolor("black")
    hurricane.circle(50)
    hurricane.degrees(180)
    
    hurricane.penup()
    hurricane.setposition(0, 0)
    hurricane.pendown()
    
    hurricane.right(2)
    
turtle.done()
