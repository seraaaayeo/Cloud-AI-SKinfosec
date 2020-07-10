def add(val1, val2):
    return val1+val2

def subtract(val1, val2):
    return val1-val2

def multiply(val1, val2):
    return val1*val2

def division(val1, val2):
    if val2==0:
        print("divion is ZERO")
    return val1/val2

print("calculator mocule ", __name__)
    

if __name__=="__main__":
    print("calculator_mldule 엔트리포인트")