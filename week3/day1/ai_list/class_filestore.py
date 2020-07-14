import os.path
from class_domain import AIEntity

def save_data(ai_list):
    save_file = open("ai_list.dat", "w")
    for idx, entity in enumerate(ai_list):
        save_file.write(f"{idx}번째 | {entity.name},{entity.age},{entity.email},{entity.major}\n")
    save_file.close()

def read_data():
    ai_list = []
    fileExist = os.path.isfile("ai_list.dat")
    if fileExist:
        # read_file = open("ai_list.dat", "r")
        # print("success open")
        
        with open("ai_list.dat", "r") as file:
            for i in file:
              if len(i.split("|")) == 2:
                ai = i.split("|")[1].rstrip('\n').split(",")
                ai_list.append(AIEntity(ai[0].strip(), int(ai[1].strip()), ai[2].strip(), ai[3].strip()))  
            
        # while True:
        #     ai_data = read_file.readline()
        #     if len(ai_data.split("|"))  == 2:
        #         ai = ai_data.split("|")[1].rstrip('\n').split(",")
        #         ai_list.append(AIEntity(ai[0].strip(), int(ai[1].strip()), ai[2].strip(), ai[3].strip()))
        #     if not ai_data:
        #         break
        # read_file.close()
    print(ai_list)
    return ai_list
