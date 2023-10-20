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
    while mountain < 3:  # While function to draw three different triangles for mountains.
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
    
    scene.circle(radius)  # Draw a circle with the specified radius
    
    scene.end_fill()


# Function to draw a cloud
def draw_cloud(x: int, y: int) -> None:
    """Simplified function to draw clouds."""
    scene.penup()
    scene.goto(x, y)
    scene.pendown()
    scene.color(255, 255, 255)  # Set the color to white in RGB format
    scene.begin_fill()
    
    # Draw the cloud's body (three humps) 
    scene.setheading(90)  # Draws the cloud at a specific angle
    cloud: int = 0 
    while cloud < 3:
        scene.circle(30, 180)  # Draw a hump of the cloud
        scene.left(180)  # Rotate to draw the next hump
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
    scene.color(37, 181, 42)  # Dark green color in RGB
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
    scene.color(255, 255, 255)  # Set the color to white in RGB
    scene.begin_fill()
    
    flake: int = 0  # Initialize a counter for the snowflake's parts
    while flake < 6:  # Loop to draw the six parts of the snowflake
        scene.forward(10)
        scene.backward(10)
        scene.left(60)
        flake += 1
    
    scene.end_fill()


def main() -> None:
    """Main function to draw the scene I coded above."""
    scene.speed(0)  # Set the drawing speed to the maximum speed

    # Function call to draw mountains
    draw_mountain(-300, -150, 200, 300, (128, 128, 128))  # "gray"
    draw_mountain(100, -150, 150, 250, (105, 105, 105))  # "dimgray"
    draw_mountain(-150, -150, 250, 400, (112, 128, 144))  # "slategray"

    # Function call to draw the sun
    draw_sun(300, 300, 50)  # Draw a sun with a radius of 50.

    # Function call to draw the clouds
    draw_cloud(-200, 250)
    draw_cloud(200, 200)  
    draw_cloud(-100, 180)

    # Function call to draw the grass at the bottom
    draw_grass()

    # Draw snowflakes
    snow_count = 0  # Initialize a counter variable for the snowflakes
    while snow_count < 50:  # Draw 50 RANDOM snowflakes
        x = random.randint(-400, 400)  # Generate a random x-coordinate within the scene
        y = random.randint(0, 400)  # Generate a random y-coordinate within the scene
        draw_snowflake(x, y)  # Function call to draw snowflake at random location
        snow_count += 1

    done()  # Finish drawing and display the scene


if __name__ == "__main__":
    main()