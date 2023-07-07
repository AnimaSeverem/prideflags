
//testing to see if this shows up in the repo
	
#Importing the module to make Turtle Graphics work.
import turtle

#Setting the name of the Turtle so I can summon it quickly.
pride = turtle.Turtle()

#Setting the background color so you can see the stripes easily.

pridebg = turtle.Screen()
pridebg.bgcolor("darkgrey")

#Making the turtle look like a turtle.

pride.shape("turtle")
pride.penup()

#Flag Dimensions

flag_height = 200
length = 300

#Flag Types

flag_types = {	
"gay": ["#FF1E26", "#FE941E", "#FFFF00", "#06BD00", "#004CFF", "#760088"],
"bi": ["#D70071", "#D70071", "#9C4E97", "#0035AA", "#0035AA"],
"trans": ["#55CDFD", "#F6AAB7", "#FFFFFF", "#F6AAB7", "#55CDFD"],
"ace": ["#000000", "#9E9E9E", "#FFFFFF", "#5E1984"],
"enby": ["#FCF431", "#FFFFFF", "#9D59D2", "#000000"],
"pan": ["#FE218B", "#FED700", "#21B0FE"],
"lesbian": ["#D42C00", "#FD9855", "#FFFFFF", "#D161A2", "#A20161"],
}

#Fetch stripe height by dividing total flag width by number of stripes in flag_type

def get_stripe_height(flag_type): 
	stripe_height = flag_height / len(flag_type)
	return(stripe_height)

#Drawing the Stripes
def draw_stripe(stripecolor, stripe_height):
	angle = 0
	pride.fillcolor(stripecolor)
	pride.pencolor(stripecolor)
	pride.begin_fill()
	pride.pendown()
	for i in range (0, 4):
		pride.seth(angle * -1)
		angle += 90
		if angle == 360:
			angle = 0
		elif angle == 90 or angle == 270: 
			pride.forward(length)
		else: 
			pride.forward(stripe_height)
	pride.end_fill()
	pride.penup()
   
def draw_pride_flag(flag_type):
	stripe_height = get_stripe_height(flag_type)
	pride.forward(length * -0.5)
	for color in flag_type:
		draw_stripe(color, stripe_height)

def victory_dance():
    pride.forward(flag_height)
    angle = 0
    for i in range (0, 24):
        pride.seth(angle * -1)
        angle += 90

#Lets the user define their flag choice
def flag_choice():
	choice = input("What flag would you like me to draw? ")
	if choice in flag_types:
		draw_pride_flag(flag_types[choice])
	else:
		print("Not a valid choice! Try again")

flag_choice()

victory_dance()

pridebg.exitonclick()

