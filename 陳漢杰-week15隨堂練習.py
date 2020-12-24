## 圖案1:畫出幾何彩虹圖案，畫出一排彩色正方形
# (1)準備工(彩色)
import turtle
shelly = turtle.Turtle()
turtle.bgcolor("black") #把背景變黑

# (2)畫出6個正方形，各差30步
for n in range(6):  #畫六個正方形
    colors = ["red","green","blue","gold","purple","yellow"]
    shelly.color(colors[n])  # A.選擇第n個正方形的顏色
    for i in range(4):      # B.畫一個尺寸為25的正方形
        shelly.forward(25)
        shelly.left(90)
    shelly.penup()          # C.畫下一個正方形，前近30步(25+5)
    shelly.forward(30)
    shelly.pendown()

# (3)隱藏海龜
shelly.hideturtle()