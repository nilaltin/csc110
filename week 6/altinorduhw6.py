
CANVAS_WIDTH = 900
CANVAS_HEIGHT = 800

from Gui import *        


# 1. Draw one line grid
def draw_line_grid(canvas, top_left_x, top_left_y, width, num_lines, color):
    """Draws a square line grid of horizontal lines.

    top_left_x, top_left_y : coordinates of the left endpoint of the TOP line
    width                  : width (and height) of the grid
    num_lines              : how many horizontal lines
    color                  : line color (string)
    """

    if num_lines <= 0:
        return
    if num_lines == 1:
        # single line, just draw the top one
        canvas.line([[top_left_x, top_left_y],
                     [top_left_x + width, top_left_y]], fill=color)
        return

    # there are (num_lines - 1) vertical gaps
    gap = floor(width / (num_lines - 1))

    for i in range(num_lines):
        y = top_left_y - i * gap # go DOWN by decreasing y
        x1 = top_left_x
        x2 = top_left_x + width
        canvas.line([[x1, y], [x2, y]], fill=color)


# 2. Draw one fan
def draw_fan(canvas, cx, cy, width, num_lines, color, facing_up):
    """Draws a fan of lines from a common point (cx, cy).

    cx, cy        : common endpoint (center of the square)
    width         : width (and height) of the imaginary square
    num_lines     : number of lines in the fan
    color         : line color
    facing_up     : True  -> fan opens upward (endpoints on top edge)
                    False -> fan opens downward (endpoints on bottom edge)
    """

    if num_lines <= 0:
        return
    if num_lines == 1:
        # just one line straight up or down from the center
        half = width / 2.0
        end_y = cy + half if facing_up else cy - half
        canvas.line([[cx, cy], [cx, end_y]], fill=color)
        return

    half = width / 2.0

    # left corner x of the square
    start_x = cx - half

    # there are (num_lines - 1) horizontal gaps along the edge spanning "width"
    gap = floor(width / (num_lines - 1))

    # y for endpoints along either the top or bottom edge of the square
    if facing_up:
        end_y = cy + half
    else:
        end_y = cy - half

    for i in range(num_lines):
        end_x = start_x + i * gap
        canvas.line([[cx, cy], [end_x, end_y]], fill=color)



# 3. Main: draw the whole scene

def main():
    # Line grids (Figures 1–3)
    # Figure 1: width 120, top-left (-200, 300), 20 lines, brown
    draw_line_grid(canvas, -200, 300, 120, 20, 'brown')

    # Figure 2: width 200, top-left (135, 200), 5 lines, purple
    draw_line_grid(canvas, 135, 200, 200, 5, 'purple')

    # Figure 3: width 90, top-left (-300, -280), 8 lines, red
    draw_line_grid(canvas, -300, -280, 90, 8, 'red')

    # Fans (Figures A–C)
    # Figure A: width 120, center (0, 0), 10 lines, blue, facing up
    draw_fan(canvas, 0, 0, 120, 10, 'blue', True)

    # Figure B: width 200, center (-350, 0), 9 lines, orange, facing down
    draw_fan(canvas, -350, 0, 200, 9, 'orange', False)

    # Figure C: width 150, center (200, -200), 5 lines, green, facing down
    draw_fan(canvas, 200, -200, 150, 5, 'green', False)


g = Gui()
g.title('HW6 Lines')

# canvas is the drawing area
canvas = g.ca(width=CANVAS_WIDTH, height=CANVAS_HEIGHT)

main()
g.mainloop()

#Written report
"""
1. How did you go about starting this assignment? Where did you get stuck, if at all, and how did you get unstuck?

I started by reviewing the example grids and fans to understand the geometry behind how each line should shift.
I sketched a few examples on paper to visualize the spacing and endpoint changes. My main sticking point was calculating
the gap between lines so the total height or width matched the requested size. Once I realized the spacing is divided by
the number of gaps rather than the number of lines, the logic became much clearer and the functions worked as intended.

2. How did you test your program? Does your program meet the homework specification? What doesn't work as you'd like?

I tested my functions by calling them with different positions, widths, colors, and line counts to make sure the spacing
and alignment always adjusted correctly. After that, I used the exact values from the assignment to recreate the full scene.
The output matches the required figures and includes all six drawings. Everything works as expected, and there are no remaining issues.

3. What did you learn from this assignment? What would you do differently on the next project?

I learned how important it is to break down a visual problem into smaller geometric calculations. This assignment also
reinforced using functions properly so the same logic can be reused with different values.
Next time, I would start testing small pieces of the drawing earlier instead of trying to
complete a full figure before checking whether my math was correct.
"""
