import random
print("오징어 게임에 오신 것을 환영합니다")
print("홀짝 게임을 시작합니다 ")
a=random.randint(1,10) # 10개 이하의 무작위 수로 구슬의 개수가 나오게해야함.

# 구슬로 홀짝 게임 규칙
# 상대방이 구슬의 갯수를 정한다
for i in range(2):
    my = input("홀 짝? (잘 못쓰면 빵이지만 한번은 기회줄게) ") #고정되어 있는 값을 사용자가 입력받을 수 있었음 좋겠다.(1=홀,2=짝)
    if my == "홀" or my == "짝":
        dab = ""
        if a % 2 == 0:
            dab = "짝"
        else:
            dab = "홀"
            print("나 : 너 "+str(my)+"이지?")

# 틀리면 틀렸다
        if my==dab: # 만약에 내가 얘기한 홀과 짝중에 맞으면 맞다
            print("상대 : "+str(dab)+"입니다")
            print("당신이 맞혔습니다")
        else:
            print("상대 : 아닌데요?(씨익)"+str(dab)+"입니다")
            print("당신은 틀렸습니다")