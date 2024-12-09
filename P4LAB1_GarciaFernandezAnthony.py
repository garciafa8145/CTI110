import turtle

# Function to draw a square
def draw_square(side_length):
    for _ in range(4):
        turtle.forward(side_length)
        turtle.right(90)

# Set up the turtle
turtle.speed(2)  # Set the drawing speed
turtle.color("blue")  # Set color for the square

# Draw the square
draw_square(100)  # You can change the size by modifying this value

# Finish drawing
turtle.done()
