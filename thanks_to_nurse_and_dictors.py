import turtle

mypen = turtle.Turtle()
mypen.shape("turtle")
mypen.speed(10)
window = turtle.Screen()
window.bgcolor("skyblue")
style = ("Courier", 50, "italic")
rainbow = ['red', 'orange', 'yellow', 'green', 'blue', 'indigo', 'violet']
size = 250
mypen.penup()
mypen.goto(0, -80)
for color in rainbow:
	mypen.color(color)
	mypen.fillcolor(color)
	mypen.begin_fill()
	mypen.circle(size)
	mypen.end_fill()
	size -= 30
mypen.penup()
mypen.color("blue")
mypen.goto(0, -150)
mypen.write("Thank You Medical Staff", font=style, align='center')
mypen.penup()
mypen.goto(0, -200)
mypen.write("and", font=style, align='center')
mypen.penup()
mypen.goto(0, -250)
mypen.write("Key Workers", font=style, align='center')
mypen.hideturtle()
turtle.done()