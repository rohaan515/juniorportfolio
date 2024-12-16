import simplegui
import random

# Global variable
santa_pos = [300, 300]  # Start position of the santa

# Constants
WIDTH = 600
HEIGHT = 600

# Function to draw the scene
def draw_handler(canvas):
    # Use the global variable
    global santa_pos
    
    # Draw background (snow)
    canvas.draw_polygon([(0, 0), (WIDTH, 0), (WIDTH, HEIGHT), (0, HEIGHT)], 1, "LightBlue", "LightBlue")
    
    # Draw snow (circles)
    for i in range(5):
        x = random.randint(0, WIDTH)
        y = random.randint(0, HEIGHT)
        radius = random.randint(2, 5)
        canvas.draw_circle([x, y], radius, 1, "White", "White")
    
    # Draw snow (circles)
    for i in range(5):
        x = random.randint(100, 500)
        y = random.randint(100, 500)
        radius = random.randint(2, 5)
        canvas.draw_circle([x, y], radius, 1, "white", "white")
    
    # Draw santa (polygon)
    santa_points = [[santa_pos[0], santa_pos[1] - 20],  # top
                        [santa_pos[0] - 15, santa_pos[1] + 15],  # left bottom
                        [santa_pos[0] + 15, santa_pos[1] + 15]]  # right bottom
    canvas.draw_polygon(santa_points, 2, "gold", "red")
    
    # Draw santa trail (lines)
    trail_length = 5
    for i in range(trail_length):
        x_offset = santa_pos[0] - i * 10
        y_offset = santa_pos[1] + i * 2
        canvas.draw_line([santa_pos[0], santa_pos[1]], [x_offset, y_offset], 2, "White")
    
    # Draw the boundary lines (frame of the canvas)
    canvas.draw_line([0, 0], [WIDTH, 0], 2, "White")  # Top boundary
    canvas.draw_line([WIDTH, 0], [WIDTH, HEIGHT], 2, "White")  # Right boundary
    canvas.draw_line([WIDTH, HEIGHT], [0, HEIGHT], 2, "White")  # Bottom boundary
    canvas.draw_line([0, HEIGHT], [0, 0], 2, "White")  # Left boundary
    
    # Move santa (modifying the global variable)
    santa_pos[0] += 2  # Move right
    if santa_pos[0] > WIDTH:
        santa_pos[0] = 0  # Reset position when off screen

# Set up the frame
frame = simplegui.create_frame('Santas sleigh', WIDTH, HEIGHT)
frame.set_canvas_background("Black")

# Set the draw handler
frame.set_draw_handler(draw_handler)

# Start the frame
frame.start()
