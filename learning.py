
# coding=utf-8


#--------------------------for in------------------------
print ("something...")
for item in 'Hello':
    if item =='l':
        break
    print(item)

numbers= [43,32,55,74]
print ("---full sentence---")
for item in numbers:
    if item == 55:
        break
    print(item)

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