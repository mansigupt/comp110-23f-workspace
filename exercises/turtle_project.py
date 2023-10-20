"""EX05 - Turtle- Mountain scene with random snowflake presentation!"""
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
def draw_mountain(x: int, y: int, width: int, height: int, color: tuple[int, int, int]) -> None:
    """Simplified function to draw a mountain."""
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
def draw_sun(x: int, y: int, radius: int) -> None:
    """Simplified function to draw sun."""
    scene.penup()
    scene.fillcolor(255, 255, 0)
    scene.goto(x, y)
    scene.pendown()
    scene.begin_fill()
    
    scene.circle(radius)
    
    scene.end_fill()


# Function to draw a cloud
def draw_cloud(x: int, y: int) -> None:
    """Simplified function to draw clouds."""
    scene.penup()
    scene.goto(x, y)
    scene.pendown()
    scene.color(255, 255, 255)
    scene.begin_fill()
    
    # Draw the cloud's body (three humps) 
    scene.setheading(90)  # Draws the cloud at a specific angle
    cloud: int = 0 
    while cloud < 3:
        scene.circle(30, 180)
        scene.left(180)
        cloud += 1
    
    scene.end_fill()
    scene.penup()
    scene.setheading(0)
    scene.forward(50)


def draw_grass() -> None:
    """Function to draw grass."""
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
def draw_snowflake(x: int, y: int) -> None:
    """Function to draw snowflakes using random."""
    scene.penup()
    scene.goto(x, y)
    scene.pendown()
    scene.color(255, 255, 255)
    scene.begin_fill()
    
    flake: int = 0  
    while flake < 6:
        scene.forward(10)
        scene.backward(10)
        scene.left(60)
        flake += 1
    
    scene.end_fill()


def main() -> None:
    """Main function to draw the scene I coded above."""
    # Set the drawing speed
    scene.speed(0)

    # Draw mountains
    draw_mountain(-300, -150, 200, 300, (128, 128, 128))  # "gray"
    draw_mountain(100, -150, 150, 250, (105, 105, 105))  # "dimgray"
    draw_mountain(-150, -150, 250, 400, (112, 128, 144))  # "slategray"

    # Draw the sun
    draw_sun(300, 300, 50)

    # Draw clouds
    draw_cloud(-200, 250)
    draw_cloud(200, 200)  
    draw_cloud(-100, 180)

    # Draw grass at the bottom
    draw_grass()

    # Draw snowflakes
    snow_count: int = 0  # Initialize a counter variable
    while snow_count < 50:
        x = random.randint(-400, 400)
        y = random.randint(0, 400)
        draw_snowflake(x, y)
        snow_count += 1

    done()


if __name__ == "__main__":
    main()