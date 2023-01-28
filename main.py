from tkinter import *
from solution import *

def main():
    root=Tk()
    root.title(lang["title"])
    root.iconbitmap('images/cube.ico')
    root.geometry("470x465")
    root.config(bg=colours["default"])

    # HOLDING DATA
    # Every square has its own square_no 0 to 23.
    # Every square has its own colour no 0 to 5. These will be kept in the_dict.
    # the_dict={square_no : colour_no}
    # Every click on cube will update the_dict.
    the_dict={}
    for square_no in range(24):
        the_dict[square_no]=5 # 5 is colour_code of white.
    # Every square has its own coordinate in cube_window. It will be kept in coordinates.
    # coordinates={ square_no :[row,column] }
    coordinates={}
    # surfaces_list has all surfaces top-left square coordinates.
    # Every surface has 4 square.
    surfaces_tuple=((0,2),(2,0),(2,2),(2,4),(2,6),(4,2))
    square_no=0
    for surface in surfaces_tuple:
        for y in (0,1):
            for x in (0,1):
                coordinates[square_no]=[surface[0]+y,surface[1]+x]
                square_no+=1

    # MESSAGE LABEL
    msg = Label(root,text=lang["first_message"], font=("Arial", 20), bg=colours["message_back"],fg=colours["message_font"],
                width=26,pady=8,relief="solid",border=1)
    msg.grid(row=0, column=0, columnspan=2, pady=25)

    # CUBE WINDOW
    cube_window = LabelFrame(root, bd=0, bg=colours["default"])
    cube_window.grid(row=1, column=0, padx=20)
    # Creating squares
    class Square:
        def __init__(self,square_no):
            self.square_no=square_no
            self.b = Button(cube_window, width=4, height=2, cursor="spraycan",
                            command=self.click, relief="solid")
            self.b.grid(row=coordinates[square_no][0], column=coordinates[square_no][1])

        def click(self):
            the_dict[self.square_no]=chosen
            self.b["bg"]= colours[colour_list[chosen]]
            if msg["text"]!=lang["first_message"]:
                msg["text"]=lang["first_message"]
    for square_no in range(24):
        Square(square_no)

    # PALETTE WINDOW
    palette_window = LabelFrame(root, bd=0, bg=colours["default"])
    palette_window.grid(row=1, column=1, rowspan=2, padx=20)
    class PaletteButton:
        def __init__(self, colour_no):
            self.colour_no = colour_no
            self.b = Button(palette_window, bg=colours[colour_list[self.colour_no]],width=10, height=2, bd=2,
                            command=self.click, relief="ridge", cursor="dot")
            self.b.pack()
        def click(self):
            for x in range(6):
                button_list[x].b.config(relief="ridge", bd=2)
            self.b.config(relief="solid", bd=5)
            global chosen
            chosen=self.colour_no       
    button_list=[PaletteButton(0),PaletteButton(1),PaletteButton(2),PaletteButton(3),PaletteButton(4),PaletteButton(5)]
    button_list[0].b.invoke()# Selects yellow
    def clear_cube():
        button_list[5].b.invoke()# 5 = white
        for square_no in range(24):
            Square(square_no).b.invoke()
        button_list[0].b.invoke()# Selects yellow
    clear_button = Button(palette_window, bg=colours["clear"], text="Clear", width=10, height=2, command=clear_cube)
    clear_button.pack()
    def solved_cube():
        square_no=0
        for sur in range(6):
            button_list[sur].b.invoke()
            for times in range(4):
                Square(square_no).b.invoke()
                square_no+=1
        button_list[0].b.invoke()# Selects yellow
    solved_button = Button(palette_window, bg="pink", text="Solved", width=10, height=2, command=solved_cube)
    solved_button.pack()

    # RUN BUTTON
    def reorganise(the_dict):
        opposites={0:5,5:0,1:3,3:1,2:4,4:2}
        new_colors={} # {old number:new number}
        new_colors[the_dict[6]]=1
        new_colors[opposites[the_dict[6]]]=3
        new_colors[the_dict[19]]=4
        new_colors[opposites[the_dict[19]]]=2
        new_colors[the_dict[22]]=5
        new_colors[opposites[the_dict[22]]]=0
        hold_the_dict={} # It will be the_dict
        for key in the_dict.keys():
            hold_the_dict[key]=new_colors[the_dict[key]]
        return hold_the_dict

    def run_clicked():
        try:
            ret=solve(reorganise(the_dict))
            if ret=="F' F2 F'":
                msg["text"]=lang["already"]
            else:
                msg["text"]=ret
        except:
            msg["text"]=lang["impossible"]
            for x in range(6):
                if list(the_dict.values()).count(x)!=4:
                    msg["text"]=lang["error_message"].format(colour_list[x])
                    break
        

    run_button = Button(root, text="Solve", font=("Arial", 18), width=20, relief="groove",command=run_clicked)
    run_button.grid(row=2, column=0, sticky="s")


    root.mainloop()
main()