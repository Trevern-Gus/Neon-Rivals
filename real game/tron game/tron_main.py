import turtle

#Set up screen 
wn = turtle.Screen()
wn.bgcolor("Black")
wn.title("Neon Rivals")
screen = turtle.Screen()
wn.setup(width=1000, height=900)


class player1(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        screen.register_shape("assests/sprites/blueeast.gif")
        screen.register_shape("assests/sprites/bluesouth.gif")
        screen.register_shape("assests/sprites/bluewest.gif")
        screen.register_shape("assests/sprites/bluenorth.gif")

        self.shapes = {
            0: "assests/sprites/blueeast.gif",
            90: "assests/sprites/bluenorth.gif",
            180: "assests/sprites/bluewest.gif",
            270: "assests/sprites/bluesouth.gif"
        }
        self.shape(self.shapes[0])
        self.penup()
        self.fwd_speed = 1
        self.color("Blue")
        self.pensize(3)
        self.speed(0)
        self.goto(x, y)
        self.pendown()
        self.score = 3

    def set_heading_shape(self):
        """Set the turtle's shape based on the current heading."""
        current_heading = int(self.heading())
        if current_heading in self.shapes:
            self.shape(self.shapes[current_heading])

    def turn_left(self):
        self.left(90)
        self.set_heading_shape()

    def turn_right(self):
        self.right(90)
        self.set_heading_shape()

    def set_prev_coord(self):
        """Sets prev coordinates."""
        prev_x = int(self.xcor())
        prev_y = int(self.ycor())
        self.prev_pos = (prev_x, prev_y)

   #--------------------------------------------------------
    def accelerate(self):
        """Min. speed = 1, Max. speed = 3."""
        if self.fwd_speed < 3:
            self.fwd_speed += 1
            self.forward(self.fwd_speed)

    def decelerate(self):
        """Min. speed = 1, therefore player can never stop"""
        if self.fwd_speed > 1:
            self.fwd_speed -= 1
            self.forward(self.fwd_speed)

    def set_prev_coord(self):
        """Sets prev coordinates."""
        prev_x = int(self.xcor())
        prev_y = int(self.ycor())
        self.prev_pos = (prev_x, prev_y)
   #------------------------------------------------------------------
    def update_score(self):
        self.score -= 1
        print(f"Player {self.color()} Score: {self.score}") 
        player1_instance.goto(-400, 0)
        player2_instance.goto(400, 0)
        player1_instance.clear()  # Clear only the player's trail
        player2_instance.clear()   



class player2(turtle.Turtle):
    def __init__(self, x, y):
        turtle.Turtle.__init__(self)
        screen.register_shape("assests/sprites/redwest.gif")
        screen.register_shape("assests/sprites/rednorth.gif")
        screen.register_shape("assests/sprites/redeast.gif")
        screen.register_shape("assests/sprites/redsouth.gif")

        self.shapes = {
            0: "assests/sprites/redeast.gif",
            90: "assests/sprites/rednorth.gif",
            180: "assests/sprites/redwest.gif",
            270: "assests/sprites/redsouth.gif"
        }
        self.shape(self.shapes[180])  # Initial shape is facing west
        self.left(180)
        self.penup()
        self.fwd_speed = 1
        self.color("Red")
        self.pensize(3)
        self.speed(0)
        self.goto(x, y)
        self.pendown()
        self.score = 3

    def set_heading_shape(self):
        """Set the turtle's shape based on the current heading."""
        current_heading = int(self.heading())
        if current_heading in self.shapes:
            self.shape(self.shapes[current_heading])

    def turn_left(self):
        self.left(90)
        self.set_heading_shape()

    def turn_right(self):
        self.right(90)
        self.set_heading_shape()

#--------------------------------------------------------
    def accelerate(self):
        #Min. speed = 1, Max. speed = 3.
        if self.fwd_speed < 3:
            self.fwd_speed += 1
            self.forward(self.fwd_speed)

    def decelerate(self):
        #Min. speed = 1, therefore player can never stop
        if self.fwd_speed > 1:
            self.fwd_speed -= 1
            self.forward(self.fwd_speed)

    def set_prev_coord(self):
      #Sets prev coordinates.
        prev_x = int(self.xcor())
        prev_y = int(self.ycor())
        self.prev_pos = (prev_x, prev_y)
#------------------------------------------------------------------
    def update_score(self):
        self.score -= 1
        print(f"Player {self.color()} Score: {self.score}")
        player1_instance.goto(-400, 0)
        player2_instance.goto(400, 0)
        player1_instance.clear()  # Clear only the player's trail
        player2_instance.clear()
    
    
        




class Border(turtle.Turtle):

   def __init__(self):
      turtle.Turtle.__init__(self)
      self.penup()
      self.hideturtle()
      self.speed(0)
      self.color("white")
      self.pensize(5)

   def draw_border (self):
      self.penup()
      self.goto(-500,-500)
      self.pendown()
      self.goto(-500,500)
      self.goto(500,500)
      self.goto(500,-500)
      self.goto(-500,-500)
      




#Create class instance
player1_instance = player1(-400,0)
player2_instance = player2(400,00)
border = Border()

#Draw the Border
border.draw_border()

# Set up keyboard bindings
wn.listen()
wn.onkey(player1_instance.turn_left, "a")
wn.onkey(player1_instance.turn_right, "d")
wn.onkey(player1_instance.accelerate, "w")
wn.onkey(player1_instance.decelerate, "s")

wn.onkey(player2_instance.turn_left, "Left")
wn.onkey(player2_instance.turn_right, "Right")
wn.onkey(player2_instance.accelerate, "Up")
wn.onkey(player2_instance.decelerate, "Down")

def distance(t1, t2):
    """Compute the distance between two turtles."""
    return ((t1.xcor() - t2.xcor()) ** 2 + (t1.ycor() - t2.ycor()) ** 2) ** 0.5

while True:
    player1_instance.set_prev_coord()
    player2_instance.set_prev_coord()

    player1_instance.forward(player1_instance.fwd_speed)
    player2_instance.forward(player2_instance.fwd_speed)














    

    if distance(player1_instance, player2_instance) < 20:
        player1_instance.update_score()
        player2_instance.update_score()

    # Check if players hit the border
    if (
        player1_instance.xcor() < -490
        or player1_instance.xcor() > 490
        or player1_instance.ycor() < -490
        or player1_instance.ycor() > 490
        
    ):
        player1_instance.update_score()
        player1_instance.goto(-400, 0)
        player2_instance.goto(400, 0)

    if (
        player2_instance.xcor() < -490
        or player2_instance.xcor() > 490
        or player2_instance.ycor() < -490
        or player2_instance.ycor() > 490
    ):
        player2_instance.update_score()
        player1_instance.goto(-400, 0)
        player2_instance.goto(400, 0)
        
    # Check if players have run out of points
    if player1_instance.score <= 0 or player2_instance.score <= 0:
        print("Game Over")
        break

    wn.update()

wn.mainloop()





delay = input("Enter")   
