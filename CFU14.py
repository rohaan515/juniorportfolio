import simplegui

def draw_handler(canvas):
    #create the drawing
    #canvas.draw_point([x,y],"color")
    canvas.draw_line([35,125], [145,125], 2, "blue")
    canvas.draw_line([45,25], [45,40], 2, "blue")
    canvas.draw_line([115,25], [115,40], 2, "blue")
    canvas.draw_line([15,105], [35,125], 2, "blue")
    canvas.draw_line([145,125], [165,105], 2, "blue")
    
    
frame = simplegui.create_frame("happy dots", 200,200)
frame.set_canvas_background("white")
frame.set_draw_handler(draw_handler)
frame.start()
