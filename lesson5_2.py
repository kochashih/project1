#一個專案內的主執行的py黨,必須使用____的判斷式
"""
這是一個猜數字遊戲
一個專案的文字說明
"""

import random

if __name__ == "__main__":
    min=1
    max=100
    count=0
    random_value=random.randint(min,max)
    print(random_value)


    print("===猜數字遊戲===")
    while True:
        count +=1
        keyin=int(input(f"輸入數字範圍{min}~{max}:"))
        if keyin>= min and keyin <= max:                           
                if keyin==random_value:
                    print(f"猜對了,答案是{random_value}")                
                    break
                elif keyin>random_value:
                    print("再小一點")
                    max=keyin-1
                elif keyin<random_value:
                    print("再大一點")
                    min=keyin+1   
                #if count==3
                # break     
        else:
            print("超出範圍")        

    print(f"game over 共猜了{count}次")
        


print(keyin)
