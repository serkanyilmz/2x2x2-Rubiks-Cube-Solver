from library import *

# LOADING WHOLE SCRAMBLED CASES TO THE PROGRAM
# GitHub allows to load files wit max 25 mb capasity, thus I split the data file.
data_list = [open("./data/data1.txt", "r"), open("./data/data2.txt", "r"), open("./data/data3.txt", "r"),
             open("./data/data4.txt", "r"), open("./data/data5.txt", "r"), open("./data/data6.txt", "r")]
# alg (dictionary) will hold solutions for all scrambled cases.
# Number of cases will be 3.674.160 which will be equal to len(alg).
alg = {}
for data in data_list:
    for line in data.readlines():
        line.rstrip()
        # for example line can be "232305103412055243144150 6040706161"
        sp = line.split()
        # sp= ["232305103412055243144150" , "6040706161"]
        alg[sp[0]] = sp[1]
        # sp[0] is every colour on cube.
        # sp[1] is the solution for sp[0].
        # alg ={scramble : solution}
        # alg ={"232305103412055243144150":"6040706161"}


# SOLUTION
# When run button clicked.
def solve(the_dict):
    scramble="".join([str(x) for x in the_dict.values()]) # scramble looks like "232305103412055243144150".
    solution_moves=[]
    for x in alg[scramble]: # alg[scramble] is something like "6040706161".
        solution_moves.append(move_names[int(x)])
    return " ".join(solution_moves) # returns something like "U F R' F U' F U F' U F'"