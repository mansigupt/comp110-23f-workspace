"""EX05 - Turtle!"""
__author__ = "730391057"

from turtle import Turtle, Screen, colormode, done
import random

# Create a turtle object for drawing and color mode setting
scene: Turtle = Turtle()
colormode(255)

# Set up the screen
window = Screen()
window.bgcolor(173, 216, 230)  # "lightblue" in RGB (173, 216, 230)

# Function to draw a mountain
def draw_mountain(x, y, width, height, color):
    scene.penup()
    scene.fillcolor(color)
    scene.goto(x, y)
    scene.pendown()
    scene.begin_fill()
    
    mountain: int = 0
    while mountain < 3:
        scene.forward(width)
        scene.left(120)
        mountain += 1
    
    scene.end_fill()


# Function to draw the sun
def draw_sun(x, y, radius):
    scene.penup()
    scene.fillcolor(255, 255, 0)
    scene.goto(x, y)
    scene.pendown()
    scene.begin_fill()
    
    scene.circle(radius)
    
    scene.end_fill()


# Function to draw a cloud
def draw_cloud(x, y):
    scene.penup()
    scene.goto(x, y)
    scene.pendown()
    scene.color(255, 255, 255)
    scene.begin_fill()
    
    # Draw the cloud's body (three humps) 
    scene.setheading(90) # Draws the cloud at a specific angle
    cloud: int = 0 
    while cloud < 3:
        scene.circle(30, 180)
        scene.left(180)
        cloud += 1
    
    scene.end_fill()
    scene.penup()
    scene.setheading(0)
    scene.forward(50)


def draw_grass():
    scene.penup()
    scene.goto(-400, -350)  
    scene.pendown()
    scene.color(37, 181, 42)
    scene.begin_fill()
    
    grass: int = 0  
    while grass < 2:
        scene.forward(800)
        scene.left(90)
        scene.forward(199)
        scene.left(90)
        grass += 1
    
    scene.end_fill()

# Function to draw snowflakes
def draw_snowflake(x, y):
    scene.penup()
    scene.goto(x, y)
    scene.pendown()
    scene.color(255, 255, 255)
    scene.begin_fill()
    
    flake = 0  
    while flake < 6:
        scene.forward(10)
        scene.backward(10)
        scene.left(60)
        flake += 1
    
    scene.end_fill()

def main() -> None:
    # Set the drawing speed
    scene.speed(0)

    # Draw mountains
    draw_mountain(-300, -150, 200, 300, "gray")
    draw_mountain(100, -150, 150, 250, "dimgray")
    draw_mountain(-150, -150, 250, 400, "slategray")

    # Draw the sun
    draw_sun(300, 300, 50)

    # Draw clouds
    draw_cloud(-200, 250)
    draw_cloud(200, 200)  
    draw_cloud(-100, 180)

    # Draw grass at the bottom
    draw_grass()

    # Draw snowflakes
    for _ in range(50):
        x = random.randint(-400, 400)
        y = random.randint(0, 400)
        draw_snowflake(x, y)

    done ()

if __name__ == "__main__":
    main()