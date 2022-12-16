import random

def play_one():
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
                    
            else:
                print("超出範圍")        

        print(f"game over 共猜了{count}次")
            
        print(keyin)
     
def play_game():
     while True:
        play_one()
        play_agnin=input("要繼續玩嗎?(y,n)")
        if play_agnin.lower()=="n":       #lower 字母變小寫 則即使輸入大寫N 也會轉成小寫 達到結束的目的
            break

                                            #funtion內可呼叫其他funtion
if __name__ == "__main__":
    play_game()

