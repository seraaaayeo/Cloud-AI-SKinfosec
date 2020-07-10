'''
@function: Read data
'''
def read_data(filename):
    ai_list=[]
    with open(filename, "r") as file:
        for i in file:
            i = i.replace("\n", "")
            ai_list.append(i)
    return ai_list

def ai_list(ai_dict):
    print(ai_dict)
    return ai_dict
