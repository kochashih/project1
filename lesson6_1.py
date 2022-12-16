def sayhello():             #沒有參數的funtion
    print("hello")

def sayhello_withname(name):        #有一個參數的funtion
    print(f"Hello{name}")

def square_area(side): #有一個參數 同時有傳出值
    area = side **2 #funtion內的變數
    return area  #傳出area的值    

def rectangle(width,height):   #矩形 長高 兩參數
    area=width*height         #area與 square的area不衝突 因在不同funtion之中
    return area   


if __name__=="__main__":
    #sayhello_withname("wayne")        #引數值傳遞至name參數內
    
    #先執行8 再執行9 再執行5 再執行10 10沒有程式 就結束

    side=eval(input("請輸入正方形邊長"))
    area = square_area(side)   #area為文件變數 與funtion內變數area,side不衝突
    print(f"正方形,一邊為{side},面積為{area}")

    area=rectangle(10.5,20.9)
    print(f"矩形的寬是10.5,高是20.9,面積為{area}")   #執行到後面會把前面執行過的area的值蓋過去 所以可以直接使用area

