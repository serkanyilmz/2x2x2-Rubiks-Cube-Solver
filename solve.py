f = [[3, 8, 22, 13], [4, 6, 21, 15], [9, 11, 12, 10]]
r = [[13, 15, 16, 14], [4, 12, 24, 17], [2, 10, 22, 19]]
u = [[1, 3, 4, 2], [9, 13, 17, 5], [10, 14, 18, 6]]
move_names=["F","F'","F2","R","R'","R2","U","U'","U2"]
possibilities=open("algorithms12.txt","r").readlines()
alg={}
for possibility in possibilities:
    sp=possibility.split()
    alg[sp[0]]=sp[1].rstrip()

def try_to_solve(dict):
    string="".join([str(x) for x in dict.values()])
    ans_list=[]
    if string in alg.keys():
        for x in alg[string]:
            ans_list.append(move_names[int(x)])
        return ans_list
    else:
        return "error"