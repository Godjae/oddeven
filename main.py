print("오징어 게임에 오신 것을 환영합니다")
print("홀짝 게임을 시작합니다 ")

# 구슬로 홀짝 게임 규칙
# 상대방이 구슬의 갯수를 정한다
a=4
print(a)
# 내가 홀 또는 짝을 얘기한다
my= "홀"
print(my)
# 만약에 내가 얘기한 홀과 짝중에 맞으면 맞다
# 상대방의 구슬의 갯수에서 2로 나누어서 나머지가 0이면 짝
# 나머지가 1이면 홀
dab=""
if a%2 ==0:
    print("짝")
    dab="짝"
else:
    print("홀")
    dab="홀"
# 틀리면 틀렸다
if my==dab:
    print("맞다")
else:
    print("틀리다")