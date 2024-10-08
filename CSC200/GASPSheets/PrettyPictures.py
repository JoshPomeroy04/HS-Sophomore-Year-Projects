from gasp import *

begin_graphics()
def draw_guy(x, y):
    Circle((x, y), 40)    # Head
    Circle((x-15, y+10), 5)     # Left Eye
    Circle((x+15, y+10), 5)     # Right Eye
    Line((x, y+10), (x-10, y-10))   # Diagonal part of nose
    Line((x-10, y-10), (x+10, y-10))   # Straight part of nose
    Arc((x, y), 30, 200, 140)  # Mouth
    Line((x, y-40), (x, y-200))   # Body
    Line((x, y-100), (x-100, y-150))   # Left arm
    Line((x, y-100), (x+100, y-150))   # Right arm
    Line((x, y-200), (x-50, y-300))    # Left leg
    Line((x, y-200), (x+50, y-300))    # Right leg

draw_guy(300, 350)
update_when('key_pressed')
end_graphics()
