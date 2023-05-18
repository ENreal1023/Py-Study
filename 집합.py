# 3가지 방법으로 만든 집합
# a = set([5,2,3,2,1,4])
# b = set("apple")
# c = {3,6,4,7,1,7}
# print(a,type(a))
# print(b, type(b))
# print(c, type(c))

#합집합, 교집합, 차집합
# - 합집합
# a = set([1,2,3])
# b = set([2,3,4])
# print(a | b)
# print(a.union(b))
# print(b.union(a))
# - 교집합
# a = set([1,2,3])
# b = set([2,3,4])
# print(a & b)
# print(a.intersection(b))
# print(b.intersection(a))
# - 차집합
# a = set([1,2,3])
# b = set([2,3,4])
# print(a - b)
# print(b - a)
# print(a.difference(b))
# print(b.difference(a))
