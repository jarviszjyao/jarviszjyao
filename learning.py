
# coding=utf-8

i=100; a=0; b=0; c=0

while i <1000:
    a = i // 100
    b = (i - a * 100) // 10
    c = i - a * 100 - b * 10
    if i == (a ** 3 + b ** 3 + c ** 3):
        print("i = " + str(i))
    i += 1



#------------------------break/continue---------------------

# for item in range(10):
#     if item ==3:
#         # break
#         continue
#     print(item)


#--------------------------for in------------------------
# print ("something...")
# for item in 'Hello':
#     if item =='l':
#         break
#     print(item)

# numbers= [43,32,55,74]
# print ("---full sentence---")
# for item in range(100):
#     if item == 81:
#         break
#     print(item)

# -------------------------while else---------------------
# i = 0
# while i * i < 100:
#      i += 1
#      if i == 4:
#           break
#      print (str(i) + '*' + str (i) + '=' + str(i*i))
# else:
#      print ("while is over")


# ---------------------if else-----------------------
# score = int (input("please input 0-100: "))
# if score >=90:
#     word= "You are excellent!"
# elif score>=70:
#     word= "good"
# elif score>=60:
#     word = "keep on"
# else:
#     word ="add oil"
# print (word)
# 