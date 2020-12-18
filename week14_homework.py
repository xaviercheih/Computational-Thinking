import turtle
turtle.pensize(3) # 畫筆大小
turtle.pencolor("yellow") # 畫筆顏色
turtle.fillcolor("red") # 填充顏色
turtle.begin_fill() # 開始填充
for i in range(5):
turtle.forward(200) # 五角星的邊長200像素
turtle.left(144) # 畫筆旋轉角度
turtle.end_fill() # 填充完成
