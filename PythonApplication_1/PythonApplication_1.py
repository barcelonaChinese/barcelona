print("+---------------------------------------------------------------------+")
print("|                                                                     |")
print("|                   花有重开日, 人无再少年                               |")
print("|                                                                     |")
print("|                   欢迎来到, 人生重开模拟器                             |")
print("|                                                                     |")
print("+---------------------------------------------------------------------+")
# 设置初始属性
while True:
    print("请设定初始属性(可用总点数 20)")
    face = int(input("设定 颜值(1-10):"))
    strong = int(input("设定 体质(1-10):"))
    iq = int(input("设定 智力(1-10):"))
    home = int(input("设定 家境(1-10):"))

    if face < 1 or face > 10:
        print("颜值设置有误!")
        continue
    if strong < 1 or strong > 10:
        print("体质设置有误!")
        continue
    if iq < 1 or iq > 10:
        print("智力设置有误!")
        continue
    if home < 1 or home > 10:
        print("家境设置有误!")
        continue
    if face + strong + iq + home > 20:
        print("总点数超过了 20!")
        continue
    print("初始属性设定完成!")
    break