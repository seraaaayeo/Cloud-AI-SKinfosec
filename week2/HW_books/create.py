import datetime

def register():
    name = str(input("Product name: "))
    price = int(input("Price: "))
    description = str(input("Description: "))
    
    now = datetime.datetime.now()
    product_num = str(now)

    ai_dict = {"Product name": name, "Price": price, "Description": description, "Product number": str(product_num)}
    print(f"도서 {name}의 정보가 등록되었습니다.")

    return ai_dict
