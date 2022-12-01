from colours_and_language import *
def solvable(dict):
    val=list(dict.values())
    for x in range(6):
        if x not in val or val.count(x)!=4:
            return colour_list[x]
    return "no_error"