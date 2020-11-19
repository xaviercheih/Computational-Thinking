# Input Data
time = 123

# Process
hour = time // 60 #商數
minute = time % 60 #除數

# Output

print(time,"是",hour,"小時",minute,"分鐘")

## Process

hour1 = int(time/60)#除法與整數
minute1 = ((time/60) - hour1)*60
import math
minute1 = round(minute1)

print(time,"是",hour1,"小時",minute1,"分鐘")