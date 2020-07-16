def save_list(filename, ai_dict):
    with open(filename, "w") as file:
        for data in ai_dict:
            data = str(data)+"\n"
            file.write(data)

def read_data(filename):
    ai_list=[]
    with open(filename, "r") as file:
        for i in file:
            i = i.replace("\n", "")
            ai_list.append(i)
    return ai_list