import random

secret = random.randint(1, 100)
guess = int(input("猜猜是哪一个数字："))
if guess == secret:
    print("不错哦，猜对了")
else:
    i = 1
    while (guess != secret) and (i < 5):
        if guess > secret:
            guess = int(input("昂，大了，请重新输入："))
        else:
            guess = int(input("嘿，小了，请重新输入："))
        i += 1
    if guess == secret:
        print("不错哦，猜对了")
    else:
        print("猜数失败，游戏结束。")