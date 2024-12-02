import simplegui

# Frame setup
frame = simplegui.create_frame("Thanksgiving Drawing", 600, 400)

# Draw handler function
def draw(canvas):
    # Drawing a circle
    canvas.draw_circle((300, 200), 50, 5, "Brown", "Orange")
    # Drawing a polygon
    canvas.draw_polygon([(250, 250), (350, 250), (300, 300)], 5, "Red", "Yellow")
    # Drawing a circle
    canvas.draw_circle((265, 200), 10, 5, "Brown", "black")
    # Drawing a circle
    canvas.draw_circle((335, 200), 10, 5, "Brown", "black")
    # Drawing a line
    canvas.draw_line((65, 50), (350, 105), 5, "red")
    # Drawing a line
    canvas.draw_line((65, 60), (350, 105), 5, "orange")
    # Drawing a line
    canvas.draw_line((65, 70), (350, 105), 5, "yellow")
    # Drawing a line
    canvas.draw_line((65, 80), (350, 105), 5, "orange")
    # Drawing a line
    canvas.draw_line((65, 40), (350, 105), 5, "orange")
    # Drawing a line
    canvas.draw_line((65, 90), (350, 105), 5, "red")
    # Drawing a line
    canvas.draw_line((65, 100), (350, 105), 5, "orange")
    # Drawing a line
    canvas.draw_line((65, 110), (350, 105), 5, "yellow")
    # Drawing a line
    canvas.draw_line((65, 120), (350, 105), 5, "orange")
    # Drawing a line
    canvas.draw_line((65, 120), (350, 105), 5, "orange")
    # Drawing a line
    canvas.draw_line((250, 100), (500, 160), 5, "red")
    # Drawing a line
    canvas.draw_line((250, 100), (500, 150), 5, "orange")
    # Drawing a line
    canvas.draw_line((250, 100), (500, 140), 5, "yellow")
    # Drawing a line
    canvas.draw_line((250, 100), (500, 130), 5, "orange")
    # Drawing a line
    canvas.draw_line((250, 100), (500, 120), 5, "red")
    # Drawing a line
    canvas.draw_line((250, 100), (500, 110), 5, "orange")
     # Drawing a line
    canvas.draw_line((250, 100), (500, 100), 5, "red")
    # Drawing a line
    canvas.draw_line((250, 100), (500, 90), 5, "orange")
    # Drawing a line
    canvas.draw_line((250, 100), (500, 80), 5, "yellow")
    # Drawing a line
    canvas.draw_line((250, 100), (500, 70), 5, "orange")
    # Drawing a line
    canvas.draw_line((250, 100), (500, 60), 5, "red")
    
   
    # Drawing a circle
    canvas.draw_circle((300, 100), 70, 5, "Brown", "Orange")
# Assign draw handler to the frame

frame.set_draw_handler(draw)
# Start the frame
frame.set_canvas_background("cyan")
frame.start()
