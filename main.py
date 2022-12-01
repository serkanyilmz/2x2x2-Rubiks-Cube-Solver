from cube import *


def main():
    root = Tk()
    root.title(lang["title"])
    root.geometry("470x450")
    root.config(bg=colours["default"])

    # Creates cube_window
    cube_grid(root)
    palette_grid(root)
    run_button_grid(root)
    root.mainloop()


main()
