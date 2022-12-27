f = [[3, 8, 22, 13], [4, 6, 21, 15], [9, 11, 12, 10]]
r = [[13, 15, 16, 14], [4, 12, 24, 17], [2, 10, 22, 19]]
u = [[1, 3, 4, 2], [9, 13, 17, 5], [10, 14, 18, 6]]
move_names=["F","F'","F2","R","R'","R2","U","U'","U2"]

data_list=[open("./data/data1.txt","r"),open("./data/data2.txt","r"),open("./data/data3.txt","r"),open("./data/data4.txt","r"),open("./data/data5.txt","r"),open("./data/data6.txt","r")]
alg={}
for data in data_list:
    for possibility in data.readlines():
        sp=possibility.split()
        alg[sp[0]]=sp[1].rstrip()
print(len(alg))

def try_to_solve(dict):
    string="".join([str(x) for x in dict.values()])
    ans_list=[]
    if string in alg.keys():
        for x in alg[string]:
            ans_list.append(move_names[int(x)])
        return ans_list
    else:
        return "error"