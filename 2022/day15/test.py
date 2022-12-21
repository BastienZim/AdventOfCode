from tkinter import *

class BresenhamCanvas(Canvas):

    def draw_point(self, x, y, color="red"):
        self.create_line(x, y, x+1, y+1, fill=color)

#    def draw_circle_points(self, x, y, center_x, center_y, color="red"):
    def get_circle_points(self, x, y, center_x, center_y):
        center_x, center_y = 0,0
        '''Draw 8 points on a circle centered
           at center_x, center_y, by symmetry.'''
        aa = [(center_x + x, center_y + y),
                (center_x - x, center_y - y),  
                (center_x + x, center_y - y),
                (center_x - x, center_y + y)]
        # If x == y then these points will simply duplicate
        # points already drawn above. No need to repeat them then.
        if x != y:
            bb= [(center_x + y, center_y + x),
                (center_x - y, center_y - x),
                (center_x + y, center_y - x),
                (center_x - y, center_y + x)]
            return(list(set(aa+bb)))
        return(list(set(aa)))

    def draw_circle(self, center_x, center_y, radius, line_thickness):

        # Start at the top of the circle
        
        circle_pts = []
        for x in range(int(radius/2)+1):
            y = radius - x
            aa = self.get_circle_points(x, y, center_x, center_y)
            circle_pts = circle_pts+aa
        print(circle_pts)


def run():
    import math
    CANVAS_SIZE = 600

    root = Tk()
    canvas = BresenhamCanvas(root, width=CANVAS_SIZE, height=CANVAS_SIZE)
    canvas.pack()
    
    margin = CANVAS_SIZE / 10
    
    radius = margin*2
    
    n_circles = 1
    print(radius)
    for i in range(n_circles):
        center_x, center_y = 300,300
        for radius in [3]:
            canvas.draw_circle(center_x, center_y, radius, 2)
       
    
                
if __name__ == "__main__":
    run()
