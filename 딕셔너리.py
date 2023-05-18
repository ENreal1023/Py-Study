#딕셔너리
# dic = {'Unreal':'파이썬','c':'c언어','java':'자바'}
# print(dic["Unreal"])
# print(dic["c"])
# print(dic["java"])

#KEY에 문자열 자료형을, VALUE에는 여러 자료형
# dic = {"int":1,"str":"문자","list":[1,2],"tuple":(1,2),"dict":{"Unreal":"언리얼"}}
# print(dic["int"])
# print(dic["str"])
# print(dic["list"])
# print(dic["tuple"])
# print(dic["dict"])

#key, value 쌍을 추가하는 코드
# dic = {"a":"apple","b":"banana","c":"cool"}
# dic["d"]="dictionary"
# print(dic)

#update() 함수로 여러 개의 key, value 쌍을 추가
# dic = {"a":"apple","b":"banana","c":"cool"}
# dic.update({"c":"cold","d":"dictionary","e":"elevator"})
# print(dic)

#예약어인 del로 key, value 쌍을 삭제하는 코드
# dic = {"a":"apple","b":"banana","c":"cool"}
# del dic["a"]
# print(dic)

#value 값을 수정하는 코드입니다
# dic = {"a":"apple","b":"banana","c":"cool"}
# dic["c"]="coconut"
# print(dic)

#Keys() 함수로 딕셔너리의 key 값을 출력하는 코드
# dic = {"a":"apple","b":"banana","c":"cool"}
# print(dic.keys())

#----------------------------------- For문 -----------------------------------

#Keys() 함수로 for 반복문을 사용한 코드
# dic = {"a":"apple","b":"banana","c":"cool"}
# for k in dic.keys():
#     print(k, end="")
#     print(dic[k],end="")

#value() 함수로 딕셔너리의 value 값을 출력
# dic = {"a":"apple","b":"banana","c":"cool"}
# print(dic.values())

#values() 함수로 for 반복문을 사용한 코드
# dic = {"a":"apple","b":"banana","c":"cool"}
# for v in dic.values():
#     print(v,end="")

#item() 함수로 딕셔너리의 key, value 쌍을 출력
# dic = {"a":"apple","b":"banana","c":"cool"}
# print(dic.items())

#items() 함수로 딕셔너리의 key,value 쌍을 출력하는 코드
# dic = {"a":"apple","b":"banana","c":"cool"}
# for k,v in dic.items():
#     print(k,v)



