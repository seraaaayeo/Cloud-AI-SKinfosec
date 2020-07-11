
def read_data(filename):
    ai_list=[]
    with open(filename, "r") as file:
        for i in file:
            i = i.replace("\n", "")
            ai_list.append(i)
    return ai_list