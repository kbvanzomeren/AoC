with open("day1.txt", "r") as fd:
    x = [int(n) for n in fd.read().splitlines()]

dx = list(x)

#A
print([(2020 - j) * j for j in x if (2020 - j) in x])
# for i in x:
#     y = 2020 - i
#     if y in x:
#         print(i*y)
#         break
#
# #B
# for i in x:
#     dx.remove(i)
#     for j in dx:
#         y = 2020 - i - j
#         if y in x:
#             print(i*j*y)
