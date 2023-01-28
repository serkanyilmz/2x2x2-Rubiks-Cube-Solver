from moves import *
import time

# last holds the current scramble.
# curr holds the current scramble algorithm.
# move_change changes the order of curr.
def move_change(which=-1):
    # Increases move number.
    if -which > len(curr):
        curr.insert(0, 0)
    else:
        # Changes move s.a:4-5
        if curr[which] < 8:
            curr[which] += 1
        else:
            # Changes previous move s.a:109-110
            curr[which] = 0
            return (move_change(which - 1))
    # Pops notr curr
    if -which + 1 <= len(curr):
        if {curr[which - 1], curr[which]} in notr_moves:
            return (move_change(which))
    if which < -1:
        if {curr[which + 1], curr[which]} in notr_moves:
            return (move_change(which + 1))
    return (curr)

# make_moves changes the last with moves in curr.
def make_moves():
    for m in curr:
        if m == 0:
            last.update(move(f,0,last))
        elif m == 1:
            last.update(move(f, 1,last))
        elif m == 2:
            last.update(move(f, 2,last))
        elif m == 3:
            last.update(move(r,0,last))
        elif m == 4:
            last.update(move(r, 1,last))
        elif m == 5:
            last.update(move(r, 2,last))
        elif m == 6:
            last.update(move(u,0,last))
        elif m == 7:
            last.update(move(u, 1,last))
        elif m == 8:
            last.update(move(u, 2,last))

# takes the list curr. take its counter so cube can be solved. returns a string
def solution_of(curr):
    reverse={1:0,0:1,3:4,4:3,6:7,7:6}
    ret=[]
    for no in curr.copy()[::-1]:
        ret.append(reverse[no]) if no in reverse else ret.append(no)
    return ("".join([str(x) for x in ret]))

# poss is a set holding scrambles that already being holding.
file = open("test.txt", "w")
poss=set()
# curr holds the current scramble algorithm.
# curr is how to shuffle the solved cube
curr=[0] # 0 refers to F move
start_time = time.time()
a=1

while a<=6: ###### !!!!!!! IT MUST BE 12 NOT 6. It may cause damage on computer so if you try it is on your responsibility.
    # last is solved cube at first so everytime it starsts solved
    last={1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 1, 8: 1, 9: 2, 10: 2, 11: 2, 12: 2, 13: 3, 14: 3, 15: 3, 16: 3,
            17: 4, 18: 4, 19: 4, 20: 4, 21: 5, 22: 5, 23: 5, 24: 5}
    make_moves()
    # now last is shuffled
    string = "".join([str(x) for x in last.values()]) # how we hold dhuffled cube data
    if string not in poss:
        poss.add(string)
        file.write(string + " " + solution_of(curr) + "\n") # solution_off(curr) is the counter(reverse) of the shuffle.
    curr=move_change() # change how to shuffle
    if len(curr)>a:
        print(f"{round(time.time() - start_time, 2)}  {a}-move algorithms completed. ({len(poss)} algorithms)")
        a+=1