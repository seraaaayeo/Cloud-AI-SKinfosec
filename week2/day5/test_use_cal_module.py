import test_make_cal_module as cal

print("20+10 = ", cal.add(20, 10))
print("20-10 = ", cal.subtract(20, 10))
print("20*10 = ", cal.multiply(20, 10))
print("20/10 = ", cal.division(20, 10))

print("use_cal.py", __name__)
if __name__ == "__main__":
    print("use_cal.py 엔트리포인트")