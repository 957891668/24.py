import random
import time
print("游戏开始！")
time.sleep(0.5)

def fapai():
    for i in range(8):
        print("\r正在发牌."+'.'*(i%4)+'   ',end = "")
        time.sleep(0.4)
    print("\r您的牌为：",random.randint(1,13))
fapai()
