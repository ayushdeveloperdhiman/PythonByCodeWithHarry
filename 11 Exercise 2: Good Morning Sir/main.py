import time
timestamp = time.strftime("%H:%M:%S")
# print(timestamp)
# timestamp = time.strftime('%H')
# print(timestamp)
# timestamp = time.strftime('%M')
# print(timestamp)
# timestamp = time.strftime('%S')
# print(timestamp)
hour = int(timestamp.split(":")[0])
if(hour < 12):
    print("Good Morning Sir")
elif(hour < 17):
    print("Good Afternoon Sir")
else:
    print("Good Evening Sir")