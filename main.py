import random
print("오징어 게임에 오신 것을 환영합니다")
print("홀짝 게임을 시작합니다 ")
# 상대방 구슬의 갯수를 정한다
a=random.randint(1,10) 
# 참가자가 가진 구슬의 갯수
marble=10

# 구슬로 홀짝 게임 규칙
for i in range(5):
    # 구슬의 개수를 알려주자
    print("당신의 구슬의 갯수: {}개".format(marble))
    try: #try/except 부분은 오류가 나는 경우에 대체할수있음
        # 구슬의 갯수 베팅
        bet = int(input("구슬 몇 개 베팅? ")) #input은 반드시 문자열로 인식하므로 int로 감싸준다.
    except:
        print("숫자만 입력해라~")
        continue
    if marble < bet:
        print("당신이 가진 구슬이 부족하다 다시 베팅하시오")
        continue #for문의 처음으로 돌아가는것
    my = input("상대 손에있는 구슬은 홀일까 짝일까? (홀or짝 입력) : ") #고정되어 있는 값을 사용자가 입력받을 수 있었음 좋겠다.(1=홀,2=짝)
    if my == "홀" or my == "짝":
        if a % 2 == 0:
            dab = "짝"
        else:
            dab = "홀"
        print("나 : 너 "+str(my)+"이지?")

# 틀리면 틀렸다
        if my==dab: # 만약에 내가 얘기한 홀과 짝중에 맞으면 맞다
            print("상대 : 넵 ")
            print("나 : 구슬 내놔")
            marble = marble + bet #딴만큼 이득
            # print("당신의 구슬의 갯수: {}개".format(marble))
        else:
            print("상대 : 아닌데요?(씨익)"+str(dab)+"입니다")
            print("나 : 하... 구슬 여기")
            marble = marble - bet
            # print("당신의 구슬의 갯수: {}개".format(marble))
        if marble<=0:
            print("당신의 구슬의 갯수: {}개".format(marble))
            print("패배")
            break
        if marble>=20:
            print("당신의 구슬의 갯수: {}개".format(marble))
            print("승리")
            break