from tkinter import *
from control import *
from solve import *

# Every square has its own square_no 1 to 24.
# Every square has its own colour no 0 to 5. These will be kept in dict.
# dict={square_no : colour_no}
# Every click on cube will update dict.
dict={}
for square_no in range(24):
    dict[square_no]=5 # 5 is colour_code of white.

# Every square has its own coordinate in cube_window. It will be kept in coordinates.
# coordinates={ square_no :[row,column] }
coordinates={}
# surfaces_list has all surfaces top-left square coordinates.
surfaces_list = [[1, 3], [3, 1], [3, 3], [3, 5], [3, 7], [5, 3]]
square_no=0
for surface in surfaces_list:
    for y in [0,1]:
        for x in [0,1]:
            coordinates[square_no]=[surface[0]+y,surface[1]+x]
            square_no+=1


class Square:
    def __init__(self,square_no):
        self.square_no=square_no
        self.b = Button(cube_window, width=4, height=2, cursor="spraycan",
                        command=self.click, relief="solid")
        self.b.grid(row=coordinates[square_no][0], column=coordinates[square_no][1])  # ,padx=0.5,pady=0.5

    def click(self):
        dict[self.square_no]=chosen
        self.b["bg"]= colours[chosen]




def cube_grid(where):
    global msg
    msg = Label(text="Colour the cube!", font=("Arial", 20), bg=colours["default"],fg=colours["white"])
    msg.grid(row=0, column=0, columnspan=2, pady=20)
    global cube_window
    cube_window = LabelFrame(where, bd=0, bg=colours["default"])
    cube_window.grid(row=1, column=0, padx=20)
    for square_no in range(24):
        Square(square_no)


class PaletteButon:
    def __init__(self, colour_no):
        self.colour_no = colour_no
        self.b = Button(palette_window, bg=colours[self.colour_no],
                        width=10, height=2, bd=2,
                        command=self.click, relief="ridge", cursor="dot")
        self.b.pack()

    def click(self):
        for x in pal_lis:
            x.b.config(relief="ridge", bd=2)
        self.b.config(relief="solid", bd=5)
        global chosen
        chosen=self.colour_no


def palette_grid(where):
    global palette_window, rr, oo, gg, bb, ww, yy, pal_lis
    palette_window = LabelFrame(where, bd=0, bg=colours["default"])
    palette_window.grid(row=1, column=1, rowspan=2, padx=20)
    yy = PaletteButon(0)
    rr = PaletteButon(1)
    gg = PaletteButon(2)
    oo = PaletteButon(3)
    bb = PaletteButon(4)
    ww = PaletteButon(5)
    pal_lis=[yy, rr, gg, oo, bb, ww]
    yy.b.invoke()

    # Rewrite it later
    def clear_cube():
        ww.b.invoke()
        for square_no in range(24):
            Square(square_no).b.invoke()

    clear = Button(palette_window, bg=colours["clear"], text="Clear", width=10, height=2, command=clear_cube)
    clear.pack()

    def solved_cube():
        square_no=0
        for sur in range(6):
            pal_lis[sur].b.invoke()
            for times in range(4):
                Square(square_no).b.invoke()
                square_no+=1

    solved = Button(palette_window, bg="pink", text="Solved", width=10, height=2, command=solved_cube)
    solved.pack()

def run_button_grid(where):
    run = Button(where, text="Solve", font=("Arial", 18), width=20, relief="groove",
                 command=run_clicked)
    run.grid(row=2, column=0, sticky="s")
def dict_re(dict):
    antis=[[0,5],[1,3],[2,4]]
    hold={}
    new_colors={}
    new_colors[dict[6]]=1
    for x in antis:
        if dict[6] in x:
            x.remove(dict[6])
            new_colors[x[0]]=3
            break
    new_colors[dict[19]]=4
    for x in antis:
        if dict[19] in x:
            x.remove(dict[19])
            new_colors[x[0]]=2
            break
    new_colors[dict[22]]=5
    for x in antis:
        if dict[22] in x:
            x.remove(dict[22])
            new_colors[x[0]]=0
            break
    for key in dict.keys():
        a=dict[key]
        hold[key]=new_colors[a]
    return hold
def run_clicked():
    xx=dict_re(dict)
    #xx=dict.copy()
    error = solvable(xx)
    if error=="no_error":
        msg["text"] = lang["while_solving"]
        ret=try_to_solve(xx)
        if ret=="error":
            msg["text"] = "Not Found"
        elif ret=="already":
            msg["text"] = lang["already"]
        else:
            msg["text"]=ret


    else:
        msg["text"]=lang["error_message"].format(error)