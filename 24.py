import random
import time
print("游戏开始！")
time.sleep(0.5)

hand = []
num = 0
def fapai():
    for i in range(8):
        print("\r正在发牌."+'.'*(i%4)+'   ',end = "")
        time.sleep(0.3)
    hand.append(random.randint(1,13))
    print("\r您的牌为：",hand[-1])

gameover = False
continu = True

while continu:
    fapai()
    inp = input("是否继续发牌？")
    if inp != "y":
        continu = False
print("您的牌为：",end = "")
for i in hand:
    num = i+num
    print(i,"",end = "")
print("\n您的牌点为：",num)
if num >24:
    print("您输了")
