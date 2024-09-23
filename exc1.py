# exc a
l1: list[int] = []
for i in range(1, 101):
    l1.append(i)
# exc b
print(f"fist number is {l1[0]}")
# exc c
print(f"last number is {l1[-1]}")
# exc d
print(f"l1's length is {len(l1)}")
# exc e
l2: list[int] = l1[2:12]
print(f"l2 = {l2}")
# exc f
l3: list[int] = l1[79:]
print(f"l3 = {l3}")
# exc g
l4: list[int] = l1[:18]
print(f"l4 = {l4}")
# exc h
print(l1[::-1])
# exc i
print(l1[1::2])
# exc j
print(l1[2::3])
# exc k
print(l1[6::7])
# exc l
print(l1[9::10])
# exc m
print(l1[98:64:-3])
# exc n
l1.insert(50, 999)
print(l1)
# exc o
l1.pop()
