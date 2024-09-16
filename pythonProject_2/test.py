import math

# while True:
#     face =int(input("face:"))
#
#     if face<1 or face>10:
#         print("wrong")
#         continue
#     print("finish")
#     break

def test():
    print("test")

a=(1,2,3)
b=[4,5,6]
c={7:"a",8:"b",9:"c"}
print(4 in a)
print(4 in b)
print(7 in c)
print("c" in c)

# for a in range(1,3):
#     print(a)
#
# for b in range(1,3):
#     print(b)

for k in a:
    print(k)

for k in b:
    print(k)

for k in c:
    print(k,":",c[k])

test()

print(math.exp(2))

