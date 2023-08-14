# name = input("What is your name?")
# sur = input("What is your surname?")
# age = input("What is your age?")
# print("Hi", sur, name, "!", "I am also", age )
#
# choice = input("Please enter your choice: computer or smartphones")
# price = input("Please enter your estimated price $:")
# print("Here is the list of 100+", choice, "lower pr equal to $", price)
# import turtle
import random
# name = input("What is your name?")
# number = input("Please enter your number:")
# ad = input("Please enter your address")
# print("Dear", name)
# print("You have been added to database", number, ad)
#
# name = input("What is your name?")
# city = input("Which country do you to go? ")
# stay = input("How many years you want to stay")
# travel = input("How many times you travelled with us? ")
# print("Hi", name, travel, "time", "Specially for you we offer 30% discount for the", stay, "years trip to", city)


# weight = int(input("Please enter luggage weight:"))
# cargo = int(input("Please enter cargo weight"))
# print("Total weight:", weight+cargo)
#
# hotel = int(input("Please enter price of one night in hotel:"))
# day = int(input("Please enter number of days you stay:"))
# print("Total price:", hotel*day)


# spend = int(input("Please enter amount of money you want to spend:"))
# print("You have got 7% cashback with is:$" + str(spend*0.07))
#
# stu_1 = float(input("Please enter GPA of student 1:"))
# stu_2 = float(input("Please enter GPA of student 2:"))
# stu_3 = float(input("Please enter GPA of student 3:"))
# stu_4 = stu_1+stu_2+stu_3
# print("Average GPA of a group is", stu_4/3)


# son = int(input("Enter your money"))
# print(int(son/1000))
# print(int(son//100))
# print(int(son//10))
# print(int(son%12340))

#
# greeting = "Hello, world!"
# greeting = greeting.lower()
# symbol = greeting[0:5]
# result = greeting.find("hello")
# print(symbol)
# print(result)

# feed = input("Please enter you feedback:")
# print("Thank you! You feedback has", len(feed), "symbols")
#
# feedback = "Your restaurant is awesome!"
# result = feedback[19:26]
# print("Thank you  for", result, "feedback")

# feedback = "Abdulloh and Ismoil are good programmers"
# name = feedback[0:18]
# print("Salary of ", name, "should be raised")


# food = input("Please enter dish names you like:")
# result = food.find("kebab")
# result_2 = food.find("chocolate")
# print("kebab", result)
# print("chocolate", result_2)


# rate = int(input("Please rate us:"))
# like = input("Pleaee enter what you liked:")
# print(rate, "-", like)


# give = input("Please enter give us a feedback")
# dish = input("Please enter what you liked:")
# dis = input("Please enter what you disliked:")
# print("Your coupon is 5")

# trip = input("How is your trip?")
# trip_1 = len(trip)
# trip_2 = trip.find("wonderful")
# trip_3 = trip.find("boring")
# print("Your answers has", trip_1, "symbols")
# print("Searching adventages:", trip_2)
# print("Searching disandvantages:", trip_3)

# feedback = "They made ud feel welcomed and gave us amazing experience"
# result = feedback.find("amazing experience")
# result_1 = feedback[result:len(feedback)]
# print(result_1)


# amount_orange = int(input("How many kg of oranges do you want ?"))
# presence_orange = 80
# sell = presence_orange > amount_orange
# print("Deal:", sell)


# price = int(input("What is your estimated price?"))
# min_price = 10
# max_price = 100
# can_buy = price > min_price and price < max_price
# print("Sale:", can_buy)


# price = int(input("What is your estimated price?"))
# min_price = 10
# max_price = 100
# can_buy = price > min_price or price < max_price
# print("Sale:", can_buy)


# if 10 > 15:
#     print("smth")
# else:
#     print("amth again")
#

#
# balance = int(input("Please enter your card balance?"))
# price = int(input("Please enter check price:"))
# if balance >= price:
#     print("Paid")
# else:
#     print("Not enough money")


# purchase = input("Do you want to make a purchase?")
# if purchase == "yes":
#    category = input("Please enter your category:")
#    if category =="phone":
#        print("Recomendation Iphone")
#    if category =="pc":
#         print("Recomendation Acer")
# else:
#        print("When you change your mind let us no")
#

# enter = input("Please enter category:")
# if enter == "pc":
#     price = int(input("Please enter estimated price:"))
#     if price < 500:
#         print("Here is the list of 100+ office PC ")
#     if price >= 500 and price < 1000:
#         print("Here is the list of 100+ premium PC ")
#     if price >= 1000:
#         print("Here is the list of 100+ gaming PC ")
# if enter == "phone":
#     price = int(input("Please enter estimated price:"))
#     if price <100:
#         print("Here is the list of 100+ budjet phone")
#     if price > 100 and price < 499:
#         print("Here is the list of 100+ premium phone ")
#     if price > 100 and price > 500:
#         print("Here is the list of 100+ gaming phone ")
# else:
#     print("When you change your mind let us no")


# item = input("What item you want?")
# if item == "pizza":
#     print("Free delivery for pizza")
# elif item == "burger":
#        print("10% discount on delivery for burger")
# else:
#     print("Paid delivery for", item)

# product = input("Do you want to see our products?")
# if product == "yes":
#     categ = input("Please enter category :")
#     if categ == "pc":
#         video = input("Please enter videocard:")
#         if video == "nvidia":
#             print("NVIDIA GEFORCE")
#         elif video == "amd":
#             print("AMD RADEON")
#         else:
#             print("INTEL GRAPHICS")
#     else:
#         print("Look at our smartphones")
# else:
#     print("Let us know if you change your mind")


# pas = input("Please enter password:")
# while pas != "qwerty":
#     print("Incorrect password")
#     pas = input("Please enter password:")
# print("You have been logged in")


# what = input("What is 2+2*2 ?")
# while what != "6":
#     print("Wrong answer!")
#     if what == "8":
#        print("Note that multiplication has a greater priority")
#     what = input("Please enter your answer again:")
# print("Right anwer!")


# promo = input("Please enter the promocode:")
# while promo != "wylsacom" and promo != "wylsa":
#     print("Incorrect! Please enter the promocode again")
# print("You have a discount")


# total = 0
# price = int(input("Please enter the price:"))
# while price != 0:
#     total = total + price
#     price = int(input("Please enter the price:"))
# print("$", total)


# category = input("Please your category: ")
# new = 0
# while category != "stop":
#     new += 1
#     category = input("Please your category: ")
# print("You have", new, "categories")


# grade = int(input("Please enter your grade:"))
# five = 0
# while grade != 0:
#     grade = int(input("Please enter your grade:"))
#     if grade == 5:
#         five += 1
# print("You have", five, "fives")


# card = int(input("Please enter UzCard number:"))
# number = 1
# while number < 3:
#     print("You have a free coffee!")
#     number += 1
#     card = int(input("Please enter UzCard number:"))
# print("Promotion is over. Please make a payment")


# discount = int(input("Please enter the price:"))
# total = 0
# while discount != 0:
#     total = total + discount
#     discount = int(input("Please enter the price:"))
#     if total / 2:
#         total = total - (total * 0.15)
# print("Total prices:", total)
#
# discount = int(input("Please enter the price:"))
# total = 0
# while discount != 0:
#     total = total + discount
#     discount = int(input("Please enter the price:"))
# if total >= (total / 2):
#     total = total - (total * 0.15)
# print("Total prices:", total)


# def price ():
#   discount = int(input("Please enter the price:"))
#   total = 0
#   count = 0
#   while discount != 0:
#     total += discount
#     discount = int(input("Please enter the price:"))
#   if total % 2 == 0:
#     total = total - (total * 0.15)
#   print("Total prices:", total)


# login = input("Please create your login:")
# wrong = "#()+-=*&!?., "
# for acc in login:
#     if acc in wrong:
#         hidden = ("Forbidden symbol:")
#         print(hidden, acc)


#
# login = input("Encrypt the text :")
# wrong = ("eiouya")
# total = ""
# for acc in login:
#      if acc in wrong:
#          total += "0"
#      else:
#          total += "1"
# print(total)


#
# def check(old):
#     if old < 50:
#         print("Discount: 5%")
#     elif old <100:
#         print("Discount: 10%")
#     else:
#         print("Discount: 20%")
# old = int(input("Please enter your grade:"))
# check(old)


# number = int(input("Please enter number of students:"))
# def average():
#     grade = int(input("Please enter his grades:"))
#     total = 0
#     counter = 0
#     while grade != 0:
#         total += grade
#         grade = int(input("Please enter his grades:"))
#         counter += 1
#         total = total / counter
#     print("Average grade of", name, total)
# for i in range(number):
#   name = input("Please enter student's name:")
#   average()


#
# def check(score):
#     if score < 30:
#       return ("You got complimentary certificate")
#     elif score < 50:
#       return("You got 3'st place ")
#     elif score < 80:
#         return ("You got 2'st place ")
#     else:
#         return ("You got 1'st place ")
# def reward(score):
#     if score < 30:
#       return ("airpods")
#     elif score < 50:
#       return("iphone ")
#     elif score < 80:
#         return ("apple tv ")
#     else:
#         return ("macbook")
# score = int(input("Please enter your score"))
# result = check(score)
# res = reward(score)
# print(result,res)


# def ask():
#     one = input("Ask me something")
#     while one != "stop":
#         if one == "What do you know":
#             print("I can talk with you if you want")
#         elif one == "Tell me joke":
#             print("What is worse than finding a worm in your apple?  Finding half a worm.")
#         else:
#             print("I don't understand")
#         one = input("Ask me something")
#
#
#
# def think():
#   num = int(input("Please enter first number:"))
#   number = int(input("Please enter second number:"))
#   for i in range(2):
#     if num == 5 and number == 7:
#         print("You won!!!")
#         break
#     elif num == 5:
#         print("You guessed first number!")
#     elif number == 7:
#         print("You guessed second number")
#     else:
#         print("Take a change next time")
#     num = int(input("Please enter first number:"))
#     number = int(input("Please enter second number:"))

#
#
#
# name = input("Hi. My name is Chalajon BOT. What is your name?")
# print("What a beautiful name", name, "What is your occupation?")
# bio = input()
# if bio == "study":
#     print("Which university are you studying at?")
#     study = input()
#     if study == "IDU":
#         print("I don't know this university")
#         paid = input("How much you are pay?")
#         print("Don't worry. The money will be found 😂😂😂")
# else:
#     print("Good👍")
# question = input("Do you want to my skills?")
# if question == "yes":
#     print("Here it is")
# else:
#     print("Anyway see my skills")
# menu = int(input('''
# 1- Find the number i think
# 2- Ask me something
# 3- Wonderful price
# 4- Find the arithmetic
# '''))
# while menu != "stop":
#     if menu == 1:
#         think()
#     elif menu == 2:
#         ask()
#     elif menu == 3:
#         price()
#     else:
#         average()


# from time import time, sleep
# stat = time()
# sleep(5)
# end = time()
# period = end - stat
# print(period)

#
# from time import time, sleep
# start = int(input("Enter 1-start"))
# while start != 0:
#     if start == 1:
#         time_start = time()
#     else:
#         print("There is no such command!")
#     start = int(input("Enter 0-stop"))
# end = time()
# passed = end-time_start
# print(passed)


# from turtle import *
# color("brown")
# forward(95)
# left(135)
# color("blue")
# forward(130)
# left(135)
# color("brown")
# forward(93)
# left(90)
# width(5)
# exitonclick()


# letter = input("Enter the word:")
# for i in letter:
#     if i.isdigit():
#         break
#     print(i)

#



# from turtle import *
# def labirint():
#   pensize(16)
#   color("brown")
#   left(90)
#   forward(150)
#   pensize(8)
#   color("green")
#
#
#   side = 10
#   for i in range(22):
#       forward(side)
#       left(90)
#       side+= 5
#   exitonclick()
# labirint()



#
# from turtle import *
# def amongus():
#      pensize(20)
#      right(90)
#      forward(50)
#      right(180)
#      circle(40, -180)
#      right(180)
#      forward(200)
#      right(180)
#      circle(100, -180)
#      left(90)
#      circle(50, -180)
#      right(90)
#      forward(100)
#      left(180)
#      circle(40, -180)
#      right(180)
#      forward(45)
#      right(90)
#      forward(10)
#      left(90)
#      circle(25, -180)
#      up()
#      right(230)
#      forward(100)
#      left(90)
#      forward(20)
#      right(90)
#      down()
#      begin_fill()
#      right(150)
#      circle(90, -55)
#
#      right(180)
#      forward(1)
#      right(180)
#      circle(10, -65)
#      right(180)
#      forward(110)
#      right(180)
#
#      circle(50, -190)
#      right(170)
#      forward(80)
#
#      right(180)
#      circle(45, -30)
#
#      end_fill()
#      exitonclick()
# amongus()
#


# from turtle import *
# t = Turtle()
# t.shape("turtle")
# t.speed(100)
#
# def move (x, y):
#    t.penup()
#    t.goto(x, y)
#    t.pendown()
# scr = t.getscreen()
# scr.onscreenclick(move)
# done()


# from turtle import *
# t = Turtle()
# t.shape("turtle")
# t.color("red")
# t.width(5)
# def Up():
#     t.goto(t.xcor(), t.ycor()+10)
#     t.setheading(90)
# def down():
#     t.goto(t.xcor(), t.ycor()-10)
#     t.setheading(-90)
# def left():
#     t.goto(t.xcor()-10, t.ycor())
#     t.setheading(180)
# def right():
#     t.goto(t.xcor()+10, t.ycor())
#     t.setheading(0)
# def x():
#     t.begin_fill()
# def y():
#     t.end_fill()
# def b():
#     t.color("blue")
# def p():
#     t.color("pink")
# scr = t.getscreen()
# scr.listen()
# scr.onkey(Up, "Up")
# scr.onkey(down, "Down")
# scr.onkey(right, "Right")
# scr.onkey(left, "Left")
# scr.onkey(b,"b")
# scr.onkey(p,"p")
# scr.onkey(x, "x")
# scr.onkey(y, "y")
# done()



# from turtle import *
# from random import randint
# from time import *
# t = Turtle()
# t.shape("turtle")
# t.color("red")
# while True:
#     t.penup()
#     x = randint(-100, 100)
#     y = randint(-100, 100)
#     t.goto(x, y)
#     t.pendown()
#     sleep(2)





# class Clash():
#     def __init__(self, name, health, armor, weapon, power):
#         self.name= name
#         self.health= health
#         self.armor= armor
#         self.weapon= weapon
#         self.power= power
#     def show(self):
#         print("Name:", self.name)
#         print("Health:", self.health)
#         print("Armor:", self.armor)
#         print("Weapon:", self.weapon)
#         print("Power:", self.power, "\n")
#     def fight(self, opppenent):
#         print(self.name, "attacks", show.name , "wi")
#
#
#
# pekka = Clash("GREAT THE HERO! P.E.K.K.A", "4000", "4000", "Sword", "3000")
# golem = Clash("GREAT THE HERO! GOLEM", "4000", "4000", "Stone Fists", "1000")
# pekka.show()
# golem.show()



#
# from time import sleep
# class Hero():
#     def __init__(self, name, health, armor, weapon, power):
#         self.name = name
#         self.health = health
#         self.armor = armor
#         self.weapon = weapon
#         self.power = power
#
#
#     def print_info(self):
#         print("GREAT THE HERO!", self.name)
#         sleep(0.5)
#         print('Health:', self.health)
#         sleep(0.5)
#         print('Armor:', self.armor)
#         sleep(0.5)
#         print('Weapon:', self.weapon)
#         sleep(0.5)
#         print('Power:', self.power, '\n')
#         sleep(1.5)
#
#     def attack(self, enemy):
#         print(self.name, 'attacks', enemy.name, 'with', self.weapon)
#         enemy.armor -= self.power
#         if enemy.armor < 0:
#             enemy.health += enemy.armor
#             enemy.armor = 0
#         sleep(1.5)
#
#
#     def fight(self, opponent):
#         while self.health > 0 and opponent.health > 0:
#             self.attack(opponent)
#             if opponent.health < 0:
#                 print('Fight is over.', self.name, 'has won!')
#                 opponent.health = 0
#                 print(opponent.name, 'took damage. His armor:', opponent.armor, 'and His health:', opponent.health,
#                       '\n')
#
#                 break
#             print(opponent.name, 'took damage. His armor:', opponent.armor, 'and His health:', opponent.health, '\n')
#
#             opponent.attack(self)
#             if self.health < 0:
#                 print('Fight is over', opponent.name, 'has won!')
#                 self.health = 0
#                 print(opponent.name, 'took damage. His armor:', opponent.armor, 'and His health:', opponent.health,
#                       '\n')
#
#                 break
#             print(opponent.name, 'took damage. His armor:', opponent.armor, 'and His health:', opponent.health, '\n')
#
#
#
#
# pekka = Hero('P.E.K.K.A', 4000, 4000, 'sword', 3000)
# golem = Hero('GOLEM', 6000, 4000, 'stone fists', 1000)
# pekka.print_info()
# golem.print_info()
# print(pekka.name, 'encountered', golem.name)
# sleep(1.5)
# print(pekka.name, 'VS', golem.name)
# sleep(1.5)
# print('FIGHT')
# sleep(1.5)
# pekka.attack(golem)
# golem.attack(pekka)
# pekka.fight(golem)

#
# from time import sleep
# class Hero():
#     def __init__(self, name, health, armor, weapon, power):
#         self.name = name
#         self.health = health
#         self.armor = armor
#         self.weapon = weapon
#         self.power = power
#     def info(self):
#         print("Name", self.name)
#         sleep(0.5)
#         print('Health:', self.health)
#         sleep(0.5)
#         print('Armor:', self.armor)
#         sleep(0.5)
#         print('Weapon:', self.weapon)
#         sleep(0.5)
#         print('Power:', self.power, '\n')
#         sleep(1.5)
# class Dragon(Hero):
#     def flying(self):
#         pass
#     def fire(self, enemy):
#         pass
# class Wizard(Hero):
#     def firebol(self):
#         pass


# courses = list()
# course = input("Please enter your course: ")
# while course != "0":
#     courses.append(course)
#     course = input("Please enter your course: ")
# print("All your", len(courses), "course have been added to the timetable")



# names = list()
# mate = input("Please enter your classmates name :")
# while mate != "0":
#     names.append(mate)
#     mate = input("Please enter your classmate name :")
# print("Your classmates:")
# count = 0
# for mate in names:
#     count += 1
#     print(count, mate)




# books = ["Oltin silsila,", "Ruxiy tarbiya,", "Hadis va hayot"]
# book = input("Please enter your choice:")
# if book in books:
#     print("You can take it")
# else:
#     add = input("We don't have it. Would you like to add it?")
#     if add =="yes":
#          books.append(book)
#          print("Thank you!  It has been added")
#          print("Update box list: ", books)
#     else:
#         print("We are sad we could not halp you")



# space = input("Please enter your grades separated by a space:").split(" ")
# count = 0
# for grade in space:
#     if grade == "5":
#        count += 1
# print("You have", count, "fives")



#
# phone = {
#     'Iphone 14': 1200,
#     'Samsung Flip': 1100,
#     'MI 13 Pro': 1000
# }
# titles = list(phone.keys())
# print(phone)
# choice = input('Please enter your choice:')
# if choice in phone:
#     print(phone[choice])
# else:
#     print("We don't have that phone")






# names = {
#     1: 'Ismoil',
#     2: 'Ibrohim',
#     3: 'Abdulloh'
# }
# print("ID:", list(names.keys()))
# stu_id = int(input("Please enter your student's ID"))
# if stu_id in names:
#     print(names[stu_id])
# else:
#     new = input("No info. Do you want to add a new student?")
#     if new == 'yes':
#         name = input('Please enter his name:')
#         names[len(names)+1] = name
#         print("Updated:", names)
#     else:
#         print("Good bye🖐️🖐️🖐️")


#
# students = {
#     'Ismoil':{
#         'age':19,
#         'address': 'Olmazor',
#         'tel': '+99839696969',
#         'faculty': 'CF',
#         'extra courses': ['Python', 'Practicum']
#     },
#     'Islom':{
#         'age': 20,
#         'address': 'Shayhontohur',
#         'tel': '+9983945455569',
#         'faculty': 'BF',
#         'extra courses': ['Python', 'SMM']
#     }
# }
#
# name = input('Please enter student name:')
# if name in students:
#     info = input("What do you want to know about this student?")
#     dic = students[name][info]
#     print(dic)


# def fact(n):
#     if n <= 1:
#         return 1
#     else:
#         return n + fact(n-1)
# print(fact(6))

