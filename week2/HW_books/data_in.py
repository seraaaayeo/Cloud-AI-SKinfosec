def save_list(filename, ai_dict):
    with open(filename, "w") as file:
        for data in ai_dict:
            data = str(data)+"\n"
            file.write(data)