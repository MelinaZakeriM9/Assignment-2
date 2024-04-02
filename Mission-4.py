#mission no. 4
import turtle

#I hope the snakes eat Alex <3
wn= turtle.Screen()
wn.title("magic")

snek= turtle.Turtle()
snek.color("Green")
snek.pensize("3")

boop= turtle.Turtle()
boop.color("Green")
boop.shape("circle")
boop.shapesize(0.5)

# clean up and use a loop?
snek.right(90)
snek.forward(65)
snek.right(90)
snek.forward(30)
snek.right(90)
snek.forward(65)

snek.penup()
snek.left(90)
snek.forward(15)
snek.pendown()

snek.left(90)
snek.penup()
snek.forward(35)
snek.pendown()
snek.forward(30)
snek.right(90)
snek.forward(35)

snek.left(90)
snek.forward(40)
snek.right(90)
snek.forward(15)

snek.penup()
snek.forward(5+35)
snek.right(90)
snek.forward(40+10)
snek.pendown()

snek.forward(15)
snek.right(90)
snek.forward(35)
snek.right(90)
snek.forward(25)
snek.right(90)
snek.forward(45+10)

snek.left(135)
snek.forward(15)
snek.right(45)
snek.forward(25)
snek.right(90)
snek.forward(45)
snek.right(90)
snek.forward(25+10)

boop.penup()
boop.right(90)
boop.forward(30)
boop.right(90)
boop.forward(45+11)
boop.stamp()
boop.forward(13)
boop.stamp()
boop.forward(11+15+23)
boop.left(90)
boop.forward(50)

wn.mainloop()

PassList= []

def unlock_vault(clues):
    for i in clues:
        PassList.append(i[0])


unlock_vault(list1)
unlock_vault(list2)

print(''.join(PassList))
