'''
@function: delete data
'''
def ai_remove(name, ai_dict):
    for i in ai_dict:
        if(i["name"] == name):
            del ai_dict[ai_dict.index(i)]
    return print(f"수강생 {name}의 정보가 삭제되었습니다.")
