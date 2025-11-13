
# CSC 110 - Scene Assignment (House, Tree, Clouds, Flower) 
# Author: Nil Altinordu
# Description:
#   A garden scene made from 4 parameterized elements:
#   houses, trees, clouds, and flowers. Each function takes (x, y, size)
#   and draws multiple GUI shapes.
#   main() calls each element 3 times.


import Gui

CANVAS_WIDTH  = 900
CANVAS_HEIGHT = 550

def draw_cloud(cx, cy, r, color='white'):
    """Draw one 3-puff cloud from circles (integer coords/sizes)."""
    r = int(r)
    x1 = int(cx - r * 4 // 5); y1 = int(cy)
    x2 = int(cx);              y2 = int(cy + r * 2 // 10)
    x3 = int(cx + r * 4 // 5); y3 = int(cy)
    canvas.circle([x1, y1], r, fill=color, width=0)
    canvas.circle([x2, y2], int(r + r // 10), fill=color, width=0)
    canvas.circle([x3, y3], r, fill=color, width=0)

def draw_house(base_x, base_y, size, body_color='yellow', roof_color='red'):
    """
    Draw a house.
    base_x, base_y : center of the bottom edge of the body
    size           : overall height of the house (pixels)
    """
    body_h = size * 60 // 100
    body_w = size * 70 // 100
    left   = base_x - body_w // 2
    right  = base_x + body_w // 2
    bottom = base_y
    top    = base_y + body_h

    # Body
    canvas.rectangle([[int(left), int(bottom)], [int(right), int(top)]],
                     fill=body_color, width=0)

    # Door
    door_w = body_w * 18 // 100
    door_h = body_h * 45 // 100
    d_left  = base_x - door_w // 2
    d_right = base_x + door_w // 2
    d_top   = bottom + door_h
    canvas.rectangle([[int(d_left), int(bottom)], [int(d_right), int(d_top)]],
                     fill='black', width=0)

    # Window 
    win_w = body_w * 22 // 100
    win_h = body_h * 20 // 100
    w_left   = left + body_w * 12 // 100
    w_right  = w_left + win_w
    w_bottom = bottom + body_h * 45 // 100
    w_top    = w_bottom + win_h
    canvas.rectangle([[int(w_left), int(w_bottom)], [int(w_right), int(w_top)]],
                     fill='white', width=1)

    # Roof (triangle)
    roof_peak = [int(base_x), int(top + size * 28 // 100)]
    lpt       = [int(left),   int(top)]
    rpt       = [int(right),  int(top)]
    canvas.polygon([roof_peak, lpt, rpt], fill=roof_color, width=0)

    #test line:canvas.line([[int(base_x), int(base_y)], [int(base_x), int(base_y + size)]], fill='magenta')

def draw_tree(base_x, base_y, size, trunk_color='black', foliage_color='green'):
    """
    base_x, base_y : center of trunk base
    size           : overall tree height
    """
    # Trunk
    trunk_w = size * 12 // 100
    trunk_h = size * 35 // 100
    left  = base_x - trunk_w // 2
    right = base_x + trunk_w // 2
    bottom = base_y
    top    = base_y + trunk_h
    canvas.rectangle([[int(left), int(bottom)], [int(right), int(top)]],
                     fill=trunk_color, width=0)

    # Foliage layers 
    layer_h = size * 22 // 100
    base_w  = size * 60 // 100

    # Layer 1 (largest)
    y0 = top
    half_w = base_w // 2
    apex = [int(base_x), int(y0 + layer_h)]
    lpt  = [int(base_x - half_w), int(y0)]
    rpt  = [int(base_x + half_w), int(y0)]
    canvas.polygon([apex, lpt, rpt], fill=foliage_color, width=0)

    # Layer 2 (medium)
    y1 = top + layer_h * 7 // 10
    half_w2 = (base_w * 85 // 100) // 2
    apex2 = [int(base_x), int(y1 + layer_h)]
    lpt2  = [int(base_x - half_w2), int(y1)]
    rpt2  = [int(base_x + half_w2), int(y1)]
    canvas.polygon([apex2, lpt2, rpt2], fill=foliage_color, width=0)

    # Layer 3 (smallest)
    y2 = y1 + layer_h * 7 // 10
    half_w3 = (base_w * 70 // 100) // 2
    apex3 = [int(base_x), int(y2 + layer_h)]
    lpt3  = [int(base_x - half_w3), int(y2)]
    rpt3  = [int(base_x + half_w3), int(y2)]
    canvas.polygon([apex3, lpt3, rpt3], fill=foliage_color, width=0)

    # TEST LINE
    # canvas.line([[int(base_x), int(base_y)], [int(base_x), int(base_y + size)]], fill='magenta')

def draw_clouds(center_x, center_y, size, color='white'):
    """
    Draw a 3-cloud cluster using three calls to draw_cloud (no loop).
    center_x, center_y: cluster center; size controls overall scale.
    """
    r = size * 18 // 100
    draw_cloud(int(center_x - size * 25 // 100), int(center_y + size * 5 // 100), r, color)
    draw_cloud(int(center_x + 0),                 int(center_y + size * 10 // 100), r + r // 10, color)
    draw_cloud(int(center_x + size * 28 // 100),  int(center_y + 0), r, color)

    # TEST LINE
    # canvas.line([[int(center_x), int(center_y)], [int(center_x), int(center_y + size)]], fill='magenta')

def draw_flower(base_x, base_y, size, petal_color='magenta', center_color='yellow'):
    """
    Draw a flower (stem + 6 petals + center) with the base exactly on the grass line.
    base_x, base_y : flower base (will be placed on grass by caller)
    size           : flower height
    """
    stem_h = size * 65 // 100
    stem_w = max(2, size * 3 // 100)

    # Stem
    canvas.line([[int(base_x), int(base_y)], [int(base_x), int(base_y + stem_h)]],
                fill='green', width=int(stem_w))

    # Simple leaf (triangle)
    leaf_len = size * 22 // 100
    leaf_wid = size * 10 // 100
    leaf_y = base_y + stem_h * 45 // 100
    canvas.polygon([
        [int(base_x), int(leaf_y)],
        [int(base_x + leaf_len), int(leaf_y + leaf_wid // 2)],
        [int(base_x + leaf_len * 85 // 100), int(leaf_y - leaf_wid // 2)]
    ], fill='green', width=0)

    # Petals (6 circles)
    head_y = base_y + stem_h
    pr = size * 9 // 100
    # up
    canvas.circle([int(base_x), int(head_y + pr * 16 // 10)], int(pr), fill=petal_color, width=0)
    # down
    canvas.circle([int(base_x), int(head_y - pr * 16 // 10)], int(pr), fill=petal_color, width=0)
    # right
    canvas.circle([int(base_x + pr * 16 // 10), int(head_y)], int(pr), fill=petal_color, width=0)
    # left
    canvas.circle([int(base_x - pr * 16 // 10), int(head_y)], int(pr), fill=petal_color, width=0)
    # up-right
    off = pr * 11 // 10
    canvas.circle([int(base_x + off), int(head_y + off)], int(pr), fill=petal_color, width=0)
    # up-left
    canvas.circle([int(base_x - off), int(head_y + off)], int(pr), fill=petal_color, width=0)

    # Center
    canvas.circle([int(base_x), int(head_y)], int(pr * 95 // 100), fill=center_color, width=0)


def draw_background():
    #Green ground strip and a yellow sun, and blue sky background
    ground_top = -CANVAS_HEIGHT // 2 + 60
    canvas.rectangle(
        [[-CANVAS_WIDTH // 2, int(ground_top)], [CANVAS_WIDTH // 2, -CANVAS_HEIGHT // 2]],
        fill='green', width=0
    )
    canvas.circle([CANVAS_WIDTH // 2 - 70, CANVAS_HEIGHT // 2 - 70], 40, fill='yellow', width=0)
    return ground_top  # so flowers can touch the grass

def main():
    ground_top = draw_background()

    # Clouds (3)
    draw_clouds(-280,  190, 120)
    draw_clouds(   0,  210, 100)
    draw_clouds( 280,  170, 110)

    # Houses (3) — spaced apart
    draw_house(-280, -120, 140, body_color='yellow', roof_color='red')
    draw_house(   0, -110, 120, body_color='yellow', roof_color='red')
    draw_house( 280, -100, 130, body_color='yellow', roof_color='red')

    # Trees (3) — placed BETWEEN houses and away from them
    # between -280 and 0 -> -140; between 0 and +280 -> +140; and one at 0 is fine if spaced
    draw_tree(-140, -60, 150, trunk_color='black', foliage_color='green')
    draw_tree( 140, -55, 160, trunk_color='black', foliage_color='green')
    draw_tree(   0, -65, 130, trunk_color='black', foliage_color='green')

    # Flowers (3) — base exactly ON the grass line
    draw_flower(-260, int(ground_top), 120, petal_color='magenta', center_color='yellow')
    draw_flower(   0, int(ground_top), 130, petal_color='magenta', center_color='yellow')
    draw_flower( 260, int(ground_top), 120, petal_color='magenta', center_color='yellow')


win = Gui.Gui()
win.title('My Garden Scene')
canvas = win.ca(width=CANVAS_WIDTH, height=CANVAS_HEIGHT, bg='blue')  
main()
win.mainloop()

# Written Report
"""
1) Getting started / stuck?
I selected four elements (house, tree, clouds, flower) and defined each with (x, y, size).
Where I mostly got stuck was with the positioning of all of my elements. I could not get the trees
or flowers to the place that I wanted, this took a lot of trial and error (to be honest I'm still not
100% happy with the placement of all trees, but I don't have infinite time to complete this). 

2) Testing and spec compliance:
I tested each drawing function by calling it with different positions and sizes to make sure
the scaling worked correctly. I also used the vertical “test line”
(commented out now) to verify that each element used its parameters properly.


3) What I learned / next time:
I learned how helpful it is to break a big drawing into smaller, reusable parts.
Writing one clear function for each scene element made it easier to organize my code
and make quick layout changes later. This project showed me how functional decomposition
simplifies both testing and creativity. Once each function worked, building the full scene
felt like arranging puzzle pieces. Next time, I’d plan my coordinates more carefully on paper
first to save time adjusting placements in code.

"""
