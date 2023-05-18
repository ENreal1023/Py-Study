#클래스
# class Waffle:
#     name = "waffle"
# choco = Waffle()
# print(choco.name)
# banana = Waffle()
# print(banana.name)

#클래스 - 2
# class Waffle:
#     name = "waffle"
# choco = Waffle()
# Waffle.name = "choco waffle"
# print(choco.name)
# banana = Waffle()

#클래스와 메소드 (객체별로 다른 속성을 부여하는 코드입니다.)
# class Waffle():
#     def setName(self,n):
#         self.name = n
# choco = Waffle()
# choco.setName("choco waffle")
# print(choco.name)
# banana = Waffle()
# banana.setName("banana waffle")
# print(banana.name)

#Avatar 클래스로 생성된 객체 byunsoo에 속성을 보여하는 코드입니다.
# class Avatar:
#     def setAvatar(self,height,skill):
#         self.height = height
#         self.skill = skill
# byunsoo = Avatar()
# byunsoo.setAvatar(120,'점프')
# print(byunsoo.height)
# print(byunsoo.skill)

#Avatar 클래스에 출력용 메소드를 추가한 코드입니다.
# class Avatar:
#     def setAvatar(self,height,skill):
#         self.height = height
#         self.skill = skill
#     def printAvatar(self):
#         print("키는",self.height,"cm","스킬은",self.skill,"입니다.")
# byunsoo = Avatar()
# byunsoo.setAvatar(120,'점프')
# byunsoo.printAvatar()