
'''
@function: 데이터 전체 반환
'''
def ai_list(ai_dict):
    print(ai_dict)
    return ai_dict

'''
@function: 특정 데이터 반환
'''
def ai_search(name, ai_dict):
    for i in ai_dict:
        if i["Product name"] == name:
            return i

'''
@function: 특정 데이터의 인덱스 반환
'''
def is_exist(name, ai_dict):
    index = 0
    for i in ai_dict:
        if i["Product name"] == name:
           return index
        index +=1

'''
@function: 특정 데이터의 등록번호 반환
'''
def ai_num(name, ai_dict):
    for i in ai_dict:
        if i["Product name"] == name:
            return i["Product number"]