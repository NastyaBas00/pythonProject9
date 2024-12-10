# try:
#     amount = int(input("fjjfjfjf"))
#     items_type = input("jdjdjdjdj")
# except:
#     print("error")
#
#
# for i in range(10):
#     print("dkkdkkd")


try:
    a = int(input("First num "))
    b = int(input("Second num "))

    print(a / b)
except ZeroDivisionError:
    print("ZeroDivisionError")






u = input("num ")

try:
    num = float(u)
    print("OOO ", num)
except ValueError:
    print("ValueError")



try:
    apples = int(input("Введи кіко яблучок маєш: "))
    if apples < 0:
        raise Exception("не мож менше нуля")
    part_num = int(input("fffff: "))
    part_amount = apples / part_num
except (ZeroDivisionError, ValueError):
    print("jffff")
except Exception as ex:
    print(ex)
except:
    print("bite")
finally:
    print("done")




try:
    a = int(input("First num "))
    if a < 0:
        raise Exception("н мож")
    print(a ** 0.5)
except:
    pass

