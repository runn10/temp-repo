import math, tkinter, time

#Create the main window       
master = tkinter.Tk()
master.title("Phyllotaxis Algorithm Animator")

#Create the main canvas where the animation occurs
canvas = tkinter.Canvas(master, width = 400, height = 400)
canvas.config(background = "#000000")
canvas.grid(column = 0, row = 0)
 
def phyllotaxis_animate():
    canvas.delete("all")

    n = 0   # ordering number of a dot, outward from center
    c = 4   # scaling factor - changes distance dots are from center and
            # and from each other.

    while (True):
        a = n * 90
        r = c * math.sqrt(n)

        # polar to cartesian coordinate transformation
        x = r * math.cos(a) + 200
        y = r * math.sin(a) + 200
        if (x >= 400 and y >= 400):
            break
        color = '#0f9b86'
        outline = '#ff4c4f'
        canvas.create_oval(x, y, x + 10, y + 20, fill=color, outline=outline)
        n += 1
        canvas.update()

          
phyllotaxis_animate()
canvas.mainloop()










