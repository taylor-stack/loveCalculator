# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
lovers = name1 + name2
lowercase_lovers = lovers.lower()

t = lowercase_lovers.count("t")
r = lowercase_lovers.count("r")
u = lowercase_lovers.count("u")
e = lowercase_lovers.count("e")

true = t + r + u + e

l = lowercase_lovers.count("l")
o = lowercase_lovers.count("o")
v = lowercase_lovers.count("v")
e = lowercase_lovers.count("e")

love = l + o + v + e

lovescore = str(true) + str(love)

lovescorefinal = str(lovescore)

int_score = int(lovescore)

if (int_score < 10) or (int_score > 90):
  print("Your love score is" + " " + lovescorefinal)
  print("You go together like vanilla and Coke!")

else:
  print("Your score is" + " " + lovescorefinal)
  print("You are alright together.")