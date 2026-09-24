# This file is just for referencing some code that will be used later in the project

from imports import *

rectangle = Rect(0, 0, 100, 100)        # Create the rectangle
rectangle_surface = Surface((rectangle.width, rectangle.height))        # Create a surface for the rectangle

while RUNNING:

    rectangle_surface.fill(WHITE)        # Fill the rectangle surface with white color
    render_screen.blit(rectangle_surface, rectangle) # Render the rectangle
    
    if rectangle.collidepoint(mouse.get_pos()):
        print("Mouse is over the rectangle!")